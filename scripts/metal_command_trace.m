// Trace completed Metal command buffers in an isolated benchmark operation.
#import <Foundation/Foundation.h>
#import <Metal/Metal.h>
#import <objc/runtime.h>
#import <stdatomic.h>

static _Atomic bool tracing;
static dispatch_group_t pending;
static FILE *output;
static IMP original_commit;
static _Atomic unsigned sequence;

static IMP replace_method(Class cls, SEL selector, IMP replacement) {
    Method method = class_getInstanceMethod(cls, selector);
    if (!method) return NULL;
    IMP original = method_getImplementation(method);
    if (!class_addMethod(cls, selector, replacement, method_getTypeEncoding(method))) {
        method_setImplementation(method, replacement);
    }
    return original;
}

static void traced_commit(id<MTLCommandBuffer> buffer, SEL selector) {
    if (atomic_load(&tracing)) {
        unsigned index = atomic_fetch_add(&sequence, 1);
        dispatch_group_enter(pending);
        [buffer addCompletedHandler:^(id<MTLCommandBuffer> finished) {
            fprintf(output, "%u\t%ld\t%.9f\t%.9f\t%s\n", index, (long)finished.status,
                    finished.GPUStartTime, finished.GPUEndTime,
                    finished.device.name.UTF8String);
            dispatch_group_leave(pending);
        }];
    }
    ((void (*)(id, SEL))original_commit)(buffer, selector);
}

int trace_install(void) {
    @autoreleasepool {
        id<MTLDevice> device = MTLCreateSystemDefaultDevice();
        id<MTLCommandBuffer> probe = [[device newCommandQueue] commandBuffer];
        if (!probe) return 0;
        Class cls = object_getClass(probe);
        SEL selector = @selector(commit);
        original_commit = replace_method(cls, selector, (IMP)traced_commit);
        if (!original_commit) return 0;
        pending = dispatch_group_create();
        return 1;
    }
}

int trace_begin(const char *path) {
    output = fopen(path, "w");
    if (!output) return 0;
    fputs("sequence\tstatus\tgpu_start_s\tgpu_end_s\tdevice\n", output);
    atomic_store(&sequence, 0);
    atomic_store(&tracing, true);
    return 1;
}

void trace_end(void) {
    atomic_store(&tracing, false);
    dispatch_group_wait(pending, DISPATCH_TIME_FOREVER);
    fclose(output);
}

// Optional dispatch observation. Record the pipeline active at each direct dispatch.
static FILE *dispatch_output;
static IMP original_set_pipeline;
static IMP original_dispatch_threads;
static IMP original_dispatch_groups;
static char pipeline_key;
static char function_key;
typedef id<MTLComputePipelineState> (*NewFunctionPipeline)(
    id, SEL, id<MTLFunction>, NSError **) __attribute__((ns_returns_retained));
typedef id<MTLComputePipelineState> (*NewDescriptorPipeline)(
    id, SEL, MTLComputePipelineDescriptor *, MTLPipelineOption,
    MTLComputePipelineReflection **, NSError **) __attribute__((ns_returns_retained));
static NewFunctionPipeline original_new_function_pipeline;
static NewDescriptorPipeline original_new_descriptor_pipeline;

__attribute__((ns_returns_retained))
static id<MTLComputePipelineState> traced_new_function_pipeline(
    id device, SEL selector, id<MTLFunction> function, NSError **error) {
    id<MTLComputePipelineState> state = original_new_function_pipeline(
        device, selector, function, error);
    if (state) objc_setAssociatedObject(state, &function_key, function.name, OBJC_ASSOCIATION_COPY);
    return state;
}

__attribute__((ns_returns_retained))
static id<MTLComputePipelineState> traced_new_descriptor_pipeline(
    id device, SEL selector, MTLComputePipelineDescriptor *descriptor,
    MTLPipelineOption options, MTLComputePipelineReflection **reflection, NSError **error) {
    id<MTLComputePipelineState> state = original_new_descriptor_pipeline(
        device, selector, descriptor, options, reflection, error);
    if (state) {
        objc_setAssociatedObject(state, &function_key, descriptor.computeFunction.name,
                                 OBJC_ASSOCIATION_COPY);
    }
    return state;
}

static void traced_set_pipeline(id encoder, SEL selector, id<MTLComputePipelineState> state) {
    if (atomic_load(&tracing) && dispatch_output) {
        NSString *name = objc_getAssociatedObject(state, &function_key) ?: state.label;
        objc_setAssociatedObject(encoder, &pipeline_key, name, OBJC_ASSOCIATION_COPY);
    }
    ((void (*)(id, SEL, id))original_set_pipeline)(encoder, selector, state);
}

static void record_dispatch(id encoder, const char *kind, MTLSize grid, MTLSize group) {
    if (atomic_load(&tracing) && dispatch_output) {
        NSString *label = objc_getAssociatedObject(encoder, &pipeline_key);
        fprintf(dispatch_output, "%s\t%s\t%lux%lux%lu\t%lux%lux%lu\n",
                kind, label.UTF8String ?: "<unlabeled>",
                grid.width, grid.height, grid.depth, group.width, group.height, group.depth);
    }
}

static void traced_dispatch_threads(id encoder, SEL selector, MTLSize grid, MTLSize group) {
    record_dispatch(encoder, "threads", grid, group);
    ((void (*)(id, SEL, MTLSize, MTLSize))original_dispatch_threads)(encoder, selector, grid, group);
}

static void traced_dispatch_groups(id encoder, SEL selector, MTLSize grid, MTLSize group) {
    record_dispatch(encoder, "threadgroups", grid, group);
    ((void (*)(id, SEL, MTLSize, MTLSize))original_dispatch_groups)(encoder, selector, grid, group);
}

int trace_install_dispatch(void) {
    @autoreleasepool {
        id<MTLDevice> device = MTLCreateSystemDefaultDevice();
        id<MTLCommandBuffer> buffer = [[device newCommandQueue] commandBuffer];
        id<MTLComputeCommandEncoder> encoder = [buffer computeCommandEncoderWithDispatchType:
                                                MTLDispatchTypeConcurrent];
        if (!encoder) return 0;
        Class cls = object_getClass(encoder);
        [encoder endEncoding];
        original_set_pipeline = replace_method(
            cls, @selector(setComputePipelineState:), (IMP)traced_set_pipeline);
        original_dispatch_threads = replace_method(
            cls, @selector(dispatchThreads:threadsPerThreadgroup:), (IMP)traced_dispatch_threads);
        original_dispatch_groups = replace_method(
            cls, @selector(dispatchThreadgroups:threadsPerThreadgroup:), (IMP)traced_dispatch_groups);
        original_new_function_pipeline = (NewFunctionPipeline)replace_method(
            object_getClass(device), @selector(newComputePipelineStateWithFunction:error:),
            (IMP)traced_new_function_pipeline);
        original_new_descriptor_pipeline = (NewDescriptorPipeline)replace_method(
            object_getClass(device),
            @selector(newComputePipelineStateWithDescriptor:options:reflection:error:),
            (IMP)traced_new_descriptor_pipeline);
        return original_set_pipeline && original_dispatch_threads && original_dispatch_groups
            && original_new_function_pipeline && original_new_descriptor_pipeline;
    }
}

int trace_begin_dispatch(const char *path) {
    dispatch_output = fopen(path, "w");
    if (!dispatch_output) return 0;
    fputs("dispatch\tpipeline\tgrid\tthreads_per_group\n", dispatch_output);
    return 1;
}

void trace_end_dispatch(void) {
    fclose(dispatch_output);
    dispatch_output = NULL;
}

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
        Method method = class_getInstanceMethod(cls, selector);
        if (!method) return 0;
        original_commit = method_getImplementation(method);
        if (!class_addMethod(cls, selector, (IMP)traced_commit, method_getTypeEncoding(method))) {
            method_setImplementation(method, (IMP)traced_commit);
        }
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

# Contributing

Keep changes focused on reproducible measurements and correctness. Provide a small configuration, seed, dependency versions and redacted failure record with a bug report.

Run pytest, Ruff and mypy before proposing changes. Mark tests that require Metal with apple_gpu. Keep generic CI usable on Linux. Run GPU integration tests sequentially on an Apple Silicon Mac.

Changes to dependencies or backend classification need a source review of dispatch, precision and synchronization behavior. Preserve failures in raw records and expose correctness status in summaries. Shared objective names alone do not establish solver equivalence.

Avoid committing generated datasets, virtual environments, private paths, credentials and large local runs. Use scripts/export_results.py for an evidence bundle, then inspect the generated files. Upstream code reuse must preserve applicable licenses and notices.

Future backends should extend the existing adapters and isolated worker contract. xgboost-metal and stock XGBoost need separate environments because they expose the same import name.

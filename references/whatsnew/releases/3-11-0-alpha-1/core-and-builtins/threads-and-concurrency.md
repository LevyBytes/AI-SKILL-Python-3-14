# Python 3.11.0 alpha 1 / core and builtins / threads and concurrency

[bpo-44590](https://bugs.python.org/issue?@action=redirect&bpo=44590): Everything required to run a Python function (local variables, stack, and so on) now lives on a per-thread stack. Frame objects get allocated lazily only when required. This lifts performance by roughly 7% across the standard benchmark suite. Because frame objects remain available whenever they are needed, introspection and debugging are not affected. Mark Shannon wrote the patch.

[bpo-44032](https://bugs.python.org/issue?@action=redirect&bpo=44032): Relocated "fast" locals together with other variables off the frame object and onto a per-thread datastack.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

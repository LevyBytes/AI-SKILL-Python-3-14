# Single-threaded performance

### Single-threaded performance

Running Python code on the free-threaded build carries extra cost relative to the standard GIL-enabled build. How much that costs varies with both the workload and the hardware involved. Measured against the pyperformance benchmark suite, the typical penalty spans roughly 1% on macOS aarch64 up to 8% on x86-64 Linux systems.

[Subject index](INDEX.md) · [Previous source context](iterators.md) · [Following source context](behavioral-changes.md)

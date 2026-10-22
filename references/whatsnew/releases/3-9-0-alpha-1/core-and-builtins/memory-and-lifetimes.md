# Python 3.9.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-37257](https://bugs.python.org/issue?@action=redirect&bpo=37257): The small object allocator of Python (`obmalloc.c`) now lets (at most) a single empty arena stay ready for immediate reuse without handing it back to the OS. That stops thrashing in plain loops where an arena would otherwise be freshly created and torn down on every pass.

[bpo-38124](https://bugs.python.org/issue?@action=redirect&bpo=38124): Repaired an off-by-one mistake within PyState_AddModule capable of producing out-of-bounds memory access.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

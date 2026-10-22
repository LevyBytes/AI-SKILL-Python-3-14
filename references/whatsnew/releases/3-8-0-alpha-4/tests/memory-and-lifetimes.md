# Python 3.8.0 alpha 4 / tests / memory and lifetimes

[bpo-36560](https://bugs.python.org/issue?@action=redirect&bpo=36560): Made reference-leak hunting in regrtest more reliable: the deltas (reference count, allocated memory blocks, file descriptor count) are now also computed during warmup, guaranteeing everything is set up before leak hunting begins.

[bpo-36436](https://bugs.python.org/issue?@action=redirect&bpo=36436): Corrected `_testcapi.pymem_buffer_overflow()` so a failed memory allocation is handled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

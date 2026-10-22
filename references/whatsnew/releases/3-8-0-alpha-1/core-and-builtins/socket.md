# Python 3.8.0 alpha 1 / core and builtins / socket

[bpo-34353](https://bugs.python.org/issue?@action=redirect&bpo=34353): Add the ?socket? option to the `stat.filemode()` Python implementation so it lines up with the C implementation.

[bpo-35050](https://bugs.python.org/issue?@action=redirect&bpo=35050): [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket): Correct an off-by-one defect in the length validation for `AF_ALG` name and type.

[bpo-29832](https://bugs.python.org/issue?@action=redirect&bpo=29832): Dropped mentions of "getsockaddrarg" from several socket error messages. Patch by Oren Milman.

[bpo-35214](https://bugs.python.org/issue?@action=redirect&bpo=35214): To sidestep false positives coming from posix, socket, time, test_io, and test_faulthandler, build instrumentation for the clang Memory Sanitizer was introduced.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

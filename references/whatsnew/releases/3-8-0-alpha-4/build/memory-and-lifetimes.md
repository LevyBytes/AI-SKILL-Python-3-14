# Python 3.8.0 alpha 4 / build / memory and lifetimes

[bpo-36618](https://bugs.python.org/issue?@action=redirect&bpo=36618): When the clang compiler is detected, append `-fmax-type-align=8` to CFLAGS. pymalloc, the memory allocator, lines memory up on 8-byte boundaries. By default on x86-64, clang assumes 16-byte alignment and therefore emits the MOVAPS instruction, which can trigger a segmentation fault. Telling clang that Python only guarantees 8-byte alignment makes it pick MOVUPS instead: that path runs slower yet avoids a SIGSEGV when memory isn't 16-byte aligned. Unfortunately the flag has to land in `CFLAGS` rather than only `CFLAGS_NODIST`, because third party C extensions may hit the very same problem.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

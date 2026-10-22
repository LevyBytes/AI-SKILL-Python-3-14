# Python 3.11.0 alpha 7 / library / faulthandler

[bpo-46968](https://bugs.python.org/issue?@action=redirect&bpo=46968): Within [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler), test whether the “sys/auxv.h” header is present so that systems lacking that header don’t hit compilation trouble. Pablo Galindo contributed the patch

[bpo-46968](https://bugs.python.org/issue?@action=redirect&bpo=46968): [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler): Beginning with Linux 5.14, the size of the signal-handler stack that CPython allocates is worked out at runtime via `getauxval(AT_MINSIGSTKSZ)`. With this change, a Python extension can ask the Linux kernel to enable the AMX_TILE instruction set on the Sapphire Rapids Xeon processor and succeed, which clears the way for that ISA inside frameworks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

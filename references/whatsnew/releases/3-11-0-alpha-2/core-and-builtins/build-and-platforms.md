# Python 3.11.0 alpha 2 / core and builtins / build and platforms

[bpo-45526](https://bugs.python.org/issue?@action=redirect&bpo=45526): Within obmalloc, configure ADDRESS_BITS so that no bits are discarded (16 were discarded before). This is the safer choice should the kernel hand user-space virtual addresses covering a range wider than 48 bits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

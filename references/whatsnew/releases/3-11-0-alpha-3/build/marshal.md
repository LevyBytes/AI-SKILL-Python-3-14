# Python 3.11.0 alpha 3 / build / marshal

[bpo-45696](https://bugs.python.org/issue?@action=redirect&bpo=45696): For frozen modules, skip the marshal step by emitting C code that yields a collection of code objects already prepared for use. This trims startup time by a further 10% or more.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

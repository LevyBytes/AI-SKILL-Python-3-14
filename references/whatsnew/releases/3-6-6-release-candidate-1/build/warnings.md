# Python 3.6.6 release candidate 1 / build / warnings

[bpo-5755](https://bugs.python.org/issue?@action=redirect&bpo=5755): Relocated the `-Wstrict-prototypes` option out of `OPT` and into `CFLAGS_NODIST`. The option produced irritating warnings during the build of C++-written extension modules.

[bpo-33012](https://bugs.python.org/issue?@action=redirect&bpo=33012): Supplied `-Wno-cast-function-type` under gcc 8 to mute warnings concerning function casts, such as a cast to PyCFunction inside method definition lists.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 5 / build / sys

[bpo-1294959](https://bugs.python.org/issue?@action=redirect&bpo=1294959): Give the configure script a `--with-platlibdir` option: the name of the platform-specific library directory, which is recorded in the new [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir) attribute. It serves to construct the path for platform-specific extension modules as well as the path of the standard library. On the majority of platforms it equals `"lib"`. Under Fedora and SuSE it equals `"lib64"` on 64-bit platforms. Jan Matějek, Matěj Cepl, Charalampos Stratakis and Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

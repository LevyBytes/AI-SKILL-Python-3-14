# Python 3.8.0 alpha 4 / library / modulefinder

[bpo-35936](https://bugs.python.org/issue?@action=redirect&bpo=35936): The reliance of [`modulefinder`](https://docs.python.org/3.14/library/modulefinder.html#module-modulefinder) on the deprecated [`imp`](https://docs.python.org/3.14/library/imp.html#module-imp) module is gone, and the constructor for [`modulefinder.ModuleFinder`](https://docs.python.org/3.14/library/modulefinder.html#modulefinder.ModuleFinder) now uses immutable defaults. Brandt Bucher authored the patch.

[bpo-35376](https://bugs.python.org/issue?@action=redirect&bpo=35376): [`modulefinder`](https://docs.python.org/3.14/library/modulefinder.html#module-modulefinder) now deals properly with a module sharing its name with a broken package. Brandt Bucher authored the patch.

[bpo-17396](https://bugs.python.org/issue?@action=redirect&bpo=17396): A syntax error in a followed import no longer crashes [`modulefinder`](https://docs.python.org/3.14/library/modulefinder.html#module-modulefinder). Brandt Bucher authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

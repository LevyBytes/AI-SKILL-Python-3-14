# Python 3.14.0 alpha 6 / library / zipimport

[gh-57537](https://github.com/python/cpython/issues/57537): Brings breakpoint support for [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport) modules into [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)

[gh-125746](https://github.com/python/cpython/issues/125746): Removal of the deprecated [`zipimport.zipimporter.load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) has been pushed back to 3.15. Reach for [`zipimport.zipimporter.exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module) as the replacement.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

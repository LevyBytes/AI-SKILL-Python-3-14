# Python 3.11.0 alpha 6 / library / locale

[bpo-46659](https://bugs.python.org/issue?@action=redirect&bpo=46659): The [`locale.getdefaultlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getdefaultlocale) function carries a deprecation and is slated for removal in Python 3.13. Reach instead for the [`locale.setlocale()`](https://docs.python.org/3.14/library/locale.html#locale.setlocale), [`locale.getpreferredencoding(False)`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) and [`locale.getlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getlocale) functions. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

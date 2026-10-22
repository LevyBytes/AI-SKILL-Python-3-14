# Python 3.9.0 alpha 3 / library / os

[bpo-38878](https://bugs.python.org/issue?@action=redirect&bpo=38878): The __subclasshook__ of [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) was fixed to give the right answer across inheritance. Bar Harel wrote the patch.

[bpo-39413](https://bugs.python.org/issue?@action=redirect&bpo=39413): Windows now also provides the [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv) function.

[bpo-39395](https://bugs.python.org/issue?@action=redirect&bpo=39395): Both the [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv) and [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv) functions can now be used on every platform.

[bpo-39406](https://bugs.python.org/issue?@action=redirect&bpo=39406): Where the `setenv()` C function exists, [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv) now relies on `setenv()` rather than `putenv()`, freeing Python from managing the environment variable memory itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 5 / library / compileall

[bpo-39769](https://bugs.python.org/issue?@action=redirect&bpo=39769): The *ddir* parameter of the [`compileall.compile_dir()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_dir) function, together with the `-d` flag on the compileall command line, no longer records the incorrect pathname into the produced pyc file for submodules nested under the root of the compiled directory tree. The regression that Python 3.5 introduced is thereby fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's New In Python 3.7 / py_compile - compileall, py_compile

### py_compile

[`py_compile.compile()`](https://docs.python.org/3.14/library/py_compile.html#py_compile.compile) – and therefore [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) too – now honors the `SOURCE_DATE_EPOCH` environment variable by always producing `.pyc` files set up for hash-based validation. Creating `.pyc` files eagerly this way guarantees [reproducible builds](https://reproducible-builds.org/) of them. (Contributed by Bernhard M. Wiedemann in [bpo-29708](https://bugs.python.org/issue?@action=redirect&bpo=29708).)

[Subject index](INDEX.md) · [Previous source section](pdb.md) · [Next source section](pydoc.md) · [Release/subject declaration](summary-release-highlights.md)

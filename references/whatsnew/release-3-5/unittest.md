# What’s New In Python 3.5 / unittest - unittest

### unittest

A keyword-only argument named *pattern*, forwarded to `load_tests` as its third argument, is now accepted by the [`TestLoader.loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule) method. Discovered packages are now examined for `load_tests` no matter whether their path lines up with *pattern*, since no package name could possibly satisfy the default pattern. Robert Collins and Barry A. Warsaw contributed this (see [bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662)).

Errors hit during unittest discovery are now surfaced via the [`TestLoader.errors`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.errors) attribute on the [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) instance. Robert Collins landed this (see [bpo-19746](https://bugs.python.org/issue?@action=redirect&bpo=19746)).

To display local variables within tracebacks, there is a new `--locals` command line option. Robert Collins contributed this (see [bpo-22936](https://bugs.python.org/issue?@action=redirect&bpo=22936)).

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](unittest-mock.md) · [Release/subject declaration](summary-release-highlights.md)

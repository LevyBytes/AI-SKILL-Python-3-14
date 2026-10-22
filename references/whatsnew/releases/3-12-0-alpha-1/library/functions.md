# Python 3.12.0 alpha 1 / library / functions

[gh-94169](https://github.com/python/cpython/issues/94169): Both `io.OpenWrapper` and `_pyio.OpenWrapper` — deprecated as of Python 3.10 — have been dropped; simply reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open). The `open()` ([`io.open()`](https://docs.python.org/3.14/library/io.html#io.open)) callable is built in. As of Python 3.10, `_pyio.open()` also became a static method. Victor Stinner supplied the patch.

[bpo-41287](https://bugs.python.org/issue?@action=redirect&bpo=41287): Corrected how the `doc` argument behaves within subclasses of [`property()`](https://docs.python.org/3.14/library/functions.html#property).

[bpo-45393](https://bugs.python.org/issue?@action=redirect&bpo=45393): Corrected the layout of `await x` and `not x` within the operator precedence table shown by the [`help()`](https://docs.python.org/3.14/library/functions.html#help) system.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

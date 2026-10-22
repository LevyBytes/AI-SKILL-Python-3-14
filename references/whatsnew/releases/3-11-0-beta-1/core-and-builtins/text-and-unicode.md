# Python 3.11.0 beta 1 / core and builtins / text and unicode

[bpo-34093](https://bugs.python.org/issue?@action=redirect&bpo=34093): For every interned string, `marshal.dumps()` now applies `FLAG_REF`. The output becomes more deterministic this way, which aids reproducible build.

[gh-91576](https://github.com/python/cpython/issues/91576): Make iterating ascii strings 50% faster. Kumar Aditya authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

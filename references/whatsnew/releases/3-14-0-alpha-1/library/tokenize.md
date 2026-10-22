# Python 3.14.0 alpha 1 / library / tokenize

[gh-119118](https://github.com/python/cpython/issues/119118): Cure a performance regression within the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module by caching the `line` token attribute and computing the column offset more efficiently.

[gh-125008](https://github.com/python/cpython/issues/125008): A bug where [`tokenize.untokenize()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.untokenize) emitted invalid syntax for double braces that followed certain escape characters is fixed.

[gh-120343](https://github.com/python/cpython/issues/120343): Correct the column-offset reporting in the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module for tokens that follow multiline f-strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

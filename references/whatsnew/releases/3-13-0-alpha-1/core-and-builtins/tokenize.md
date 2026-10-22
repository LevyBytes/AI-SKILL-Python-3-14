# Python 3.13.0 alpha 1 / core and builtins / tokenize

[gh-105017](https://github.com/python/cpython/issues/105017): Surface CRLF lines within the tokenize string attribute across both `NL` and `NEWLINE` tokens. Marta Gómez prepared the patch.

[gh-104976](https://github.com/python/cpython/issues/104976): Make certain that trailing `DEDENT` `tokenize.TokenInfo` objects produced by the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module are reported just as they were under Python 3.11. Pablo Galindo authored this.

[gh-104972](https://github.com/python/cpython/issues/104972): Make certain the `line` attribute on `tokenize.TokenInfo` objects within the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module is always right. Pablo Galindo authored this.

[gh-104825](https://github.com/python/cpython/issues/104825): Tokens that the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module produces no longer carry an implicit `\n` character inside the `line` attribute. Pablo Galindo authored this.

[gh-105564](https://github.com/python/cpython/issues/105564): Keep artificil newlines out of the `line` attribute on tokens produced by the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module's APIs. Pablo Galindo authored this.

[gh-105390](https://github.com/python/cpython/issues/105390): Properly raise [`tokenize.TokenError`](https://docs.python.org/3.14/library/tokenize.html#tokenize.TokenError) exceptions in place of [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) for tokenize problems such as truncated input. Pablo Galindo authored this.

[gh-105259](https://github.com/python/cpython/issues/105259): Leave the newline character out of trailing `NEWLINE` tokens that the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module emits. Pablo Galindo authored this.

[gh-105324](https://github.com/python/cpython/issues/105324): Repair the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module's main function while it reads from `sys.stdin`. Pablo Galindo authored this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

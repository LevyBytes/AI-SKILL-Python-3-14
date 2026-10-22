# Python 3.14.4 final / core and builtins / compiler and parser

[gh-80667](https://github.com/python/cpython/issues/80667): Literals written with the `\N{name}` escape syntax are now able to build CJK ideographs along with Hangul syllables via case-insensitive names.

[gh-148157](https://github.com/python/cpython/issues/148157): Stop an improbable crash arising while parsing invalid type comments attached to function parameters. OSS Fuzz surfaced this in [#492782951](https://issues.oss-fuzz.com/issues/492782951).

[gh-145187](https://github.com/python/cpython/issues/145187): Resolves a compiler assertion failure occurring when a type parameter bound holds an invalid expression inside a conditional block.

[gh-145783](https://github.com/python/cpython/issues/145783): Corrects a rare crash inside the parser that struck when specific errors went erroneously unpropagated. OSS Fuzz surfaced it in [#491369109](https://issues.oss-fuzz.com/issues/491369109).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

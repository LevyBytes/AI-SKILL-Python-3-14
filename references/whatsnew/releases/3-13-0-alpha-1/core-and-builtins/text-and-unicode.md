# Python 3.13.0 alpha 1 / core and builtins / text and unicode

[gh-105194](https://github.com/python/cpython/issues/105194): Stop escaping f-string format specifiers with backslashes. Pablo Galindo authored this.

[gh-106931](https://github.com/python/cpython/issues/106931): String objects allocated statically are henceforth interned across the whole runtime rather than within each interpreter. That corrects a case in which one of these strings would be interned solely in a lone interpreter. Ordinary string objects see no change.

[gh-105699](https://github.com/python/cpython/issues/105699): A rare race while setting up per-interpreter interned strings no longer brings Python down. That crash used to show up at the moment the interpreter was being finalized.

[gh-109114](https://github.com/python/cpython/issues/109114): The detection of the error message for invalid lambdas within f-strings was relaxed so it stops scanning for arbitrary replacement fields, avoiding false positives. Pablo Galindo wrote the patch

[gh-104169](https://github.com/python/cpython/issues/104169): The tokenizer was divided across two distinct directories: - The first holds the genuine lexeme-producing logic and resides in `Parser/lexer`. - The second wraps that lexer for each of our tokenization modes (string, utf-8, file, interactive, readline) and resides in `Parser/tokenizer`.

[gh-110259](https://github.com/python/cpython/issues/110259): The format spec is now identified correctly inside f-strings (single- or triple-quoted) whose expression part spans several lines and carries a formatting spec. Pablo Galindo wrote the patch

[gh-105435](https://github.com/python/cpython/issues/105435): Eliminate a spurious newline character when a file finishes on a comment that lacks a newline. Pablo Galindo authored this.

[gh-33092](https://github.com/python/cpython/issues/33092): Streamline and accelerate the interpreter where f-strings are concerned. Drops the `FORMAT_VALUE` opcode. Brings in the `CONVERT_VALUE`, `FORMAT_SIMPLE` and `FORMAT_WITH_SPEC` opcode. The compiler now emits a tighter sequence for each format expression.

[gh-88943](https://github.com/python/cpython/issues/88943): The syntax error for a non-ASCII character following a numerical literal was improved. The error now points at the invalid non-ASCII character rather than at the valid numerical literal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

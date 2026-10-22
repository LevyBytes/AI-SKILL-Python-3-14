# tokenize — `tokenize` — Tokenizer for Python source

## tokenize — Tokenizer for Python source

### `tokenize` — Tokenizer for Python source

**Source code:** [Lib/tokenize.py](https://github.com/python/cpython/tree/3.14/Lib/tokenize.py)

---

A lexical scanner for Python source code, written in Python itself, is what the `tokenize` module delivers. Because the scanner in this module hands back comments as tokens too, it comes in handy for writing "pretty-printers", colorizers for on-screen displays included.

So that handling the token stream stays simple, every [operator](https://docs.python.org/3.14/reference/lexical_analysis.html#operators) and [delimiter](https://docs.python.org/3.14/reference/lexical_analysis.html#delimiters) token plus [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) comes back under the generic [`OP`](https://docs.python.org/3.14/library/token.html#token.OP) token type. You can pin down the exact type by inspecting the `exact_type` property on the [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) that `tokenize.tokenize()` returns.

Warning

Bear in mind that this module's functions are built solely to parse Python code that is syntactically valid (code that raises nothing when [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) processes it). When you hand them invalid Python code, the behavior of this module's functions is **undefined** and can change at any moment.

[Subject index](INDEX.md) · [Continue](tokenize-tokenize-to-tokenize-tokenerror.md)

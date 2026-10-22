# token: Tokenizer terminal, name, number and f-string constants

### `token` — Constants used with Python parse trees

**Source code:** [Lib/token.py](https://github.com/python/cpython/tree/3.14/Lib/token.py)

---

Constants standing for the numeric values of the parse tree's leaf nodes (terminal tokens) are what this module supplies. For the definitions of these names within the context of the language grammar, look at the file `Grammar/Tokens` in the Python distribution. Which exact numeric values the names map to can shift between Python versions.

The module further supplies a mapping from numeric codes to names plus a few functions. Those functions echo definitions found in the Python C header files.

Keep in mind that a token's value can hinge on tokenizer options. To illustrate, a `"+"` token might come back as either `PLUS` or `OP`, while a `"match"` token might be either `NAME` or `SOFT_KEYWORD`.

 token.tok_name

A dictionary mapping the numeric values of this module's constants back to name strings, which lets a more human-readable rendering of parse trees be produced.

 token.ISTERMINAL(*x*)

Return `True` for terminal token values.

 token.ISNONTERMINAL(*x*)

Return `True` for non-terminal token values.

 token.ISEOF(*x*)

Return `True` if *x* is the marker indicating the end of input.

The token constants are:

 token.NAME

Token value that indicates an [identifier or keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers).

 token.NUMBER

Token value that indicates a [numeric literal](https://docs.python.org/3.14/reference/lexical_analysis.html#numbers)

 token.STRING

A token value flagging a [string or byte literal](https://docs.python.org/3.14/reference/lexical_analysis.html#strings), but not [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings). The token string goes uninterpreted: the surrounding quotation marks and the prefix (where present) are included, and backslashes appear literally, with no escape sequence processing.

 token.OP

A generic token value that indicates an [operator](https://docs.python.org/3.14/reference/lexical_analysis.html#operators) or [delimiter](https://docs.python.org/3.14/reference/lexical_analysis.html#delimiters).

**CPython implementation detail:** Only the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module reports this value. Internally the tokenizer relies on exact token types instead.

 token.COMMENT

Token value used to indicate a comment. The parser ignores `COMMENT` tokens.

 token.NEWLINE

Token value that indicates the end of a [logical line](https://docs.python.org/3.14/reference/lexical_analysis.html#logical-lines).

 token.NL

A token value flagging a non-terminating newline. `NL` tokens get produced whenever a logical line of code spreads across several physical lines. The parser ignores `NL` tokens.

 token.INDENT

A token value placed at the start of a [logical line](https://docs.python.org/3.14/reference/lexical_analysis.html#logical-lines) to mark where an [indented block](https://docs.python.org/3.14/reference/lexical_analysis.html#indentation) begins.

 token.DEDENT

A token value placed at the start of a [logical line](https://docs.python.org/3.14/reference/lexical_analysis.html#logical-lines) to mark where an [indented block](https://docs.python.org/3.14/reference/lexical_analysis.html#indentation) ends.

 token.FSTRING_START

Token value used to indicate the beginning of an [f-string literal](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings).

**CPython implementation detail:** The token string carries the prefix and the opening quote(s), yet none of the literal's contents.

 token.FSTRING_MIDDLE

A token value covering literal text within an [f-string literal](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), format specifications included.

**CPython implementation detail:** The replacement fields (in other words, the non-literal parts of f-strings) draw on the same tokens as other expressions and are bounded by `LBRACE`, `RBRACE`, `EXCLAMATION` and `COLON` tokens.

[Subject index](INDEX.md) · [Previous](constants-used-with-python-parse-trees.md) · [Continue](token-fstring-end-to-token-soft-keyword.md)

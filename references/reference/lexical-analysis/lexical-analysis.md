# 2. Lexical analysis

### 2. Lexical analysis

A *parser* consumes a Python program. What feeds that parser is a stream of [tokens](https://docs.python.org/3.14/glossary.html#term-token) emitted by the *lexical analyzer* (also called the *tokenizer*). This chapter covers how those tokens get produced by the lexical analyzer.

First, the lexical analyzer works out the encoding of the program text (UTF-8 unless stated otherwise) and decodes that text into source characters. A [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) is raised whenever decoding fails.

The analyzer then turns those source characters into a stream of tokens. Which type a token receives usually hinges on the next source character awaiting processing. Likewise, the analyzer's other special behaviors depend on the first source character it has not yet consumed. A brief summary of these source characters appears in the table below, along with links into sections holding further detail.

| Character | Next token (or other relevant documentation) |
| --- | --- |
| - space - tab - formfeed | - Whitespace |
| - CR, LF | - New line - Indentation |
| - backslash (`\`) | - Explicit line joining - (Also significant in string escape sequences) |
| - hash (`#`) | - Comment |
| - quote (`'`, `"`) | - String literal |
| - ASCII letter (`a`-`z`, `A`-`Z`) - non-ASCII character | - Name - Prefixed string or bytes literal |
| - underscore (`_`) | - Name - (Can also be part of numeric literals) |
| - number (`0`-`9`) | - Numeric literal |
| - dot (`.`) | - Numeric literal - Operator |
| - question mark (`?`) - dollar (`$`) - backquote (`​`​`) - control character | - Error (outside string literals and comments) |
| - other printing character | - Operator or delimiter |
| - end of file | - End marker |

[Subject index](INDEX.md) · [Following source section](line-structure.md)

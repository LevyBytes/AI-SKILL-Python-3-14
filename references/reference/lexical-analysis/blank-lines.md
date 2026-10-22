# 2.1.7. Blank lines

### 2.1.7. Blank lines

When a logical line holds nothing but spaces, tabs, formfeeds and perhaps a comment, it gets discarded (meaning no [`NEWLINE`](https://docs.python.org/3.14/library/token.html#token.NEWLINE) token is produced). While statements are entered interactively, a blank line might be treated differently depending on how the read-eval-print loop is built. Within the standard interactive interpreter, a fully blank logical line (one carrying not so much as whitespace or a comment) ends a multi-line statement.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](implicit-line-joining.md) · [Following source section](indentation.md)

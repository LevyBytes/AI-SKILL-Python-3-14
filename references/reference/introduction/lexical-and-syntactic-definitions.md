# 1.2.1. Lexical and Syntactic definitions

### 1.2.1. Lexical and Syntactic definitions

A degree of distinction separates *lexical* work from *syntactic* work: the [lexical analyzer](https://docs.python.org/3.14/glossary.html#term-lexical-analyzer) works over the source's separate characters one at a time, whereas the *parser* (the syntactic analyzer) consumes the run of [tokens](https://docs.python.org/3.14/glossary.html#term-token) that the lexical pass has produced. Even so, where exactly the line between these two stages falls can, in certain situations, come down to a CPython implementation detail.

In everyday terms, the gap comes to this: within *lexical* definitions every bit of whitespace carries weight. The lexical analyzer simply [discards](https://docs.python.org/3.14/reference/lexical_analysis.html#whitespace) any whitespace not turned into tokens such as [`token.INDENT`](https://docs.python.org/3.14/library/token.html#token.INDENT) or [`NEWLINE`](https://docs.python.org/3.14/library/token.html#token.NEWLINE). From there, *syntactic* definitions build on those tokens instead of the raw source characters.

Throughout these docs one and the same BNF grammar serves both definition styles. Every appearance of BNF in the chapter that follows ([Lexical analysis](https://docs.python.org/3.14/reference/lexical_analysis.html#lexical)) counts as a lexical definition, while appearances in later chapters count as syntactic ones.

[Subject index](INDEX.md) · [Owning language section](introduction.md) · [Owning language section](notation.md) · [Previous source section](notation.md)

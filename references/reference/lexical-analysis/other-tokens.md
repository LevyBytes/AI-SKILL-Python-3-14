# 2.2. Other tokens

### 2.2. Other tokens

Aside from [`NEWLINE`](https://docs.python.org/3.14/library/token.html#token.NEWLINE), [`INDENT`](https://docs.python.org/3.14/library/token.html#token.INDENT) and [`DEDENT`](https://docs.python.org/3.14/library/token.html#token.DEDENT), these token categories exist: *identifiers* and *keywords* ([`NAME`](https://docs.python.org/3.14/library/token.html#token.NAME)), *literals* (for instance [`NUMBER`](https://docs.python.org/3.14/library/token.html#token.NUMBER) and [`STRING`](https://docs.python.org/3.14/library/token.html#token.STRING)), plus other symbols (*operators* and *delimiters*, [`OP`](https://docs.python.org/3.14/library/token.html#token.OP)). Whitespace characters (those other than the logical line terminators covered earlier) are not themselves tokens but mark off tokens. When ambiguity arises, a token is the longest string forming a legal token as it is read from left to right.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Previous source section](end-marker.md) · [Following source section](names.md)

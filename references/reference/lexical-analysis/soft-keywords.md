# 2.3.2. Soft Keywords

### 2.3.2. Soft Keywords

Added in version 3.10.

A handful of names hold reserved status only within particular contexts. These go by the name *soft keywords*:

- `match`, `case`, and `_`, when used in the [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) statement.

- `type`, when used in the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement.

In their particular contexts these behave syntactically like keywords, but the parser draws that line, not the tokenizer.

Because they are soft keywords, the grammar can employ them while still keeping compatibility with existing code that uses these names as identifier names.

Changed in version 3.12: `type` is now a soft keyword.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](names.md) · [Previous source section](keywords.md) · [Following source section](reserved-classes-of-identifiers.md)

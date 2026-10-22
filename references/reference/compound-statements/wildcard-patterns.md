# 8.6.4.5. Wildcard Patterns

#### 8.6.4.5. Wildcard Patterns

A wildcard pattern matches anything (it always passes) and binds nothing. Syntax:

```text

wildcard_pattern: '_'
```

Within any pattern `_` behaves as a [soft keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords), though only there. Everywhere else it remains an ordinary identifier, including inside `match` subject expressions, `guard`s, and `case` blocks.

Put simply, `_` always passes.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](capture-patterns.md) · [Following source section](value-patterns.md)

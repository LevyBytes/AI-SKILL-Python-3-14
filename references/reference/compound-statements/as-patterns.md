# 8.6.4.2. AS Patterns

#### 8.6.4.2. AS Patterns

To the left of the `as` keyword, an AS pattern matches an OR pattern against the subject. Syntax:

```text

as_pattern: or_pattern "as" capture_pattern
```

When the OR pattern fails, the AS pattern fails as well. Otherwise it binds the subject to the name appearing to the right of the as keyword and reports success. `capture_pattern` cannot be a `_`.

Put simply, `P as NAME` matches against `P`, and when that works it assigns `NAME = <subject>`.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](or-patterns.md) · [Following source section](literal-patterns.md)

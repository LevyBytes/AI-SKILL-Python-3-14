# 8.6.4.4. Capture Patterns

#### 8.6.4.4. Capture Patterns

The subject value is bound to a name by a capture pattern. Syntax:

```text

capture_pattern: !'_' NAME
```

A lone underscore `_` does not count as a capture pattern (which is exactly what `!'_'` conveys). Instead it is handled as a `wildcard_pattern`.

Inside one pattern, any single name may be bound only a single time. E.g. `case x, x: ...` is invalid while `case [x] | x: ...` is allowed.

A capture pattern never fails. Its binding obeys the scoping rules that the assignment expression operator set out in [**PEP 572**](https://peps.python.org/pep-0572/); the name turns into a local variable within the nearest enclosing function scope, barring an applicable [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) or [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement.

Put simply, `NAME` always passes and it assigns `NAME = <subject>`.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](literal-patterns.md) · [Following source section](wildcard-patterns.md)

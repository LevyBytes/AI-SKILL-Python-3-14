# 8.6.4.6. Value Patterns

#### 8.6.4.6. Value Patterns

A named value in Python is represented by a value pattern. Syntax:

```text

value_pattern: attr
attr:          name_or_attr "." NAME
name_or_attr:  attr | NAME
```

Resolution of the pattern's dotted name follows the usual Python [name resolution rules](https://docs.python.org/3.14/reference/executionmodel.html#resolve-names). Should the located value compare equal to the subject value (via the `==` equality operator), the pattern passes.

Put simply, `NAME1.NAME2` passes only when `<subject> == NAME1.NAME2`

Note

When one value appears more than once within a single match statement, the interpreter is free to remember the first value it looked up and reuse it instead of performing the lookup again. Such a cache is bound strictly to one particular run of one particular match statement.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](wildcard-patterns.md) · [Following source section](group-patterns.md)

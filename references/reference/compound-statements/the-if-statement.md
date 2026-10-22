# 8.1. The `if` statement

### 8.1. The `if` statement

Conditional execution is handled by the `if` statement:

```text

if_stmt: "if" assignment_expression ":" suite
         ("elif" assignment_expression ":" suite)*
         ["else" ":" suite]
```

It picks precisely one of the suites by working through the expressions in sequence until it reaches one that is true (consult the section [Boolean operations](https://docs.python.org/3.14/reference/expressions.html#booleans) for what counts as true and false); that suite then runs (and nothing else in the `if` statement runs or is evaluated). Should every expression turn out false, then the suite belonging to the `else` clause runs, provided one exists.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](compound-statements.md) · [Following source section](the-while-statement.md)

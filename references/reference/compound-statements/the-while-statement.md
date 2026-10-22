# 8.2. The `while` statement

### 8.2. The `while` statement

Repeated execution that continues for as long as an expression stays true is carried out by the `while` statement:

```text

while_stmt: "while" assignment_expression ":" suite
            ["else" ":" suite]
```

It checks the expression over and over, running the first suite whenever it is true; once the expression is false (which can happen on the very first check) the suite of the `else` clause runs, if one is present, and the loop ends.

Running a [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) statement within the first suite ends the loop and skips the `else` clause’s suite entirely. Running a [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement within the first suite drops the remainder of the suite and returns to checking the expression.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](the-if-statement.md) · [Following source section](the-for-statement.md)

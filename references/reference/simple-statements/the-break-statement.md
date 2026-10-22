# 7.9. The `break` statement

### 7.9. The `break` statement

```text

break_stmt: "break"
```

Syntactically, `break` is permitted only when nested inside a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) loop, yet never when nested inside a function or class definition that itself sits within that loop.

What it does is end the closest surrounding loop, bypassing the optional `else` clause should that loop carry one.

Where `break` ends a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop, whatever value the loop control target currently holds is retained.

Should `break` hand control out of a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement that has a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause, that `finally` clause runs before the loop is genuinely exited.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](raise-and-implicit-exception-chaining.md) · [Following source section](the-continue-statement.md)

# 7.10. The `continue` statement

### 7.10. The `continue` statement

```text

continue_stmt: "continue"
```

Syntactically, `continue` is permitted only when nested inside a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) loop, yet never when nested inside a function or class definition that itself sits within that loop. It proceeds on to the next iteration of the closest surrounding loop.

Should `continue` hand control out of a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement that has a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause, that `finally` clause runs before the next loop iteration genuinely begins.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-break-statement.md) · [Following source section](the-import-statement.md)

# 7.6. The `return` statement

### 7.6. The `return` statement

```text

return_stmt: "return" [expression_list]
```

`return` is permitted syntactically only when nested within a function definition, and not within a nested class definition.

When an expression list is supplied, it is evaluated; otherwise `None` takes its place.

`return` exits the current function call, carrying the expression list (or `None`) out as the return value.

Whenever `return` hands control out of a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement that has a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause, that `finally` clause runs before the function is genuinely left.

Inside a generator function, the `return` statement signals that the generator has finished and triggers [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) being raised. Any returned value serves as an argument for constructing `StopIteration` and becomes its [`StopIteration.value`](https://docs.python.org/3.14/library/exceptions.html#StopIteration.value) attribute.

Inside an asynchronous generator function, a bare `return` statement signals that the asynchronous generator has finished and triggers [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) being raised. A `return` statement carrying a value is a syntax error within an asynchronous generator function.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-del-statement.md) · [Following source section](the-yield-statement.md)

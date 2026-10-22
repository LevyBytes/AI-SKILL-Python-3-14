# Why don’t generators support the with statement?

### Why don’t generators support the with statement?

Owing to technical considerations, handing a generator straight to a context manager would misbehave. In the usual scenario, where a generator serves as an iterator driven to exhaustion, there is nothing to close. Should closing be required, though, wrap the generator with [`contextlib.closing(generator)`](https://docs.python.org/3.14/library/contextlib.html#contextlib.closing) inside the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[Subject index](INDEX.md)

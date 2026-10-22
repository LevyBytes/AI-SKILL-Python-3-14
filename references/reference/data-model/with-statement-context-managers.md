# 3.3.9. With Statement Context Managers

### 3.3.9. With Statement Context Managers

A *context manager* is an object establishing the runtime context that should be set up while a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement runs. The context manager governs both entry into and exit from the intended runtime context for running the code block. Context managers are typically engaged through the `with` statement (covered in section [The with statement](https://docs.python.org/3.14/reference/compound_stmts.html#with)), yet they can also be used by calling their methods directly.

Common applications of context managers involve saving and restoring assorted kinds of global state, locking and unlocking resources, closing opened files, and similar tasks.

For further details on context managers, see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager). The [`object`](https://docs.python.org/3.14/library/functions.html#object) class on its own does not furnish the context manager methods.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](object-round-object-trunc-object-floor-object-ceil.md) · [Following source section](object-enter.md)

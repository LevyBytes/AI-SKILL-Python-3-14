# contextlib — Catching exceptions from `__enter__` methods

### Catching exceptions from `__enter__` methods

Now and then you want to trap exceptions thrown by an [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method's body *without* accidentally trapping ones from the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement body or from the context manager's [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method. Leaning on `ExitStack`, you can pull the context management protocol's stages slightly apart so this becomes feasible:

```python
stack = ExitStack()
try:
    x = stack.enter_context(cm)
except Exception:
    # handle __enter__ exception
else:
    with stack:
        # Handle normal case

```

If you genuinely find yourself reaching for this, it usually hints that the API beneath ought to expose a plain resource-management interface suited to [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)/[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except)/[`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) statements, though not every API is built that thoughtfully. Where a context manager is the sole resource-management entry point on offer, `ExitStack` smooths over a range of cases that a bare [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement cannot tackle on its own.

[Subject index](INDEX.md) · [Previous](supporting-a-variable-number-of-context-managers.md) · [Continue](cleaning-up-in-an-enter-implementation.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)

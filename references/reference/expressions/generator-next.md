# generator.__next__()

generator.__next__()

Begins running a generator function, or picks up again at the yield expression that ran most recently. Whenever a generator function resumes through a `__next__()` method, the active yield expression evaluates to [`None`](https://docs.python.org/3.14/library/constants.html#None). Running then proceeds onward to the following yield expression, at which point the generator pauses once more, and the `yield_list` value goes back to the caller of `__next__()`. Should the generator finish without producing a further value, it raises a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception.

Typically this method gets invoked behind the scenes, for instance through a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop or via the built-in [`next()`](https://docs.python.org/3.14/library/functions.html#next) function.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Owning language section](generator-iterator-methods.md) · [Previous source section](generator-iterator-methods.md) · [Following source section](generator-send.md)

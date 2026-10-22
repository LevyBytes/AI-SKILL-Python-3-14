# inspect: `inspect.getgeneratorlocals()`, `inspect.getcoroutinelocals()`, `inspect.getasyncgenlocals()`

inspect.getgeneratorlocals(*generator*)

Obtain the mapping that ties the live local variables inside *generator* to whatever they currently hold. You get back a dictionary keyed by variable name and valued by the corresponding value. It amounts to invoking [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) within the generator’s body, carrying over every one of the same caveats.

Should *generator* be a [generator](https://docs.python.org/3.14/glossary.html#term-generator) that currently has no frame attached, the result is an empty dictionary. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised when *generator* is not a Python generator object.

**CPython implementation detail:** This routine counts on the generator surfacing a Python stack frame to be introspected, which not every Python implementation is bound to do. Where that holds, the function invariably gives back an empty dictionary.

Added in version 3.3.

 inspect.getcoroutinelocals(*coroutine*)

This routine parallels `getgeneratorlocals()`, except it operates on coroutine objects produced by [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions.

Added in version 3.5.

 inspect.getasyncgenlocals(*agen*)

This routine parallels `getgeneratorlocals()`, except it operates on asynchronous generator objects produced by [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions that employ the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](inspect-getgeneratorstate-to-inspect-getasyncgenstate.md) · [Continue](inspect-co-optimized-to-inspect-co-method.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Current State of Generators, Coroutines, and Asynchronous Generators](inspect-getgeneratorstate-to-inspect-getasyncgenstate.md)

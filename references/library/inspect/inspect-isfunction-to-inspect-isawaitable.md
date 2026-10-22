# inspect: `inspect.isfunction()`, `inspect.ispackage()`, `inspect.isgeneratorfunction()`, `inspect.isgenerator()`, `inspect.iscoroutinefunction()`, `inspect.markcoroutinefunction()`, `inspect.iscoroutine()`, `inspect.isawaitable()`

inspect.isfunction(*object*)

Return `True` if the object is a Python function, a category that takes in functions built by a [lambda](https://docs.python.org/3.14/glossary.html#term-lambda) expression.

Consult the note attached to `ismethod()` for a worked example.

 inspect.ispackage(*object*)

Return `True` if the object is a [package](https://docs.python.org/3.14/glossary.html#term-package).

Added in version 3.14.

 inspect.isgeneratorfunction(*object*)

Return `True` if the object is a Python generator function.

It likewise yields `True` for bound methods derived from Python generator functions (consult [Methods](https://docs.python.org/3.14/library/stdtypes.html#typesmethods) for further detail).

Changed in version 3.8: A [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) wrapper now yields `True` whenever its wrapped target is a Python generator function.

Changed in version 3.13: A [`functools.partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod) wrapper now yields `True` whenever its wrapped target is a Python generator function.

 inspect.isgenerator(*object*)

Return `True` if the object is a generator.

 inspect.iscoroutinefunction(*object*)

Return `True` for a [coroutine function](https://docs.python.org/3.14/glossary.html#term-coroutine-function) (something declared via the [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) syntax), for a [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) that wraps such a coroutine function, or for a sync function tagged with `markcoroutinefunction()`.

Added in version 3.5.

Changed in version 3.8: A [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) wrapper now yields `True` whenever its wrapped target is a [coroutine function](https://docs.python.org/3.14/glossary.html#term-coroutine-function).

Changed in version 3.12: Sync functions marked with `markcoroutinefunction()` now return `True`.

Changed in version 3.13: A [`functools.partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod) wrapper now yields `True` whenever its wrapped target is a [coroutine function](https://docs.python.org/3.14/glossary.html#term-coroutine-function).

 inspect.markcoroutinefunction(*func*)

A decorator that flags a callable as a [coroutine function](https://docs.python.org/3.14/glossary.html#term-coroutine-function) in cases where `iscoroutinefunction()` would otherwise fail to recognize it.

This can come in handy for sync functions that hand back a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine), whenever the function is handed to an API that expects `iscoroutinefunction()`.

Where you can, reach for an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function instead. Another workable route is to invoke the function and check its return value with `iscoroutine()`.

Added in version 3.12.

 inspect.iscoroutine(*object*)

Return `True` if the object is a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) created by an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function.

Added in version 3.5.

 inspect.isawaitable(*object*)

Return `True` if the object can be used in [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression.

It also serves to tell generator-based coroutines apart from ordinary generators:

```python
import types

def gen():
    yield
@types.coroutine
def gen_coro():
    yield

assert not isawaitable(gen())
assert isawaitable(gen_coro())

```

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](inspect-getmembers-to-inspect-ismethod.md) · [Continue](inspect-isasyncgenfunction-to-inspect-isgetsetdescriptor.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Types and members](types-and-members-section-introduction-and-initial-examples.md)

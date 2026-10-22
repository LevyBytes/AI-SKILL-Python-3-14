# collections.abc: `collections.abc.Awaitable`

*class *collections.abc.Awaitable

ABC for [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) objects, the kind usable within [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expressions. A custom implementation has to supply the [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method.

[Coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) objects together with instances of the `Coroutine` ABC count as instances of this ABC.

Note

Within CPython, generator-based coroutines ([generators](https://docs.python.org/3.14/glossary.html#term-generator) decorated with [`@types.coroutine`](https://docs.python.org/3.14/library/types.html#types.coroutine)) qualify as *awaitables*, despite lacking an [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method. Running `isinstance(gencoro, Awaitable)` against them yields `False`. Reach for [`inspect.isawaitable()`](https://docs.python.org/3.14/library/inspect.html#inspect.isawaitable) to spot them.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](mapping-view-interfaces.md) · [Continue](collections-abc-coroutine-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: Collections Abstract Base Classes ??? Detailed Descriptions](collections-abc-container-class.md)

# collections.abc: `collections.abc.Coroutine`

*class *collections.abc.Coroutine

ABC for classes compatible with the [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) protocol. They provide the methods listed below, which [Coroutine Objects](https://docs.python.org/3.14/reference/datamodel.html#coroutine-objects) defines: [`send()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.send), [`throw()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.throw), and [`close()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.close). A custom implementation is additionally required to implement [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__). Every `Coroutine` instance ranks as an instance of `Awaitable` too.

Note

Within CPython, generator-based coroutines ([generators](https://docs.python.org/3.14/glossary.html#term-generator) decorated with [`@types.coroutine`](https://docs.python.org/3.14/library/types.html#types.coroutine)) qualify as *awaitables*, despite lacking an [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method. Running `isinstance(gencoro, Coroutine)` against them yields `False`. Reach for [`inspect.isawaitable()`](https://docs.python.org/3.14/library/inspect.html#inspect.isawaitable) to spot them.

Consult [Annotating generators and coroutines](https://docs.python.org/3.14/library/typing.html#annotating-generators-and-coroutines) regarding how `Coroutine` is applied within type annotations. Its type parameters match `Generator` in both variance and ordering.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](collections-abc-awaitable-class.md) · [Continue](collections-abc-asynciterable-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: Collections Abstract Base Classes ??? Detailed Descriptions](collections-abc-container-class.md)

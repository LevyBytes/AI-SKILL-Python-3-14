# types — Coroutine Utility Functions

### Coroutine Utility Functions

 types.coroutine(*gen_func*)

This function converts a [generator](https://docs.python.org/3.14/glossary.html#term-generator) function into a [coroutine function](https://docs.python.org/3.14/glossary.html#term-coroutine-function) that returns a generator-based coroutine. That generator-based coroutine remains a [generator iterator](https://docs.python.org/3.14/glossary.html#term-generator-iterator), yet it also counts as a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) object and is [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable). That said, it need not necessarily provide the [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method.

When *gen_func* is a generator function, it gets modified in-place.

When *gen_func* is not a generator function, it gets wrapped. Should it return an instance of [`collections.abc.Generator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator), that instance is wrapped within an *awaitable* proxy object. Objects of every other type come back unchanged.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](types-simplenamespace-class-to-types-dynamicclassattribute.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md)

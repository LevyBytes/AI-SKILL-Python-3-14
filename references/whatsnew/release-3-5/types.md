# What’s New In Python 3.5 / types — collections.abc, types

### types

To turn [generator](https://docs.python.org/3.14/glossary.html#term-generator-iterator) and [`generator-like`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator) objects into [awaitables](https://docs.python.org/3.14/glossary.html#term-awaitable), there is a new [`coroutine()`](https://docs.python.org/3.14/library/types.html#types.coroutine) function. Yury Selivanov contributed this (see [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017)).

For the [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) objects that [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions create, there is a new type named [`CoroutineType`](https://docs.python.org/3.14/library/types.html#types.CoroutineType). Yury Selivanov landed this (see [bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400)).

[Subject index](INDEX.md) · [Previous source section](traceback.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)

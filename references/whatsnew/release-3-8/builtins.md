# What’s New In Python 3.8 / builtins

> (Contributed by twisteroid ambassador in [bpo-33530](https://bugs.python.org/issue?@action=redirect&bpo=33530).)

### builtins

The [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in gained the ability to take the `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` flag. When you pass that fresh flag, `compile()` permits top-level `await`, `async for` and `async with` forms that would ordinarily count as invalid syntax. The asynchronous code object it yields may then bear the `CO_COROUTINE` flag.

[Subject index](INDEX.md) · [Previous source section](asyncio.md) · [Next source section](collections.md) · [Release/subject declaration](assignment-expressions.md)

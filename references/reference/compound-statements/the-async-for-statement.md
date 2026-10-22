# 8.9.2. The `async for` statement

### 8.9.2. The `async for` statement

```text

async_for_stmt: "async" for_stmt
```

An [asynchronous iterable](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterable) supplies an `__aiter__` method that directly hands back an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator), whose `__anext__` method is able to invoke asynchronous code.

The `async for` statement makes iterating over asynchronous iterables straightforward.

The following code:

```python
async for TARGET in ITER:
    SUITE
else:
    SUITE2

```

Is semantically equivalent to:

```python
iter = (ITER).__aiter__()
running = True

while running:
    try:
        TARGET = await iter.__anext__()
    except StopAsyncIteration:
        running = False
    else:
        SUITE
else:
    SUITE2

```

save that implicit [special method lookup](https://docs.python.org/3.14/reference/datamodel.html#special-lookup) applies for [`__aiter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aiter__) and [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__).

Using an `async for` statement outside the body of a coroutine function raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](coroutine-function-definition.md) · [Following source section](the-async-with-statement.md)

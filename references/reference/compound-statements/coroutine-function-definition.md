# 8.9.1. Coroutine function definition

<a id="89-coroutines"></a>

8.9. Coroutines: Added in version 3.5.

### 8.9.1. Coroutine function definition

```text

async_funcdef: [decorators] "async" "def" funcname "(" [parameter_list] ")"
               ["->" expression] ":" suite
```

Python coroutines can have their execution paused and later picked up at numerous points (see [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine)). [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expressions, along with `async for` and `async with`, are usable only within the body of a coroutine function.

A function written with `async def` syntax is always a coroutine function, regardless of whether it contains any `await` or `async` keywords.

Putting a `yield from` expression inside the body of a coroutine function raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

An example of a coroutine function:

```python
async def func(param1, param2):
    do_stuff()
    await some_coroutine()

```

Changed in version 3.7: `await` and `async` have become keywords; before this they counted as keywords solely within the body of a coroutine function.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Following source section](the-async-for-statement.md)

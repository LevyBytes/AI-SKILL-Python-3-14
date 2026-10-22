# 8.9.3. The `async with` statement

### 8.9.3. The `async with` statement

```text

async_with_stmt: "async" with_stmt
```

An [asynchronous context manager](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager) is a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) capable of suspending execution within its *enter* and *exit* methods.

The following code:

```python
async with EXPRESSION as TARGET:
    SUITE

```

is semantically equivalent to:

```python
manager = (EXPRESSION)
aenter = manager.__aenter__
aexit = manager.__aexit__
value = await aenter()
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not await aexit(*sys.exc_info()):
        raise
finally:
    if not hit_except:
        await aexit(None, None, None)

```

save that implicit [special method lookup](https://docs.python.org/3.14/reference/datamodel.html#special-lookup) applies for [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) and [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__).

Using an `async with` statement outside the body of a coroutine function raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

See also

[**PEP 492**](https://peps.python.org/pep-0492/) - Coroutines with async and await syntax

The proposal that turned coroutines into a first-class concept in Python and supplied the syntax to support them.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](coroutine-function-definition.md) · [Previous source section](the-async-for-statement.md) · [Following source section](type-parameter-lists.md)

# typing — Annotating generators and coroutines

### Annotating generators and coroutines

To annotate a generator, use the generic [`Generator[YieldType, SendType, ReturnType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator). For instance:

```python
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

```

Keep in mind that, in contrast to numerous other generic classes across the standard library, the `SendType` of [`Generator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator) is contravariant rather than covariant or invariant.

`None` serves as the default for both the `SendType` and `ReturnType` parameters:

```python
def infinite_stream(start: int) -> Generator[int]:
    while True:
        yield start
        start += 1

```

You can likewise spell these types out in full:

```python
def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1

```

A plain generator that does nothing but yield values may instead be annotated with a return type of [`Iterable[YieldType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable) or [`Iterator[YieldType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterator):

```python
def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1

```

The async counterpart works much the same way, except no `ReturnType` argument is expected ([`AsyncGenerator[YieldType, SendType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncGenerator)). Because the `SendType` argument falls back to `None`, the two definitions that follow mean the same thing:

```python
async def infinite_stream(start: int) -> AsyncGenerator[int]:
    while True:
        yield start
        start = await increment(start)

async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
    while True:
        yield start
        start = await increment(start)

```

Mirroring the synchronous version, [`AsyncIterable[YieldType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncIterable) and [`AsyncIterator[YieldType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncIterator) can be used too:

```python
async def infinite_stream(start: int) -> AsyncIterator[int]:
    while True:
        yield start
        start = await increment(start)

```

For coroutines, annotate with [`Coroutine[YieldType, SendType, ReturnType]`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Coroutine). Its generic arguments line up with those of [`Generator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Generator); for instance:

```python
from collections.abc import Coroutine
c: Coroutine[list[str], str, int]  # Some coroutine defined elsewhere
x = c.send('hi')                   # Inferred type of 'x' is list[str]
async def bar() -> None:
    y = await c                    # Inferred type of 'y' is int

```

[Subject index](INDEX.md) · [Previous](the-type-of-class-objects.md) · [Continue](user-defined-generics-overview.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)

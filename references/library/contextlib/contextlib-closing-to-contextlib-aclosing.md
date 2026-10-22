# contextlib: `contextlib.closing()`, `contextlib.aclosing()`

contextlib.closing(*thing*)

Hands back a context manager that closes *thing* once the block finishes. In essence, it amounts to:

```python
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

```

This permits you to write something along these lines:

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

```

with no need to close `page` by hand. `page.close()` runs once the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block ends, even should an error arise.

Note

The bulk of resource-handling types honor the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol, which closes *thing* once you depart the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Consequently, `closing()` earns its keep mainly with third party types lacking context manager support. The snippet here exists solely to demonstrate, since [`urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen) would ordinarily appear inside a context manager.

 contextlib.aclosing(*thing*)

Hands back an async context manager that invokes the `aclose()` method belonging to *thing* once the block finishes. In essence, it amounts to:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def aclosing(thing):
    try:
        yield thing
    finally:
        await thing.aclose()

```

Notably, `aclosing()` enables predictable teardown of async generators in cases where they bow out prematurely through [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) or an exception. To illustrate:

```python
from contextlib import aclosing

async with aclosing(my_generator()) as values:
    async for value in values:
        if value == 42:
            break

```

Following this approach guarantees that the generator's async exit logic runs in the very context where it iterated (so that exceptions and context variables behave correctly, and the exit logic doesn't fire once some task it relies on has already ended).

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](connection-resource-and-timing-utilities.md) · [Continue](contextlib-nullcontext.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)

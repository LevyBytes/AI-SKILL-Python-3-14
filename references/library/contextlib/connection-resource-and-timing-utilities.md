# contextlib: `contextlib.asynccontextmanager`

@contextlib.asynccontextmanager

Comparable to `contextmanager()`, except it yields an [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers).

Acting as a [decorator](https://docs.python.org/3.14/glossary.html#term-decorator), this function lets you declare a factory that produces [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement asynchronous context managers, sparing you from writing a class or from authoring distinct [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) and [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) methods. You have to attach it to an [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function.

A brief illustration:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection(conn)

async def get_all_users():
    async with get_connection() as conn:
        return conn.query('SELECT ...')

```

Added in version 3.7.

Whatever context managers you build with `asynccontextmanager()` work either as decorators or alongside [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statements:

```python
import time
from contextlib import asynccontextmanager

@asynccontextmanager
async def timeit():
    now = time.monotonic()
    try:
        yield
    finally:
        print(f'it took {time.monotonic() - now}s to run')

@timeit()
async def main():
    # ... async code ...

```

When pressed into service as a decorator, each invocation of the function silently produces a brand-new generator instance. That mechanism is how the otherwise "one-shot" context managers from `asynccontextmanager()` satisfy the rule that decorators require context managers usable across multiple invocations.

Changed in version 3.10: decorator use became available for async context managers built through `asynccontextmanager()`.

[Subject index](INDEX.md) · [Previous](utilities-managed-resource.md) · [Continue](contextlib-closing-to-contextlib-aclosing.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)

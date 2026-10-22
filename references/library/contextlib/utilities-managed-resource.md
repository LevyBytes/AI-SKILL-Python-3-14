# contextlib: `contextlib.contextmanager`

@contextlib.contextmanager

Acting as a [decorator](https://docs.python.org/3.14/glossary.html#term-decorator), this function lets you declare a factory that produces [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement context managers, sparing you from writing a class or from authoring distinct [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods.

Plenty of objects already work directly inside with statements, yet occasionally you must govern a resource that isn't itself a context manager and that lacks a `close()` method compatible with `contextlib.closing`.

To guarantee proper handling of a resource, here is an abstract sketch:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

```

Once defined, you call the function as shown:

```python
>>> with managed_resource(timeout=3600) as resource:
...     # Resource is released at the end of this block,
...     # even if code in the block raises an exception

```

Whatever function carries the decorator has to hand back a [generator](https://docs.python.org/3.14/glossary.html#term-generator)-iterator when invoked. Precisely one value must be yielded by that iterator, and it gets bound to whatever targets sit in the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement's `as` clause, should one exist.

Once the generator reaches its yield, control passes to the body nested inside the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. After that body finishes, the generator picks up again. Should the body raise an exception that goes unhandled, it gets re-raised within the generator right where the yield sat. That means a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) — [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) — [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) statement lets you intercept the error (when one arises) or arrange for cleanup to happen. When an exception is caught only so it can be logged or trigger some action (instead of being fully swallowed), the generator is obligated to re-raise it. Failing that, the generator context manager will report to the `with` statement that the exception got dealt with, and the flow will carry on at whatever statement immediately follows the `with` statement.

Because `contextmanager()` builds on `ContextDecorator`, the context managers it yields double as decorators in addition to working inside [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements. Acting as a decorator, every call to the function quietly spins up a fresh generator instance (which is how the otherwise "one-shot" context managers from `contextmanager()` satisfy the rule that decorators demand context managers usable across multiple invocations).

Changed in version 3.2: Use of `ContextDecorator`.

[Subject index](INDEX.md) · [Previous](contextlib-abstractasynccontextmanager-class.md) · [Continue](connection-resource-and-timing-utilities.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)

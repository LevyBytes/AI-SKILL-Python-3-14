# contextlib — Single use, reusable and reentrant context managers

### Single use, reusable and reentrant context managers

The majority of context managers are coded such that a single [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement is all they reliably support. You have to construct these single use context managers anew on every use - reaching for the same one twice either raises an exception or otherwise misbehaves.

Owing to this widespread constraint, the usual advice is to build context managers right inside the header of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement that consumes them, exactly as every example above does.

Files illustrate the single use kind well: that opening [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement shuts the file, after which no more IO can run through that file object.

Anything `contextmanager()` produces likewise falls into the single use category, and trying it a second time draws a complaint that the backing generator did not yield:

```python
>>> from contextlib import contextmanager
>>> @contextmanager
... def singleuse():
...     print("Before")
...     yield
...     print("After")
...
>>> cm = singleuse()
>>> with cm:
...     pass
...
Before
After
>>> with cm:
...     pass
...
Traceback (most recent call last):
    ...
RuntimeError: generator didn't yield

```

[Subject index](INDEX.md) · [Previous](using-a-context-manager-as-a-function-decorator.md) · [Continue](reentrant-context-managers.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)

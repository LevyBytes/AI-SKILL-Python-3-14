# contextlib: `contextlib.ContextDecorator`

*class *contextlib.ContextDecorator

A base class allowing a context manager to serve as a decorator too.

Any context manager deriving from `ContextDecorator` still has to provide [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) in the usual way. Even in decorator form, `__exit__` keeps its optional exception handling.

Since `contextmanager()` relies on `ContextDecorator`, you receive this capability without doing anything extra.

An example of `ContextDecorator`:

```python
from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

```

Afterward, the class can be applied like so:

```python
>>> @mycontext()
... def function():
...     print('The bit in the middle')
...
>>> function()
Starting
The bit in the middle
Finishing

>>> with mycontext():
...     print('The bit in the middle')
...
Starting
The bit in the middle
Finishing

```

This amounts to nothing more than syntactic sugar over any construct shaped like:

```python
def f():
    with cm():
        # Do stuff

```

With `ContextDecorator` you may write it as:

```python
@cm()
def f():
    # Do stuff

```

It signals plainly that `cm` governs the entire function rather than only a fragment of it (and shedding an indentation level is a pleasant bonus).

You can broaden an existing context manager that already has a base class by folding in `ContextDecorator` as a mixin class:

```python
from contextlib import ContextDecorator

class mycontext(ContextBaseClass, ContextDecorator):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

```

Note

Given that the decorated function has to be callable more than once, the context manager underneath must permit use across several [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements. When that doesn't hold, fall back on the original construct that places the explicit `with` statement within the function.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](contextlib-redirect-stderr-to-contextlib-chdir.md) · [Continue](contextlib-asynccontextdecorator-class.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)

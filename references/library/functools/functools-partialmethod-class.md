# functools: `functools.partialmethod`

*class *functools.partialmethod(*func*, */*, **args*, ***keywords*)

Produce a fresh `partialmethod` descriptor that acts like `partial`, except it's intended for use within a method definition instead of being called outright.

*func* has to be a [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor) or a callable (objects qualifying as both, like ordinary functions, get treated as descriptors).

Where *func* is a descriptor (a normal Python function, [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod), [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod), [`abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod), or another `partialmethod` instance, for example), `__get__` calls are forwarded to the wrapped descriptor, and a fitting partial object comes back as the result.

Where *func* is a non-descriptor callable, a fitting bound method gets built on the fly. It acts like an ordinary Python function when serving as a method: the *self* argument slots in as the very first positional argument, ahead even of the *args* and *keywords* passed to the `partialmethod` constructor.

Example:

```python
>>> class Cell:
...     def __init__(self):
...         self._alive = False
...     @property
...     def alive(self):
...         return self._alive
...     def set_state(self, state):
...         self._alive = bool(state)
...     set_alive = partialmethod(set_state, True)
...     set_dead = partialmethod(set_state, False)
...
>>> c = Cell()
>>> c.alive
False
>>> c.set_alive()
>>> c.alive
True

```

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](functools-partial.md) · [Continue](functools-reduce.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)

# functools: `functools.singledispatchmethod`

*class *functools.singledispatchmethod(*func*)

Transform a method into a [single-dispatch](https://docs.python.org/3.14/glossary.html#term-single-dispatch) [generic function](https://docs.python.org/3.14/glossary.html#term-generic-function).

Creating a generic method means attaching the `@singledispatchmethod` decorator to it. Keep in mind that when you write a method via `@singledispatchmethod`, dispatching keys off the type of the earliest argument that is neither *self* nor *cls*:

```python
class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

```

You can nest `@singledispatchmethod` inside other decorators, [`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) among them. Bear in mind that for `dispatcher.register` to work, `singledispatchmethod` has to sit as the *outer most* decorator. Below appears the `Negator` class whose `neg` methods are tied to the class itself rather than to one of its instances:

```python
class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg

```

This very approach carries over to comparable decorators as well, including [`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod), [`@~abc.abstractmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod), and more besides.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](functools-singledispatch-registry.md) · [Continue](functools-update-wrapper.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)

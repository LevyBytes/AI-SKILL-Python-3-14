# annotationlib — Creating a custom callable annotate function

### Creating a custom callable annotate function

Custom [annotate functions](https://docs.python.org/3.14/glossary.html#term-annotate-function) can be plain functions in the style of those generated automatically for functions, classes, and modules. Alternatively, they may want to take advantage of the encapsulation that classes afford, in which event any [callable](https://docs.python.org/3.14/glossary.html#term-callable) is fit to act as an annotate function.

In order to deliver the `VALUE`, `STRING`, or `FORWARDREF` formats directly, an [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function) is required to expose the attribute below:

-

A callable `__call__` whose signature is `__call__(format, /) -> dict` and which refrains from raising a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) when handed a format it supports.

So as to supply the `VALUE_WITH_FAKE_GLOBALS` format — the one drawn on to derive `STRING` or `FORWARDREF` on the fly whenever those are not handled directly — [annotate functions](https://docs.python.org/3.14/glossary.html#term-annotate-function) are obliged to expose the attributes that follow:

- A callable `__call__` whose signature is `__call__(format, /) -> dict` and which refrains from raising a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) when handed `VALUE_WITH_FAKE_GLOBALS`.

- A [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects) `__code__` that holds the compiled code belonging to the annotate function.

- Optional: A tuple `__kwdefaults__` carrying the function’s positional defaults, should the function that `__code__` stands for make use of any positional defaults.

- Optional: A dict `__defaults__` carrying the function’s keyword defaults, should the function that `__code__` stands for make use of any keyword defaults.

- Optional: Every other one of the [function attributes](https://docs.python.org/3.14/library/inspect.html#inspect-types).

```python
class Annotate:
    called_formats = []

    def __call__(self, format=None, /, *, _self=None):
        # When called with fake globals, `_self` will be the
        # actual self value, and `self` will be the format.
        if _self is not None:
            self, format = _self, self

        self.called_formats.append(format)
        if format <= 2:  # VALUE or VALUE_WITH_FAKE_GLOBALS
            return {"x": MyType}
        raise NotImplementedError

    __code__ = __call__.__code__
    __defaults__ = (None,)
    __kwdefaults__ = property(lambda self: dict(_self=self))

    __globals__ = {}
    __builtins__ = {}
    __closure__ = None

```

From there it can be invoked like so:

```pycon
>>> from annotationlib import call_annotate_function, Format
>>> call_annotate_function(Annotate(), format=Format.STRING)
{'x': 'MyType'}

```

Or pressed into service as an object’s annotate function:

```pycon
>>> from annotationlib import get_annotations, Format
>>> class C:
...   pass
>>> C.__annotate__ = Annotate()
>>> get_annotations(Annotate(), format=Format.STRING)
{'x': 'MyType'}

```

[Subject index](INDEX.md) · [Previous](using-annotations-in-a-metaclass.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Continue](ast-binop-to-ast-subscript.md)

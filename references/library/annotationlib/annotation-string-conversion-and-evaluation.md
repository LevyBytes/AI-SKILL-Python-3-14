# annotationlib: `annotationlib.annotations_to_string()`, `annotationlib.call_annotate_function()`, `annotationlib.call_evaluate_function()`

### Functions

 annotationlib.annotations_to_string(*annotations*)

Take an annotations dict whose values are runtime objects and produce a dict made up only of strings. Any values that are not already strings get converted via `type_repr()`. This is intended as a helper for annotate functions written by users that handle the `STRING` format yet lack access to the code that builds the annotations.

As an example, this drives the `STRING` implementation for [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) classes built with the functional syntax:

```pycon
>>> from typing import TypedDict
>>> Movie = TypedDict("movie", {"name": str, "year": int})
>>> get_annotations(Movie, format=Format.STRING)
{'name': 'str', 'year': 'int'}

```

Added in version 3.14.

 annotationlib.call_annotate_function(*annotate*, *format*, ***, *owner=None*)

Invoke the [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function) *annotate* under the supplied *format* — a member of the `Format` enum — and return the annotations dictionary it yields.

This helper is needed because the annotate functions the compiler generates for functions, classes, and modules only handle the `VALUE` format when invoked outright. To cover the remaining formats, this function runs the annotate function within a special environment that lets it yield annotations in those other formats. It makes a handy building block whenever you are implementing behavior that has to partially evaluate annotations as a class is under construction.

*owner* is whatever object owns the annotation function — typically a function, class, or module. When supplied, it is used by the `FORWARDREF` format to yield a `ForwardRef` object bearing richer information.

See also

[**PEP 649**](https://peps.python.org/pep-0649/#the-stringizer-and-the-fake-globals-environment) lays out the implementation technique that this function relies on.

Added in version 3.14.

 annotationlib.call_evaluate_function(*evaluate*, *format*, ***, *owner=None*)

Invoke the [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) *evaluate* under the supplied *format* — a member of the `Format` enum — and return the value it yields. This parallels `call_annotate_function()`, except that the latter always gives back a dictionary mapping strings onto annotations, whereas this function gives back a lone value.

It is meant for use alongside the evaluate functions produced for lazily evaluated elements tied to type aliases and type parameters:

- [`typing.TypeAliasType.evaluate_value()`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType.evaluate_value), the value of type aliases

- [`typing.TypeVar.evaluate_bound()`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar.evaluate_bound), the bound of type variables

- [`typing.TypeVar.evaluate_constraints()`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar.evaluate_constraints), the constraints of type variables

- [`typing.TypeVar.evaluate_default()`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar.evaluate_default), the default value of type variables

- [`typing.ParamSpec.evaluate_default()`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec.evaluate_default), the default value of parameter specifications

- [`typing.TypeVarTuple.evaluate_default()`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple.evaluate_default), the default value of type variable tuples

*owner* is the object to which the evaluate function belongs — for instance, the relevant type alias or type variable object.

*format* lets you steer which format the value comes back in:

```pycon
>>> type Alias = undefined
>>> call_evaluate_function(Alias.evaluate_value, Format.VALUE)
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
ForwardRef('undefined')
>>> call_evaluate_function(Alias.evaluate_value, Format.STRING)
'undefined'

```

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](forward-reference-class-and-evaluation.md) · [Continue](annotationlib-get-annotate-from-class-namespace.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)

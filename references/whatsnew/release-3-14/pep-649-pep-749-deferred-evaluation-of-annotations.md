# What's new in Python 3.14 / **PEP 649** & **PEP 749**: Deferred evaluation of annotations — annotationlib

### New features

### [**PEP 649**](https://peps.python.org/pep-0649/) & [**PEP 749**](https://peps.python.org/pep-0749/): Deferred evaluation of annotations

Eager evaluation no longer applies to the [annotations](https://docs.python.org/3.14/glossary.html#term-annotation) attached to functions, classes, and modules. Rather, each set of annotations now lives inside dedicated [annotate functions](https://docs.python.org/3.14/glossary.html#term-annotate-function), computed lazily only at the moment they are needed (the exception being when `from __future__ import annotations` is active).

The aim of this shift is better speed and a smoother experience around Python annotations across most scenarios. Although defining annotations now carries minimal runtime overhead, runtime introspection of them stays fully available. Wrapping annotations in quotes to handle forward references is also no longer required.

Inspecting these lazily computed annotations is handled by the brand-new [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib) module. You can resolve annotations through the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format (which produces runtime values, matching how older Python releases behaved), the [`FORWARDREF`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.FORWARDREF) format (which substitutes special placeholder markers for names that aren't defined), or the [`STRING`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.STRING) format (which hands annotations back as plain strings).

The snippet below demonstrates each format in action:

```pycon
>>> from annotationlib import get_annotations, Format
>>> def func(arg: Undefined):
...     pass
>>> get_annotations(func, format=Format.VALUE)
Traceback (most recent call last):
  ...
NameError: name 'Undefined' is not defined
>>> get_annotations(func, format=Format.FORWARDREF)
{'arg': ForwardRef('Undefined', owner=<function func at 0x...>)}
>>> get_annotations(func, format=Format.STRING)
{'arg': 'Undefined'}

```

Adjustments you might require because of all this are covered in the porting section, though the bulk of existing code should keep running unchanged.

(Contributed by Jelle Zijlstra in [**PEP 749**](https://peps.python.org/pep-0749/) and [gh-119180](https://github.com/python/cpython/issues/119180); [**PEP 649**](https://peps.python.org/pep-0649/) was written by Larry Hastings.)

See also

[**PEP 649**](https://peps.python.org/pep-0649/)

Deferred Evaluation Of Annotations Using Descriptors

[**PEP 749**](https://peps.python.org/pep-0749/)

Implementing PEP 649

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-734-multiple-interpreters-in-the-standard-library.md) · [Release/subject declaration](summary-release-highlights.md)

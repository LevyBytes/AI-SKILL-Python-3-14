# inspect: `inspect.Parameter`, `kind.description`

*class *inspect.Parameter(*name*, *kind*, ***, *default=Parameter.empty*, *annotation=Parameter.empty*)

`Parameter` objects are *immutable*. Rather than altering a `Parameter` object directly, you can call `Parameter.replace()` or [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) to produce a modified copy.

Changed in version 3.5: Parameter objects are now picklable and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

 empty

A dedicated class-level marker indicating the absence of default values and annotations.

 name

The parameter's name as a string. That name has to be a valid Python identifier.

**CPython implementation detail:** CPython produces implicit parameter names shaped like `.0` on the code objects that back comprehensions and generator expressions.

Changed in version 3.6: This module now surfaces such parameter names under labels like `implicit0`.

 default

The parameter's default value. When the parameter lacks a default value, this attribute holds `Parameter.empty`.

 annotation

The parameter's annotation. When the parameter lacks an annotation, this attribute holds `Parameter.empty`.

 kind

Spells out how argument values get bound to the parameter. The available values are reachable through `Parameter` (such as `Parameter.KEYWORD_ONLY`), and they support comparison and ordering, in the order below:

| Name | Meaning |
| --- | --- |
| *POSITIONAL_ONLY* | The value has to be passed positionally. Such positional-only parameters are the ones sitting ahead of a `/` entry (where one exists) within a Python function definition. |
| *POSITIONAL_OR_KEYWORD* | The value can be passed either by keyword or positionally (the usual binding rule for Python-implemented functions.) |
| *VAR_POSITIONAL* | A tuple gathering positional arguments left unbound to any other parameter. It maps to a `*args` parameter inside a Python function definition. |
| *KEYWORD_ONLY* | The value has to be passed by keyword. Such keyword-only parameters are the ones following a `*` or `*args` entry within a Python function definition. |
| *VAR_KEYWORD* | A dict gathering keyword arguments left unbound to any other parameter. It maps to a `**kwargs` parameter inside a Python function definition. |

Example: print all keyword-only arguments without default values:

```pycon
>>> def foo(a, b, *, c, d=10):
...     pass

>>> sig = signature(foo)
>>> for param in sig.parameters.values():
...     if (param.kind == param.KEYWORD_ONLY and
...                        param.default is param.empty):
...         print('Parameter:', param)
Parameter: c

```

 kind.description

Spells out an enum value of `Parameter.kind`.

Added in version 3.8.

Example: print all descriptions of arguments:

```pycon
>>> def foo(a, b, *, c, d=10):
...     pass

>>> sig = signature(foo)
>>> for param in sig.parameters.values():
...     print(param.kind.description)
positional or keyword
positional or keyword
keyword-only
keyword-only

```

[Subject index](INDEX.md) · [Previous](inspect-signature-class-to-inspect-signature-format.md) · [Continue](inspect-parameter-replace.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Introspecting callables with the Signature object](inspect-signature.md)

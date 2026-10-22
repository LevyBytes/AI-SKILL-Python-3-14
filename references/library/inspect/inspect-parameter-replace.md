# inspect.Parameter: `replace()`

replace(**[, name][, kind][, default][, annotation]*)

Build a fresh `Parameter` instance derived from the instance on which replaced was called. To swap out a `Parameter` attribute, supply the matching argument. To strip a default value and/or an annotation from a `Parameter`, hand in `Parameter.empty`.

```pycon
>>> from inspect import Parameter
>>> param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)
>>> str(param)
'foo=42'

>>> str(param.replace()) # Will create a shallow copy of 'param'
'foo=42'

>>> str(param.replace(default=Parameter.empty, annotation='spam'))
"foo: 'spam'"

```

`Parameter` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace).

Changed in version 3.4: Under Python 3.3 a `Parameter` object could carry `name` equal to `None` whenever its `kind` was `POSITIONAL_ONLY`. That is no longer allowed.

[Subject index](INDEX.md) · [Previous](inspect-parameter-class-to-kind-description.md) · [Continue](bound-signature-arguments-and-defaults.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: inspect.Parameter](inspect-parameter-class-to-kind-description.md) · [Owning module, declaration or section: Introspecting callables with the Signature object](inspect-signature.md)

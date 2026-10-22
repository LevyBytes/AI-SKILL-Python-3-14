# inspect / Introspecting callables with the Signature object: `inspect.Signature`, `bind()`, `bind_partial()`, `replace()`, `format()`, `from_callable()`

*class *inspect.Signature(*parameters=None*, ***, *return_annotation=Signature.empty*)

A function's call signature, together with its return annotation, is captured by a `Signature` object. It keeps a `Parameter` object inside its `parameters` collection for every parameter the function takes.

The optional *parameters* argument is a sequence of `Parameter` objects; this sequence is checked to confirm that no two parameters share a name and that the parameters follow the correct ordering — positional-only first, then positional-or-keyword — with defaulted parameters coming after those lacking defaults.

The optional *return_annotation* argument may be any arbitrary Python object. It stands for the callable's "return" annotation.

`Signature` objects are *immutable*. Use `Signature.replace()` or [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) to make a modified copy.

Changed in version 3.5: `Signature` objects are now picklable and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

 empty

A dedicated class-level marker indicating that a return annotation is absent.

 parameters

An ordered mapping that ties each parameter's name to its matching `Parameter` object. The parameters show up in strict definition order, keyword-only parameters included.

Changed in version 3.7: Only as of version 3.7 did Python explicitly promise to keep the declaration order of keyword-only parameters, though this ordering had in fact always held in Python 3.

 return_annotation

The callable's "return" annotation. When the callable carries no "return" annotation, this attribute holds `Signature.empty`.

 bind(**args*, ***kwargs*)

Build a mapping that connects positional and keyword arguments to parameters. Yields `BoundArguments` when `*args` and `**kwargs` line up with the signature; otherwise raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 bind_partial(**args*, ***kwargs*)

Operates just like `Signature.bind()`, except it permits leaving out some required arguments (echoing [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) behavior.) Yields `BoundArguments`, or raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when the supplied arguments don't fit the signature.

 replace(**[, parameters][, return_annotation]*)

Build a fresh `Signature` instance derived from the instance on which `replace()` was called. You can supply different *parameters* and/or *return_annotation* to swap out the matching properties of the base signature. To strip `return_annotation` from the copied `Signature`, hand in `Signature.empty`.

```pycon
>>> def test(a, b):
...     pass
...
>>> sig = signature(test)
>>> new_sig = sig.replace(return_annotation="new return anno")
>>> str(new_sig)
"(a, b) -> 'new return anno'"

```

`Signature` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace).

 format(***, *max_width=None*, *quote_annotation_strings=True*)

Produce a string rendering of the `Signature` object.

When *max_width* is supplied, the method tries to pack the signature into lines no wider than *max_width* characters. Should the signature exceed *max_width*, every parameter lands on its own line.

When *quote_annotation_strings* is False, string-valued [annotations](https://docs.python.org/3.14/glossary.html#term-annotation) within the signature are shown without their surrounding quotation marks. This comes in handy when the signature was built with the [`STRING`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.STRING) format or when `from __future__ import annotations` was used.

Added in version 3.13.

Changed in version 3.14: The *unquote_annotations* parameter was added.

 *classmethod *from_callable(*obj*, ***, *follow_wrapped=True*, *globals=None*, *locals=None*, *eval_str=False*)

Yield a `Signature` (or subclass) object for the supplied callable *obj*.

This method makes subclassing of `Signature` easier:

```python
class MySignature(Signature):
    pass
sig = MySignature.from_callable(sum)
assert isinstance(sig, MySignature)

```

Aside from that, it behaves exactly like `signature()`.

Added in version 3.5.

Changed in version 3.10: The *globals*, *locals*, and *eval_str* parameters were added.

[Subject index](INDEX.md) · [Previous](introspecting-callables-with-the-signature-object.md) · [Continue](inspect-parameter-class-to-kind-description.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Introspecting callables with the Signature object](inspect-signature.md)

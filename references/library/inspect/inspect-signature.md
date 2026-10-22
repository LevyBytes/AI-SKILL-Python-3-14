# inspect: `inspect.signature()`

### Introspecting callables with the Signature object

Added in version 3.3.

A `Signature` object captures the call signature of a callable object together with its return annotation. To obtain a `Signature` object, call the `signature()` function.

 inspect.signature(*callable*, ***, *follow_wrapped=True*, *globals=None*, *locals=None*, *eval_str=False*, *annotation_format=Format.VALUE*)

Return a `Signature` object for the given *callable*:

```pycon
>>> from inspect import signature
>>> def foo(a, *, b:int, **kwargs):
...     pass

>>> sig = signature(foo)

>>> str(sig)
'(a, *, b: int, **kwargs)'

>>> str(sig.parameters['b'])
'b: int'

>>> sig.parameters['b'].annotation
<class 'int'>

```

A broad assortment of Python callables works here, ranging from ordinary functions and classes through to [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects.

[Subject index](INDEX.md) · [Previous](inspect-getdoc-to-inspect-cleandoc.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Required continuation of the source contract](introspecting-callables-with-the-signature-object.md)

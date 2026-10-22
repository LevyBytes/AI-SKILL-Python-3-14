# annotationlib: `annotationlib.get_annotations()`

annotationlib.get_annotations(*obj*, ***, *globals=None*, *locals=None*, *eval_str=False*, *format=Format.VALUE*)

Work out the annotations dict for an object.

*obj* may be a callable, a class, a module, or any other object carrying [`__annotate__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotate__) or [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attributes. Handing in anything else raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

The *format* parameter dictates which format the annotations come back in, and it has to be a member of the `Format` enum or the integer that matches it. Here is how each format operates:

- VALUE: `object.__annotations__` is attempted first; should it be absent, the `object.__annotate__` function gets invoked if one is present.

- FORWARDREF: When `object.__annotations__` is present and evaluates without trouble, that is what is used; failing that, the `object.__annotate__` function gets invoked. Should it too be absent, `object.__annotations__` is attempted once more and whatever error arises from accessing it is re-raised.

  - In invoking `object.__annotate__`, the first attempt uses `FORWARDREF`. If that is unimplemented, it next checks whether `VALUE_WITH_FAKE_GLOBALS` is supported and employs it within the fake globals environment. With neither format supported, it falls back on `VALUE`. Should `VALUE` fail, the error from that call is raised.

- STRING: When `object.__annotate__` is present, it gets invoked first; otherwise `object.__annotations__` is taken and stringified through `annotations_to_string()`.

  - In invoking `object.__annotate__`, the first attempt uses `STRING`. If that is unimplemented, it next checks whether `VALUE_WITH_FAKE_GLOBALS` is supported and employs it within the fake globals environment. With neither format supported, it falls back on `VALUE` and converts the outcome via `annotations_to_string()`. Should `VALUE` fail, the error from that call is raised.

Returns a dict. Each invocation of `get_annotations()` produces a fresh dict; invoking it twice against the same object yields two separate dicts that are nonetheless equivalent.

A number of details are taken care of for you by this function:

- When *eval_str* is true, values whose type is `str` get un-stringized by means of [`eval()`](https://docs.python.org/3.14/library/functions.html#eval). This targets stringized annotations (`from __future__ import annotations`). Setting *eval_str* to true together with any format other than `Format.VALUE` is an error.

- When *obj* carries no annotations dict, an empty dict is returned. (Functions and methods invariably carry an annotations dict; classes, modules, and other sorts of callables may not.)

- Disregards annotations inherited onto classes, along with annotations on metaclasses. When a class lacks an annotations dict of its own, an empty dict is returned.

- For safety, every access to object members and to dict values goes through `getattr()` and `dict.get()`.

*eval_str* governs whether values of type `str` get swapped out for the outcome of calling [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) on them:

- When eval_str is true, [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) gets called on values of type `str`. (Be aware that `get_annotations()` does not trap exceptions; if `eval()` raises, the exception unwinds the stack on past the `get_annotations()` call.)

- When *eval_str* is false (the default), values of type `str` are left untouched.

*globals* and *locals* get forwarded to [`eval()`](https://docs.python.org/3.14/library/functions.html#eval); see the `eval()` documentation for further detail. When either *globals* or *locals* is `None`, this function may substitute a context-specific default in its place, depending on `type(obj)`:

- When *obj* is a module, *globals* defaults to `obj.__dict__`.

- For an *obj* that is a class, the default for *globals* becomes `sys.modules[obj.__module__].__dict__`, while *locals* defaults to that class's namespace.

- When *obj* is a callable, *globals* defaults to [`obj.__globals__`](https://docs.python.org/3.14/reference/datamodel.html#function.__globals__); however, if *obj* is a wrapped function (via [`functools.update_wrapper()`](https://docs.python.org/3.14/library/functools.html#functools.update_wrapper)) or a [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) object, it is unwrapped until a function that is not wrapped turns up.

Reaching for `get_annotations()` is the recommended approach to obtaining the annotations dict of any object. Consult [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto) for additional guidance on annotation best practices.

```pycon
>>> def f(a: int, b: str) -> float:
...     pass
>>> get_annotations(f)
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

```

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](annotationlib-get-annotate-from-class-namespace.md) · [Continue](annotationlib-type-repr.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Owning module, declaration or section: Functions](annotation-string-conversion-and-evaluation.md)

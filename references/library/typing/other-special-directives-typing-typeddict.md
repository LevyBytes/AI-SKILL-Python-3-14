# typing: TypedDict totality and required-key introspection

__total__

`Point2D.__total__` gives the value of the `total` argument. Example:

```pycon
>>> from typing import TypedDict
>>> class Point2D(TypedDict): pass
>>> Point2D.__total__
True
>>> class Point2D(TypedDict, total=False): pass
>>> Point2D.__total__
False
>>> class Point3D(Point2D): pass
>>> Point3D.__total__
True

```

What this attribute mirrors is *only* the `total` argument supplied to the current `TypedDict` class, not whether that class is semantically total. To illustrate, a `TypedDict` whose `__total__` is `True` might still carry keys flagged `NotRequired`, or it might inherit from another `TypedDict` that used `total=False`. For that reason, `__required_keys__` and `__optional_keys__` are generally the better choice for introspection.

 __required_keys__

Added in version 3.9.

 __optional_keys__

Calling `Point2D.__required_keys__` and `Point2D.__optional_keys__` yields [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) objects that hold, in turn, the required keys and the non-required keys.

Keys carrying `Required` always show up in `__required_keys__`, and keys carrying `NotRequired` always show up in `__optional_keys__`.

To stay compatible with Python 3.10 and earlier, you may also rely on inheritance to declare both required and non-required keys within a single `TypedDict`. The trick is to declare a `TypedDict` using one `total` value and then inherit from it in a second `TypedDict` that uses a different `total` value:

```pycon
>>> class Point2D(TypedDict, total=False):
...     x: int
...     y: int
...
>>> class Point3D(Point2D):
...     z: int
...
>>> Point3D.__required_keys__ == frozenset({'z'})
True
>>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
True

```

Added in version 3.9.

Note

When `from __future__ import annotations` is in effect, or when annotations are supplied as strings, the annotations go unevaluated at the point the `TypedDict` is defined. The runtime introspection on which `__required_keys__` and `__optional_keys__` depend may therefore misbehave, leaving the attribute values possibly wrong.

Support for `ReadOnly` is reflected in the following attributes:

 __readonly_keys__

A [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) holding the names of every read-only key. A key counts as read-only when it bears the `ReadOnly` qualifier.

Added in version 3.13.

 __mutable_keys__

A [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) holding the names of every mutable key. A key counts as mutable when it lacks the `ReadOnly` qualifier.

Added in version 3.13.

Consult the [TypedDict](https://typing.python.org/en/latest/spec/typeddict.html#typeddict) section of the typing spec for further worked examples and the complete ruleset.

Added in version 3.8.

Changed in version 3.9: `TypedDict` became a function instead of a class. As shown above, it can still serve as a class base.

Changed in version 3.11: Marking individual keys as `Required` or `NotRequired` became supported. Refer to [**PEP 655**](https://peps.python.org/pep-0655/).

Changed in version 3.11: Generic `TypedDict`s became supported.

Changed in version 3.13: The keyword-argument way of creating `TypedDict`s was dropped.

Changed in version 3.13: The `ReadOnly` qualifier became supported.

Deprecated since version 3.13, will be removed in version 3.15: With the functional syntax for creating a TypedDict class, omitting a value for the 'fields' parameter (`TD = TypedDict("TD")`) is deprecated. Likewise, supplying `None` for the 'fields' parameter (`TD = TypedDict("TD", None)`) is deprecated. Python 3.15 will reject both. For a TypedDict class holding 0 fields, write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

[Subject index](INDEX.md) · [Previous](typed-dictionary-optional-fields-example.md) · [Continue](typing-supportsabs-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypedDict](typing-typeddict-class.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)

# typing: `typing.evaluate_forward_ref()`, `typing.NoDefault`

typing.evaluate_forward_ref(*forward_ref*, ***, *owner=None*, *globals=None*, *locals=None*, *type_params=None*, *format=annotationlib.Format.VALUE*)

Evaluate an [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) as a [type hint](https://docs.python.org/3.14/glossary.html#term-type-hint).

The behavior resembles a call to [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate), except that, in contrast to that method, `evaluate_forward_ref()` additionally descends recursively into and evaluates forward references embedded inside the type hint.

For what the *owner*, *globals*, *locals*, *type_params*, and *format* parameters signify, refer to the [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate) documentation.

Caution

Arbitrary code held inside annotations may be run by this function. Consult [Security implications of introspecting annotations](https://docs.python.org/3.14/library/annotationlib.html#annotationlib-security) for further detail.

Added in version 3.14.

 typing.NoDefault

A sentinel object that marks a type parameter as having no default value. As an example:

```pycon
>>> T = TypeVar("T")
>>> T.__default__ is typing.NoDefault
True
>>> S = TypeVar("S", default=None)
>>> S.__default__ is None
True

```

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](typing-forwardref-class.md) · [Continue](typing-type-checking.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Introspection helpers](typing-get-type-hints-to-typing-get-origin.md)

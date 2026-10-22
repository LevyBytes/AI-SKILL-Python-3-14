# typing.TypeAliasType: `evaluate_value()`

evaluate_value()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__value__` attribute. Called by itself, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which is the same as reading the `__value__` attribute directly; but the method object may be handed to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) to compute the value under a different format:

```pycon
>>> type Alias = undefined
>>> Alias.__value__
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> from annotationlib import Format, call_evaluate_function
>>> Alias.evaluate_value(Format.VALUE)
Traceback (most recent call last):
...
NameError: name 'undefined' is not defined
>>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
ForwardRef('undefined')

```

Added in version 3.14.

Unpacking

Star unpacking is available for type aliases via the `*Alias` syntax, which behaves the same as writing `Unpack[Alias]` directly:

```pycon
>>> type Alias = tuple[int, str]
>>> type Unpacked = tuple[bool, *Alias]
>>> Unpacked.__value__
tuple[bool, typing.Unpack[Alias]]

```

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](typing-typealiastype-class.md) · [Continue](type-construction-directives.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypeAliasType](typing-typealiastype-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)

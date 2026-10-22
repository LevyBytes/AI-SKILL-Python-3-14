# string.templatelib: `string.templatelib.Interpolation`

*class *string.templatelib.Interpolation

An `Interpolation` type stands for one expression embedded within a template string. Like the template, it is immutable, so the attributes of an interpolation cannot be reassigned.

Because interpolations work with pattern matching, you can match on their attributes through the [match statement](https://docs.python.org/3.14/reference/compound_stmts.html#match):

```python
>>> from string.templatelib import Interpolation
>>> interpolation = t'{1. + 2.:.2f}'.interpolations[0]
>>> interpolation
Interpolation(3.0, '1. + 2.', None, '.2f')
>>> match interpolation:
...     case Interpolation(value, expression, conversion, format_spec):
...         print(value, expression, conversion, format_spec, sep=' | ')
...
3.0 | 1. + 2. | None | .2f

```

With respect to the types of the values they carry, interpolations are [generic](https://docs.python.org/3.14/library/typing.html#generics).

Attributes

 value*: [object](https://docs.python.org/3.14/library/functions.html#object)*

The interpolation's value once it has been evaluated.

```python
>>> t'{1 + 2}'.interpolations[0].value
3

```

 expression*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

When an interpolation comes from a t-string literal, `expression` is the chunk of expression text sitting within the curly brackets (`{` & `}`) - whitespace kept, the brackets themselves dropped, and the text cut off just ahead of the first `!`, `:`, or `=` should one occur. For interpolations you assemble by hand, `expression` is simply whatever arbitrary string you supplied while constructing the instance.

For the `expression` field of hand-built `Interpolation` instances, our advice is to stick to valid Python expressions or to an empty string, though nothing at runtime forces this.

```python
>>> t'{1 + 2}'.interpolations[0].expression
'1 + 2'

```

 conversion*: [Literal](https://docs.python.org/3.14/library/typing.html#typing.Literal)['a', 'r', 's'] | [None](https://docs.python.org/3.14/library/constants.html#None)*

Which conversion gets applied to the value, or else `None`.

The `conversion` attribute names the optional conversion that should be applied to the value:

```python
>>> t'{1 + 2!a}'.interpolations[0].conversion
'a'

```

Note

With f-strings, conversions happen on their own, but t-strings work differently: it falls to whatever code *processes* the `Template` to choose how the `conversion` is read and whether it gets applied at all. As a shortcut, you can lean on the `convert()` function to reproduce the conversion behavior of f-strings.

 format_spec*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

The format specification that the value should be presented with.

The `format_spec` is an optional, free-form string serving as the format specification for displaying the value:

```python
>>> t'{1 + 2:.2f}'.interpolations[0].format_spec
'.2f'

```

Note

Whereas f-strings apply format specifications on their own by way of the [`format()`](https://docs.python.org/3.14/library/functions.html#format) protocol, with t-strings it is the code *processing* the interpolation that settles how the format specification is understood and whether it is applied. Because of this, a `format_spec` on an interpolation may be any arbitrary string at all, even one that breaks the `format()` protocol.

Methods

[Subject index](INDEX.md) · [Previous](string-templatelib-template-iter.md) · [Continue](string-templatelib-interpolation-new.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md) · [Owning module, declaration or section: Types](string-templatelib-template-class.md)

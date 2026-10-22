# decimal — Decimal FAQ — Section introduction and initial examples

### Decimal FAQ

Q: Typing `decimal.Decimal('1234.5')` gets tedious. Is there a way to cut down on typing while using the interactive interpreter?

A: Some users shorten the constructor down to a single letter:

```python
>>> D = decimal.Decimal
>>> D('1.23') + D('3.45')
Decimal('4.68')

```

Q: In a fixed-point application with two decimal places, certain inputs arrive with many places and must be rounded. Others should not carry excess digits and must be validated. Which methods ought to be used?

A: The `quantize()` method rounds down to a fixed count of decimal places. When the `Inexact` trap is active, it doubles as a validation tool:

```python
>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')

```

```python
>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')

```

```python
>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')

```

```python
>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None

```

Q: After I have valid two place inputs, how do I keep that invariant across an application?

A: Certain operations such as addition, subtraction, and multiplication by an integer will keep fixed point automatically. Other operations, like division and non-integer multiplication, will alter the count of decimal places and have to be followed up with a `quantize()` step:

```python
>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')

```

When building fixed-point applications, it helps to define functions that handle the `quantize()` step:

```python
>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
...
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)

```

```python
>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')

```

[Subject index](INDEX.md) · [Previous](decimal-sine-cosine-precision-recipes.md) · [Continue](decimal-equivalent-representations-faq.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)

# Additional Methods on Float

### Additional Methods on Float

The float type implements the [`numbers.Real`](https://docs.python.org/3.14/library/numbers.html#numbers.Real) [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class). float carries the following extra methods as well.

 *classmethod *float.from_number(*x*)

A class method returning a floating-point number built out of a number *x*.

When the argument is an integer or a floating-point number, you get back a floating-point number holding the same value (to the limit of Python’s floating-point precision). When the argument lies beyond the range of a Python float, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) gets raised.

When `x` is some general Python object, `float.from_number(x)` defers to `x.__float__()`. Where [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) is missing, it instead falls back on [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

Added in version 3.14.

 float.as_integer_ratio()

Return a pair of integers whose ratio is precisely equal to the original float. That ratio comes in lowest terms with a positive denominator. It raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) on infinities and a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) on NaNs.

 float.is_integer()

Return `True` when the float instance is finite and holds an integral value, and `False` if not:

```python
>>> (-2.0).is_integer()
True
>>> (3.2).is_integer()
False

```

A couple of methods handle conversion to and from hexadecimal strings. Because Python keeps its floats internally as binary numbers, taking a float to or from a *decimal* string normally brings a small rounding error along with it. Hexadecimal strings, by contrast, let floating-point numbers be represented and specified exactly. That comes in handy while debugging and during numerical work.

 float.hex()

Return a floating-point number rendered as a hexadecimal string. With finite floating-point numbers, this rendering always carries a leading `0x` plus a trailing `p` and exponent.

 *classmethod *float.fromhex(*s*)

A class method returning the float that a hexadecimal string *s* represents. Leading and trailing whitespace is allowed on the string *s*.

Bear in mind that `float.hex()` is an instance method while `float.fromhex()` is a class method.

The form a hexadecimal string takes is:

```python
[sign] ['0x'] integer ['.' fraction] ['p' exponent]

```

where the optional `sign` is either `+` or `-`, where `integer` and `fraction` are strings of hexadecimal digits, and where `exponent` is a decimal integer carrying an optional leading sign. Case makes no difference, and the integer or the fraction must contain at least one hexadecimal digit. This syntax resembles the one laid out in section 6.4.4.2 of the C99 standard, as well as the syntax in use since Java 1.5. In particular, the output of `float.hex()` can serve as a hexadecimal floating-point literal in C or Java code, and `float.fromhex()` accepts hexadecimal strings turned out by C’s `%a` format character or by Java’s `Double.toHexString`.

Bear in mind that the exponent appears in decimal rather than hexadecimal, and that it states the power of 2 the coefficient is to be multiplied by. The hexadecimal string `0x3.a7p10`, for example, stands for the floating-point number `(3 + 10./16 + 7./16**2) * 2.0**10`, that is, `3740.0`:

```python
>>> float.fromhex('0x3.a7p10')
3740.0

```

Running the conversion the other way on `3740.0` yields a different hexadecimal string standing for the same number:

```python
>>> float.hex(3740.0)
'0x1.d380000000000p+11'

```

[Subject index](INDEX.md) · [Previous](int-as-integer-ratio-to-int-is-integer.md) · [Continue](additional-methods-on-complex.md)

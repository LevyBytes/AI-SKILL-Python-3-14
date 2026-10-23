# What's New In Python 3.2 / decimal and fractions - decimal, fractions, sys

### decimal and fractions

To guarantee that distinct numeric datatypes share one hash value whenever the values they hold are equal, Mark Dickinson designed a clean and efficient scheme ([bpo-8188](https://bugs.python.org/issue?@action=redirect&bpo=8188)):

```python
assert hash(Fraction(3, 2)) == hash(1.5) == \
       hash(Decimal("1.5")) == hash(complex(1.5, 0))

```

A new attribute, [`sys.hash_info`](https://docs.python.org/3.14/library/sys.html#sys.hash_info), surfaces some of the hashing internals: it reports the hash value's bit width, the prime modulus, the hash results for *infinity* and *nan*, and the multiplier applied to a number's imaginary component:

```python
>>> sys.hash_info
sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003)

```

A previous restriction on how freely the various numeric types interoperate has been loosened. Implicit mixing within arithmetic expressions like `Decimal('1.1') + float('1.1')` stays unsupported (and inadvisable) since that float discards information while building the binary value. Even so, any existing floating-point value converts without loss to either a decimal or a rational form, so it is sensible to permit them in the constructor and to allow cross-type comparisons.

- A [`float`](https://docs.python.org/3.14/library/functions.html#float) object is now taken directly by the [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) constructor, removing any reason to reach for the [`from_float()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.from_float) method ([bpo-8257](https://bugs.python.org/issue?@action=redirect&bpo=8257)).

- Comparisons across types now work completely, letting a [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) object be compared straight against [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) ([bpo-2531](https://bugs.python.org/issue?@action=redirect&bpo=2531) and [bpo-8188](https://bugs.python.org/issue?@action=redirect&bpo=8188)).

Comparable adjustments reached [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction), so its [`from_float()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.from_float) and [`from_decimal()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.from_decimal) methods became unnecessary ([bpo-8294](https://bugs.python.org/issue?@action=redirect&bpo=8294)):

```python
>>> from decimal import Decimal
>>> from fractions import Fraction
>>> Decimal(1.1)
Decimal('1.100000000000000088817841970012523233890533447265625')
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)

```

One more handy update to the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module is that its [`Context.clamp`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.clamp) attribute became public. That helps when constructing contexts matching the decimal interchange formats laid out in IEEE 754 (see [bpo-8540](https://bugs.python.org/issue?@action=redirect&bpo=8540)).

(Contributed by Mark Dickinson and Raymond Hettinger.)

[Subject index](INDEX.md) · [Previous source section](contextlib.md) · [Next source section](ftp.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

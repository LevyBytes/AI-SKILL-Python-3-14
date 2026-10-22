# decimal: `decimal.Decimal`

### Decimal objects

 *class *decimal.Decimal(*value='0'*, *context=None*)

Construct a new `Decimal` object based from *value*.

An integer, string, tuple, [`float`](https://docs.python.org/3.14/library/functions.html#float), or a second `Decimal` object may serve as *value*. With no *value* supplied, the call yields `Decimal('0')`. Where *value* is a string, it must match the decimal numeric string syntax once leading and trailing whitespace characters, plus any underscores throughout, have been stripped:

```python
sign           ::=  '+' | '-'
digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
indicator      ::=  'e' | 'E'
digits         ::=  digit [digit]...
decimal-part   ::=  digits '.' [digits] | ['.'] digits
exponent-part  ::=  indicator [sign] digits
infinity       ::=  'Infinity' | 'Inf'
nan            ::=  'NaN' [digits] | 'sNaN' [digits]
numeric-value  ::=  decimal-part [exponent-part] | infinity
numeric-string ::=  [sign] numeric-value | [sign] nan

```

Wherever `digit` shows up above, additional Unicode decimal digits are accepted too. These cover decimal digits drawn from a variety of other scripts (such as Arabic-Indic and Devanāgarī digits) together with the fullwidth digits `'\uff10'` through `'\uff19'`. Letter case carries no weight, so for instance `inf`, `Inf`, `INFINITY`, and `iNfINity` are all valid ways to write positive infinity.

When *value* is a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), it must consist of three parts: a sign (`0` meaning positive or `1` meaning negative), a `tuple` of digits, and an integer exponent. As an example, `Decimal((0, (1, 4, 1, 4), -3))` returns `Decimal('1.414')`.

When *value* is a [`float`](https://docs.python.org/3.14/library/functions.html#float), the binary floating-point value gets losslessly turned into its exact decimal counterpart. Such a conversion frequently calls for 53 or more digits of precision. To illustrate, `Decimal(float('1.1'))` converts to `Decimal('1.100000000000000088817841970012523233890533447265625')`.

How many digits are kept is not influenced by the *context* precision. It hinges solely on the digit count within *value*. For instance, `Decimal('3.00000')` preserves all five zeros even when the context precision is merely three.

The *context* argument exists to govern what happens if *value* is a malformed string. When the context traps `InvalidOperation`, an exception is raised; if not, the constructor hands back a new Decimal whose value is `NaN`.

After construction, `Decimal` objects do not change.

Changed in version 3.2: A [`float`](https://docs.python.org/3.14/library/functions.html#float) instance is now an acceptable argument for the constructor.

Changed in version 3.3: When the `FloatOperation` trap is enabled, passing [`float`](https://docs.python.org/3.14/library/functions.html#float) arguments raises an exception. That trap stays disabled by default.

Changed in version 3.6: For grouping, underscores may be used, just as they are in integral and floating-point code literals.

Decimal floating-point objects hold many traits in common with the other built-in numeric types, for instance [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`int`](https://docs.python.org/3.14/library/functions.html#int). Every one of the customary math operations and special methods is available. In the same way, decimal objects may be copied, pickled, printed, employed as dictionary keys, used as set elements, compared, sorted, and converted to a different type (for instance `float` or `int`).

A few minor distinctions separate arithmetic on Decimal objects from arithmetic on integers and floats. With the remainder operator `%` used on Decimal objects, the result takes the sign of the *dividend* instead of the divisor's sign:

```python
>>> (-7) % 4
1
>>> Decimal(-7) % Decimal(4)
Decimal('-3')

```

The integer division operator `//` works the same way, yielding the integer portion of the true quotient (truncated toward zero) instead of its floor, in order to keep the familiar identity `x == (x // y) * y + x % y`:

```python
>>> -7 // 4
-2
>>> Decimal(-7) // Decimal(4)
Decimal('-1')

```

The `%` and `//` operators carry out the `remainder` and `divide-integer` operations (in that order) as laid out in the specification.

In arithmetic operations Decimal objects normally cannot be mixed with floats or with instances of [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction): trying to add a `Decimal` to a [`float`](https://docs.python.org/3.14/library/functions.html#float), say, will raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Even so, you can rely on Python's comparison operators to compare a `Decimal` instance `x` against another number `y`. Doing so steers clear of puzzling outcomes when running equality comparisons across numbers of differing types.

Changed in version 3.2: Comparing `Decimal` instances against other numeric types across types now has complete support.

Beyond the usual numeric features, decimal floating-point objects come with several specialized methods as well:

[Subject index](INDEX.md) · [Previous](decimal-context-precision-and-rounding-example.md) · [Continue](decimal-decimal-adjusted-to-decimal-decimal-copy-negate.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)

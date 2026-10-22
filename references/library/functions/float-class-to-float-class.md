# Built-in Functions

*class *float(*number=0.0*, */*)

 *class *float(*string*, */*)

Build and return a floating-point number out of either a number or a string.

Examples:

```pycon
>>> float('+1.23')
1.23
>>> float('   -12345\n')
-12345.0
>>> float('1e-003')
0.001
>>> float('+1E6')
1000000.0
>>> float('-Infinity')
-inf

```

When the argument is a string, it ought to hold a decimal number, optionally with a sign in front, and optionally surrounded by whitespace. The optional sign may be `'+'` or `'-'`; a `'+'` sign leaves the resulting value unchanged. The argument can equally be a string standing for a NaN (not-a-number), or for positive or negative infinity. To be exact, the input has to match the `floatvalue` production rule of the grammar below, once leading and trailing whitespace characters have been stripped:

```text

sign:          "+" | "-"
infinity:      "Infinity" | "inf"
nan:           "nan"
digit:         <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
digitpart:     digit (["_"] digit)*
number:        [digitpart] "." digitpart | digitpart ["."]
exponent:      ("e" | "E") [sign] digitpart
floatnumber:   number [exponent]
absfloatvalue: floatnumber | infinity | nan
floatvalue:    [sign] absfloatvalue
```

Case carries no meaning, so for instance “inf”, “Inf”, “INFINITY”, and “iNfINity” all count as valid spellings for positive infinity.

In the other case, when the argument is an integer or a floating-point number, what comes back is a floating-point number carrying the same value (to the limit of Python's floating-point precision). When the argument lies beyond the range of a Python float, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) gets raised.

Given a general Python object `x`, `float(x)` defers to `x.__float__()`. When [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) isn't defined, it then falls back on [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

Also refer to [`float.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#float.from_number), which takes only a numeric argument.

With no argument supplied, `0.0` comes back.

The float type is covered in [Numeric Types — int, float, complex](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric).

Changed in version 3.6: Separating digits using underscores, the way code literals do, became permitted.

Changed in version 3.7: The parameter is now positional-only.

Changed in version 3.8: Falls back to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) is not defined.

[Subject index](INDEX.md) · [Previous](INDEX.md) · [Continue](format.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)

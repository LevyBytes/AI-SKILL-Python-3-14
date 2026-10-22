# pow

pow(*base*, *exp*, *mod=None*)

Yield *base* raised to the power *exp*; when *mod* is present, yield *base* raised to the power *exp*, modulo *mod* (worked out more efficiently than `pow(base, exp) % mod`). The two-argument form `pow(base, exp)` matches using the power operator: `base**exp`.

When the arguments are builtin numeric types with mixed operand types, the coercion rules governing binary arithmetic operators take effect. For `int` operands, the type carried by the result matches that of the operands (post-coercion), except where the second argument turns out negative; should that happen, every argument is converted to float and a float result comes out. As an example, `pow(10, 2)` yields `100`, but `pow(10, -2)` yields `0.01`. For a negative base of type `int` or `float` together with a non-integral exponent, a complex result comes out. As an example, `pow(-9, 0.5)` yields a value near `3j`. By contrast, for a negative base of type `int` or `float` together with an integral exponent, a float result comes out. As an example, `pow(-9, 2.0)` yields `81.0`.

For `int` operands *base* and *exp*, when *mod* is present, *mod* must likewise be of integer type and *mod* must be nonzero. Whenever *mod* is present alongside a negative *exp*, *base* has to be relatively prime to *mod*. Under those conditions, `pow(inv_base, -exp, mod)` comes back, where *inv_base* is an inverse to *base* modulo *mod*.

Below is an example of working out an inverse for `38` modulo `97`:

```python
>>> pow(38, -1, mod=97)
23
>>> 23 * 38 % 97 == 1
True

```

Changed in version 3.8: With `int` operands, `pow` in its three-argument form now lets the second argument be negative, which opens the door to computing modular inverses.

Changed in version 3.8: Keyword arguments became allowed. Previously the function accepted positional arguments alone.

[Builtin task index](INDEX.md).

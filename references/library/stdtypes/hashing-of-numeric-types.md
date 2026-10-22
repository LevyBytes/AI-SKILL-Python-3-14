# Hashing of numeric types

### Hashing of numeric types

Given numbers `x` and `y`, which may belong to different types, Python guarantees that `hash(x) == hash(y)` holds in every case where `x == y` (the [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method documentation covers this more thoroughly). To keep things implementable and quick across the assorted numeric types — among them [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) and [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)) — Python derives the hash of numeric values from one mathematical function that holds for every rational number; it therefore covers all instances of `int` and `fractions.Fraction`, plus all finite instances of `float` and `decimal.Decimal`. At heart, that function amounts to reduction modulo `P` for some fixed prime `P`. Python exposes the value of `P` through the [`modulus`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.modulus) attribute on [`sys.hash_info`](https://docs.python.org/3.14/library/sys.html#sys.hash_info).

**CPython implementation detail:** At present the chosen prime is `P = 2**31 - 1` where the C long is 32-bit, switching to `P = 2**61 - 1` where the C long is 64-bit.

Here are the rules in detail:

- When `x = m / n` is a nonnegative rational number whose `n` is not divisible by `P`, then `hash(x)` is set to `m * invmod(n, P) % P`, with `invmod(n, P)` supplying the inverse of `n` modulo `P`.

- When `x = m / n` is a nonnegative rational number whose `n` is divisible by `P` (though `m` is not), then `n` lacks any inverse modulo `P` and the previous rule fails to apply; here `hash(x)` is fixed at the constant value `sys.hash_info.inf`.

- When `x = m / n` is a negative rational number, set `hash(x)` to `-hash(-x)`. Should the resulting hash come out as `-1`, swap in `-2` instead.

- The two specific values `sys.hash_info.inf` and `-sys.hash_info.inf` serve as the hashes of positive infinity and negative infinity (in that order).

- For a [`complex`](https://docs.python.org/3.14/library/functions.html#complex) number `z`, the hashes of the real and imaginary components are merged by evaluating `hash(z.real) + sys.hash_info.imag * hash(z.imag)`, then reducing that modulo `2**sys.hash_info.width` so the outcome falls within `range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1))`. Once more, should the result equal `-1`, it becomes `-2`.

To make the above rules concrete, the following sample Python code mirrors the built-in hash and computes the hash of a rational number, [`float`](https://docs.python.org/3.14/library/functions.html#float), or [`complex`](https://docs.python.org/3.14/library/functions.html#complex):

```python
import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value

```

[Subject index](INDEX.md) · [Continue](boolean-type-bool.md)

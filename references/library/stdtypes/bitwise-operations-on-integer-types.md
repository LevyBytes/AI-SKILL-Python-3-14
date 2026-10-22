# Bitwise Operations on Integer Types

### Bitwise Operations on Integer Types

Only integers make bitwise operations meaningful. Their results are computed as if performed in two’s complement using an unbounded number of sign bits.

Every binary bitwise operation ranks below the numeric operations in priority and above the comparisons; the unary `~` operation shares the priority of the rest of the unary numeric operations (`+` and `-`).

The bitwise operations are listed below in ascending order of priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x | y` | bitwise *or* of *x* and *y* | (4) |
| `x ^ y` | bitwise *exclusive or* of *x* and *y* | (4) |
| `x & y` | bitwise *and* of *x* and *y* | (4) |
| `x << n` | *x* shifted left by *n* bits | (1)(2) |
| `x >> n` | *x* shifted right by *n* bits | (1)(3) |
| `~x` | the bits of *x* inverted |  |

Notes:

1.

Shift counts that are negative are not allowed and raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

2.

Shifting left by *n* bits amounts to multiplying by `pow(2, n)`.

3.

Shifting right by *n* bits amounts to floor division by `pow(2, n)`.

4.

Carrying out these calculations with no fewer than one additional sign extension bit inside a finite two’s complement representation (that is, a working bit-width of `1 + max(x.bit_length(), y.bit_length())` or greater) is enough to reach the same result you would get with an infinite supply of sign bits.

[Subject index](INDEX.md) · [Previous](numeric-types-int-float-complex.md) · [Continue](int-bit-length-to-int-bit-count.md)

# math — Number-theoretic functions

### Number-theoretic functions

 math.comb(*n*, *k*)

Give back how many distinct selections of *k* items can be drawn from *n* items when order is irrelevant and no item repeats.

The value is `n! / (k! * (n - k)!)` whenever `k <= n`, and it is zero whenever `k > n`.

The name binomial coefficient also applies, since it equals the coefficient on the k-th term once you expand the polynomial `(1 + x)ⁿ`.

A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results when either argument is not an integer. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results when either argument is negative.

Added in version 3.8.

 math.factorial(*n*)

Give back the factorial of the nonnegative integer *n*.

Changed in version 3.10: Integral-valued floats (such as `5.0`) are no longer accepted as input.

 math.gcd(**integers*)

Give back the greatest common divisor across the integer arguments supplied. When at least one argument is nonzero, the result is the biggest positive integer dividing every argument evenly. When every argument equals zero, the result is `0`. Invoking `gcd()` with no arguments yields `0`.

Added in version 3.5.

Changed in version 3.9: Gained the ability to take any count of arguments. Previously the call accepted only two.

 math.isqrt(*n*)

Give back the integer square root for the nonnegative integer *n*. That is the floor of the exact square root of *n*, equivalently the greatest integer *a* for which *a*² ≤ *n*.

Certain applications find it handier to obtain the least integer *a* satisfying *n* ≤ *a*², that is, the ceiling of the exact square root of *n*. For positive *n*, compute it via `a = 1 + isqrt(n - 1)`.

Added in version 3.8.

 math.lcm(**integers*)

Give back the least common multiple across the integer arguments supplied. When every argument is nonzero, the result is the smallest positive integer that all arguments divide. When any argument equals zero, the result is `0`. Invoking `lcm()` with no arguments yields `1`.

Added in version 3.9.

 math.perm(*n*, *k=None*)

Give back how many distinct selections of *k* items can be drawn from *n* items when order matters and no item repeats.

The value is `n! / (n - k)!` whenever `k <= n`, and it is zero whenever `k > n`.

When *k* is left out or passed as `None`, it falls back to *n*, so the function yields `n!`.

A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) results when either argument is not an integer. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results when either argument is negative.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](math-mathematical-functions.md) · [Continue](math-ceil-to-math-trunc.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)

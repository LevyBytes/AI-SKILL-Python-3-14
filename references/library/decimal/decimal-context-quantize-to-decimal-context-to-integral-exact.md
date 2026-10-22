# decimal.Context: `quantize()`, `radix()`, `remainder()`, `remainder_near()`, `rotate()`, `same_quantum()`, `scaleb()`, `shift()`, `sqrt()`, `subtract()`, `to_eng_string()`, `to_integral_exact()`

When supplied two arguments, this computes `x**y`. A negative `x` requires that `y` be integral. Unless `y` is integral and the outcome is finite and exactly representable within ‘precision’ digits, the answer is inexact. Rounding follows the context's rounding mode. The Python implementation always rounds results correctly.

The expression `Decimal(0) ** Decimal(0)` produces `InvalidOperation`, and when `InvalidOperation` goes untrapped, it then produces `Decimal('NaN')`.

Changed in version 3.3: Within the C module, `power()` is derived from the correctly rounded `exp()` and `ln()` functions. While the outcome is well-defined, it is only “almost always correctly rounded”.

Supplying three arguments computes `(x**y) % modulo`. This three-argument variant imposes the following constraints on its arguments:

- every one of the three arguments must be integral

- `y` must be nonnegative

- at least one of `x` or `y` must be nonzero

- `modulo` must be nonzero and have at most ‘precision’ digits

What `Context.power(x, y, modulo)` produces matches the value you would get by evaluating `(x**y) % modulo` at unbounded precision, yet it arrives there more efficiently. No matter what exponents `x`, `y` and `modulo` carry, the result's exponent is zero. The outcome is always exact.

 quantize(*x*, *y*, */*)

Yields a value matching *x* (after rounding) but carrying the exponent of *y*.

 radix()

Simply returns 10, since this is Decimal, :)

 remainder(*x*, *y*, */*)

Yields the remainder left over from integer division.

When the result is non-zero, its sign matches that of the original dividend.

 remainder_near(*x*, *y*, */*)

Yields `x - y * n`, in which *n* is the integer closest to the true value of `x / y` (and if the outcome is 0, its sign matches the sign of *x*).

 rotate(*x*, *y*, */*)

Yields a rotated copy of *x*, shifted around *y* times.

 same_quantum(*x*, *y*, */*)

Yields `True` when both operands share an identical exponent.

 scaleb(*x*, *y*, */*)

Yields the first operand once the second value has been added to its exp.

 shift(*x*, *y*, */*)

Yields a shifted copy of *x*, moved *y* times.

 sqrt(*x*, */*)

Square root of a non-negative number computed to context precision.

 subtract(*x*, *y*, */*)

Return the difference between *x* and *y*.

 to_eng_string(*x*, */*)

Convert into a string, employing engineering notation whenever an exponent is called for.

In engineering notation the exponent is always a multiple of 3. As a result, as many as 3 digits can sit left of the decimal point, and one or two trailing zeros may have to be appended.

 to_integral_exact(*x*, */*)

Rounds to an integer.

[Subject index](INDEX.md) · [Continue](decimal-context-to-sci-string.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Context](decimal-context-class-to-decimal-context-create-decimal.md) · [Owning module, declaration or section: Context objects](decimal-getcontext-to-decimal-defaultcontext.md) · [Owning module, declaration or section: power](decimal-context-min-mag-to-decimal-context-power.md) · [Preceding source contract and version conditions](decimal-context-min-mag-to-decimal-context-power.md)

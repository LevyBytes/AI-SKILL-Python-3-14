# decimal.Decimal: `is_subnormal()`, `is_zero()`, `ln()`, `log10()`, `logb()`, `logical_and()`, `logical_invert()`, `logical_or()`, `logical_xor()`, `max()`, `max_mag()`, `min()`, `min_mag()`, `next_minus()`, `next_plus()`, `next_toward()`, `normalize()`

Gives back [`True`](https://docs.python.org/3.14/library/constants.html#True) when the value is a signaling NaN; otherwise yields [`False`](https://docs.python.org/3.14/library/constants.html#False).

 is_subnormal(*context=None*)

Yields [`True`](https://docs.python.org/3.14/library/constants.html#True) when the value qualifies as subnormal, and [`False`](https://docs.python.org/3.14/library/constants.html#False) when it does not.

 is_zero()

Yields [`True`](https://docs.python.org/3.14/library/constants.html#True) when the value is a zero of either sign and [`False`](https://docs.python.org/3.14/library/constants.html#False) when it is not.

 ln(*context=None*)

Computes the natural (base e) logarithm of the operand. Its result is correctly rounded under the `ROUND_HALF_EVEN` rounding mode.

 log10(*context=None*)

Computes the base ten logarithm of the operand. Its result is correctly rounded under the `ROUND_HALF_EVEN` rounding mode.

 logb(*context=None*)

When the value is nonzero, yield its operand's adjusted exponent as a `Decimal` instance. Should the operand be a zero, `Decimal('-Infinity')` comes back and the `DivisionByZero` flag fires. Should the operand be an infinity, `Decimal('Infinity')` comes back.

 logical_and(*other*, *context=None*)

`logical_and()` performs a logical operation that accepts two *logical operands* (see Logical operands). What you get is the digit-wise `and` across both operands.

 logical_invert(*context=None*)

`logical_invert()` performs a logical operation. What you get is the digit-wise inversion of the operand.

 logical_or(*other*, *context=None*)

`logical_or()` performs a logical operation that accepts two *logical operands* (see Logical operands). What you get is the digit-wise `or` across both operands.

 logical_xor(*other*, *context=None*)

`logical_xor()` performs a logical operation that accepts two *logical operands* (see Logical operands). What you get is the digit-wise exclusive or across both operands.

 max(*other*, *context=None*)

Behaves like `max(self, other)`, with two differences: the context rounding rule fires before the value comes back, and `NaN` values get either signaled or skipped (which one depends on the context and on whether each is signaling or quiet).

 max_mag(*other*, *context=None*)

Works like the `max()` method, except the comparison relies on the absolute values of the operands.

 min(*other*, *context=None*)

Behaves like `min(self, other)`, with two differences: the context rounding rule fires before the value comes back, and `NaN` values get either signaled or skipped (which one depends on the context and on whether each is signaling or quiet).

 min_mag(*other*, *context=None*)

Works like the `min()` method, except the comparison relies on the absolute values of the operands.

 next_minus(*context=None*)

Yield the largest number that the supplied context permits (or, absent a context, the active thread's context) which is still smaller than the given operand.

 next_plus(*context=None*)

Yield the smallest number that the supplied context permits (or, absent a context, the active thread's context) which is still larger than the given operand.

 next_toward(*other*, *context=None*)

When the two operands differ, yield whichever number lies closest to the first operand while heading toward the second operand. When the operands are numerically equal, yield a copy of the first operand whose sign matches the sign of the second operand.

 normalize(*context=None*)

Serves to produce canonical values for an equivalence class, working either within the current context or within the context you supply.

The semantics match the unary plus operation, with one exception: when the final result is finite it gets pared down to its simplest form, stripping every trailing zero while keeping its sign. Concretely, for as long as the coefficient stays nonzero while still being divisible by ten, that coefficient is halved-down by a factor of ten and 1 is added to the exponent. In the remaining case (a zero coefficient) the exponent becomes 0. Across every case the sign stays the same.

To illustrate, `Decimal('32.100')` and `Decimal('0.321000e+2')` each normalize down to the equivalent value `Decimal('32.1')`.

Keep in mind that rounding happens *before* the reduction to simplest form.

Recent revisions of the specification also refer to this operation as `reduce`.

[Subject index](INDEX.md) · [Continue](decimal-construction-arithmetic-and-remainders.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md) · [Owning module, declaration or section: is_snan](decimal-decimal-is-infinite-to-decimal-decimal-is-snan.md) · [Preceding source contract and version conditions](decimal-decimal-is-infinite-to-decimal-decimal-is-snan.md)

# decimal - Special values

### Special values

The numeric system behind the `decimal` module offers special values such as `NaN`, `sNaN`, `-Infinity`, `Infinity`, plus the pair of zeros, `+0` and `-0`.

Infinities may be built directly with: `Decimal('Infinity')`. They can equally emerge from dividing by zero while the `DivisionByZero` signal stays untrapped. In the same way, when the `Overflow` signal is untrapped, infinity can come from rounding past the bounds of the largest representable number.

The infinities carry a sign (affine) and serve in arithmetic operations, where they behave like very large, indeterminate numbers. Adding a constant to infinity, for instance, yields yet another infinite result.

Certain operations are indeterminate and yield `NaN`, or raise an exception if the `InvalidOperation` signal is trapped. As an example, `0/0` yields `NaN`, standing for “not a number”. This kind of `NaN` is quiet and, having been produced, will pass through later computations always producing another `NaN`. Such behavior comes in handy for a chain of computations that now and then lack inputs — it lets the calculation continue while marking particular results as invalid.

There is also `sNaN`, which signals rather than staying quiet after each operation. It makes a useful return value when an invalid result has to halt a calculation for special handling.

How Python's comparison operators act can be somewhat surprising when a `NaN` takes part. An equality test where either operand is a quiet or signaling `NaN` always yields [`False`](https://docs.python.org/3.14/library/constants.html#False) (even for `Decimal('NaN')==Decimal('NaN')`), whereas an inequality test always yields [`True`](https://docs.python.org/3.14/library/constants.html#True). Trying to compare two Decimals with any of the `<`, `<=`, `>` or `>=` operators raises the `InvalidOperation` signal whenever either operand is a `NaN`, and returns `False` if that signal goes untrapped. Bear in mind that the General Decimal Arithmetic specification leaves the behavior of direct comparisons unspecified; these rules for comparisons that involve a `NaN` were drawn from the IEEE 854 standard (consult Table 3 in section 5.7). For strict standards-compliance, rely on the `compare()` and `compare_signal()` methods instead.

The signed zeros can come out of calculations that underflow. They retain the sign the calculation would have produced had it been done at greater precision. Because their magnitude is zero, positive and negative zeros alike are treated as equal and their sign is merely informational.

Beyond the two signed zeros that are distinct and yet equal, there exist several representations of zero differing in precision while sharing the same value. This takes some getting used to. To an eye trained on normalized floating-point representations, it is not at once obvious that the calculation below returns a value equal to zero:

```python
>>> 1 / Decimal('Infinity')
Decimal('0E-1000026')

```

[Subject index](INDEX.md) · [Previous](mitigating-round-off-error-with-increased-precision.md) · [Continue](working-with-threads.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)

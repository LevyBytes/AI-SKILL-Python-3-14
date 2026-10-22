# decimal: `decimal.FloatOperation`

*class *decimal.FloatOperation

Turn on stricter semantics for combining floats and Decimals.

When the signal goes untrapped (default), combining floats and Decimals is allowed within the `Decimal` constructor, `create_decimal()` and every comparison operator. Both conversion and comparisons stay exact. Each time a mixed operation happens it is quietly noted by setting `FloatOperation` among the context flags. Explicit conversions via `from_float()` or `create_decimal_from_float()` leave the flag untouched.

Otherwise (with the signal trapped), only equality comparisons and explicit conversions stay quiet. Every other mixed operation raises `FloatOperation`.

The table below outlines the signal hierarchy:

```python
exceptions.ArithmeticError(exceptions.Exception)
    DecimalException
        Clamped
        DivisionByZero(DecimalException, exceptions.ZeroDivisionError)
        Inexact
            Overflow(Inexact, Rounded)
            Underflow(Inexact, Rounded, Subnormal)
        InvalidOperation
        Rounded
        Subnormal
        FloatOperation(DecimalException, exceptions.TypeError)

```

[Subject index](INDEX.md) · [Previous](decimal-underflow-class.md) · [Continue](mitigating-round-off-error-with-increased-precision.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Signals](decimal-clamped-class.md)

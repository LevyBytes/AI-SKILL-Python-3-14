# decimal: `decimal.DivisionByZero`

*class *decimal.DivisionByZero

Signals dividing a non-infinite number by zero.

Can arise during division, modulo division, or when a number is raised to a negative power. Should this signal go untrapped, it returns `Infinity` or `-Infinity` with the sign set by the calculation's inputs.

[Subject index](INDEX.md) · [Previous](decimal-decimalexception-class.md) · [Continue](decimal-inexact-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Signals](decimal-clamped-class.md)

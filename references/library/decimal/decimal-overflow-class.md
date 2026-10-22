# decimal: `decimal.Overflow`

*class *decimal.Overflow

Numerical overflow.

Reports that after rounding the exponent exceeds `Context.Emax`. When untrapped, the result hinges on the rounding mode, either drawing inward to the largest representable finite number or rounding outward to `Infinity`. Either way, `Inexact` and `Rounded` are signaled too.

[Subject index](INDEX.md) · [Previous](decimal-invalidoperation-class.md) · [Continue](decimal-rounded-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Signals](decimal-clamped-class.md)

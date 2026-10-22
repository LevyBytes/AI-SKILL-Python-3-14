# decimal: `decimal.Rounded`

*class *decimal.Rounded

Rounding took place though possibly nothing was lost.

Signaled any time rounding drops digits; even when those digits are zero (for instance, rounding `5.00` to `5.0`). When untrapped, returns the result unchanged. This signal serves to detect the loss of significant digits.

[Subject index](INDEX.md) · [Previous](decimal-overflow-class.md) · [Continue](decimal-subnormal-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Signals](decimal-clamped-class.md)

# decimal: `decimal.InvalidOperation`

*class *decimal.InvalidOperation

An invalid operation was carried out.

Reports that an operation was asked for that does not make sense. When untrapped, returns `NaN`. Among the possible causes:

```python
Infinity - Infinity
0 * Infinity
Infinity / Infinity
x % 0
Infinity % x
sqrt(-x) and x > 0
0 ** 0
x ** (non-integer)
x ** Infinity

```

[Subject index](INDEX.md) · [Previous](decimal-inexact-class.md) · [Continue](decimal-overflow-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Signals](decimal-clamped-class.md)

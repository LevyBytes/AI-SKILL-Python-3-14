# decimal: `decimal.Clamped`

### Signals

Signals stand for conditions that surface in the course of computation. Each maps to one context flag plus one context trap enabler.

Whenever the condition arises, the context flag gets set. Once the computation finishes, flags can be inspected for informational reasons (for example, to learn whether a computation came out exact). Having checked the flags, remember to clear them all before the next computation begins.

Should the context's trap enabler be active for the signal, the condition triggers a raised Python exception. As an example, when the `DivisionByZero` trap is active, meeting the condition raises a `DivisionByZero` exception.

 *class *decimal.Clamped

Adjusted an exponent so it would fit representation constraints.

Clamping generally happens when an exponent lands beyond the context's `Emin` and `Emax` limits. Where feasible, the exponent is shrunk to fit by appending zeros to the coefficient.

[Subject index](INDEX.md) · [Previous](decimal-round-ceiling-to-decimal-round-05up.md) · [Continue](decimal-decimalexception-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)

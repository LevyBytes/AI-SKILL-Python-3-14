# 6.1. Arithmetic conversions

### 6.1. Arithmetic conversions

Several arithmetic operators below are described with the wording ?the numeric arguments are converted to a common real type?. That phrase signals that, for the built-in numeric types, the operator behaves as laid out in the [Numeric Types](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) part of the standard library documentation.

Certain operators paired with non-numeric operands follow extra rules as well ? consider, for instance, a string supplied as the left-hand argument to the `%` operator. Extensions are responsible for specifying how their own conversions work.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](expressions.md) · [Following source section](atoms.md)

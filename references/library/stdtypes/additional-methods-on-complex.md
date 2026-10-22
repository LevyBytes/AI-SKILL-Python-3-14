# Additional Methods on Complex

### Additional Methods on Complex

The `complex` type implements the [`numbers.Complex`](https://docs.python.org/3.14/library/numbers.html#numbers.Complex) [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class). `complex` carries the following extra methods as well.

 *classmethod *complex.from_number(*x*)

A class method to turn a number into a complex number.

When `x` is some general Python object, `complex.from_number(x)` defers to `x.__complex__()`. Where [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) is missing, it falls back on [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__). Where `__float__()` is missing too, it falls back on [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](float-as-integer-ratio-to-float-hex.md) · [Continue](hashing-of-numeric-types.md)

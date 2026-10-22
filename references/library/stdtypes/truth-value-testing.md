# Truth Value Testing

### Truth Value Testing

Every object may be evaluated for its truth value, whether inside an [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) or [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) condition or as an operand of the Boolean operations described below.

An object counts as true by default, unless its class supplies either a [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__) method returning `False` or a [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) method returning zero when invoked on the object. [1] Should either method raise an exception when invoked, that exception propagates and the object is left without a truth value (such as [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented)). The built-in objects treated as false are mostly these:

- constants defined to be false: `None` and `False`

- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`

- empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

Whenever an operation or built-in function yields a Boolean result, it returns `0` or `False` for false and `1` or `True` for true, except where noted otherwise. (One key exception: the Boolean operations `or` and `and` always hand back one of their operands.)

[Subject index](INDEX.md) · [Previous](built-in-types.md) · [Continue](boolean-operations-and-or-not.md)

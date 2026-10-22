# operator: Arithmetic, bitwise and unary operator functions

`operator.add(*a*, *b*)`

 `operator.__add__(*a*, *b*)`

Return `a + b`, for *a* and *b* numbers.

 `operator.and_(*a*, *b*)`

 `operator.__and__(*a*, *b*)`

Return `a & b`.

 `operator.floordiv(*a*, *b*)`

 `operator.__floordiv__(*a*, *b*)`

Return `a // b`.

 `operator.index(*a*)`

 `operator.__index__(*a*)`

Give back *a* turned into an integer. The same as `a.__index__()`.

Changed in version 3.10: From now on the result is always of exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). Before this, what came back might have been an instance of some `int` subclass.

 `operator.inv(*obj*)`

 `operator.invert(*obj*)`

 `operator.__inv__(*obj*)`

 `operator.__invert__(*obj*)`

Return `~obj`.

 `operator.lshift(*a*, *b*)`

 `operator.__lshift__(*a*, *b*)`

Return `a << b`.

 `operator.mod(*a*, *b*)`

 `operator.__mod__(*a*, *b*)`

Return `a % b`.

 `operator.mul(*a*, *b*)`

 `operator.__mul__(*a*, *b*)`

Return `a * b`.

 `operator.matmul(*a*, *b*)`

 `operator.__matmul__(*a*, *b*)`

Return `a @ b`.

Added in version 3.5.

 `operator.neg(*obj*)`

 `operator.__neg__(*obj*)`

Return *obj* negated (`-obj`).

 `operator.or_(*a*, *b*)`

 `operator.__or__(*a*, *b*)`

Return `a | b`.

 `operator.pos(*obj*)`

 `operator.__pos__(*obj*)`

Return `+obj`.

[Subject index](INDEX.md) · [Previous](operator-lt-to-operator-abs.md) · [Continue](operator-pow-to-operator-length-hint.md) · [Owning module, declaration or section: operator](operator-lt-to-operator-abs.md)

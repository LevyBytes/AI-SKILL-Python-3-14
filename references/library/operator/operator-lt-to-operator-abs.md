# operator: Comparison, truth and identity operator functions

# Operator

### `operator` - Standard operators as functions

**Source code:** [Lib/operator.py](https://github.com/python/cpython/tree/3.14/Lib/operator.py)

---

A collection of fast functions that mirror Python's built-in operators is provided by the `operator` module. To take one case, `operator.add(x, y)` behaves the same as writing the expression `x+y`. A lot of these functions carry the names of special methods minus the leading and trailing double underscores. To stay compatible with older code, a number of them also keep a double-underscore variant. For readability, reach for the versions that omit the double underscores.

You can sort the functions by what they do: comparing objects, performing logical work, handling math, and operating on sequences.

Every object can make use of the object-comparison functions, which take their names from the rich comparison operators they correspond to:

 `operator.lt(*a*, *b*)`

 `operator.le(*a*, *b*)`

 `operator.eq(*a*, *b*)`

 `operator.ne(*a*, *b*)`

 `operator.ge(*a*, *b*)`

 `operator.gt(*a*, *b*)`

 `operator.__lt__(*a*, *b*)`

 `operator.__le__(*a*, *b*)`

 `operator.__eq__(*a*, *b*)`

 `operator.__ne__(*a*, *b*)`

 `operator.__ge__(*a*, *b*)`

 `operator.__gt__(*a*, *b*)`

Carry out “rich comparisons” of *a* against *b*. In concrete terms, `lt(a, b)` matches `a < b`, while `le(a, b)` stands for `a <= b`; likewise `eq(a, b)` corresponds to `a == b`, `ne(a, b)` maps to `a != b`, `gt(a, b)` means `a > b`, and finally `ge(a, b)` denotes `a >= b`. Keep in mind that any value at all may come back from these functions, and it need not be something you can read as a Boolean. Further detail on rich comparisons lives at [Comparisons](https://docs.python.org/3.14/reference/expressions.html#comparisons).

The logical functions, too, apply broadly to any object, covering truth tests, identity tests, and boolean operations:

 `operator.not_(*obj*)`

 `operator.__not__(*obj*)`

Give back the result of [`not`](https://docs.python.org/3.14/reference/expressions.html#not) *obj*. (Be aware that object instances carry no `__not__()` method; this operation is defined solely within the interpreter core. Its outcome is shaped by the [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__) and [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) methods.)

 `operator.truth(*obj*)`

Hand back [`True`](https://docs.python.org/3.14/library/constants.html#True) when *obj* is true, otherwise [`False`](https://docs.python.org/3.14/library/constants.html#False). The effect matches calling the [`bool`](https://docs.python.org/3.14/library/functions.html#bool) constructor.

 `operator.is_(*a*, *b*)`

Return `a is b`. Tests object identity.

 `operator.is_not(*a*, *b*)`

Return `a is not b`. Tests object identity.

 `operator.is_none(*a*)`

Return `a is None`. Tests object identity.

Added in version 3.14.

 `operator.is_not_none(*a*)`

Return `a is not None`. Tests object identity.

Added in version 3.14.

The mathematical and bitwise operations are the most numerous:

 `operator.abs(*obj*)`

 `operator.__abs__(*obj*)`

Return the absolute value of *obj*.

[Subject index](INDEX.md) · [Continue](operator-add-to-operator-pos.md)

# Comparisons

### Comparisons

Python provides eight comparison operations. Every one of them shares a single priority (set above that of the Boolean operations). You can chain comparisons however you like; `x < y <= z`, for example, means the same as `x < y and y <= z`, with the difference that *y* is evaluated just once (in either case, though, *z* goes unevaluated entirely once `x < y` turns out false).

The comparison operations are summarized in this table:

| Operation | Meaning |
| --- | --- |
| `<` | strictly less than |
| `<=` | less than or equal |
| `>` | strictly greater than |
| `>=` | greater than or equal |
| `==` | equal |
| `!=` | not equal |
| `is` | object identity |
| `is not` | negated object identity |

Except where noted, objects belonging to distinct types never test as equal. While the `==` operator is always defined, for certain object types (class objects among them) it amounts to [`is`](https://docs.python.org/3.14/reference/expressions.html#is). The `<`, `<=`, `>` and `>=` operators apply only where they are meaningful; they raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception, for example, whenever one argument happens to be a complex number.

Two distinct instances of a class ordinarily test as unequal unless the class supplies the [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method.

You cannot order a class instance against other instances of the same class, nor against objects of other types, unless the class supplies an adequate set of the methods [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), [`__le__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__le__), [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__), and [`__ge__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ge__) (as a rule, `__lt__()` together with [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) suffices, assuming you want the comparison operators to carry their usual meanings).

There is no way to customize how the [`is`](https://docs.python.org/3.14/reference/expressions.html#is) and [`is not`](https://docs.python.org/3.14/reference/expressions.html#is-not) operators behave; moreover they work on any two objects whatsoever and never raise an exception.

A further pair of operations sharing this syntactic priority, [`in`](https://docs.python.org/3.14/reference/expressions.html#in) and [`not in`](https://docs.python.org/3.14/reference/expressions.html#not-in), is provided by types that are [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) or that implement the [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) method.

[Subject index](INDEX.md) · [Previous](boolean-operations-and-or-not.md) · [Continue](numeric-types-int-float-complex.md)

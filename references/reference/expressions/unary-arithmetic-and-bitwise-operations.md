# 6.6. Unary arithmetic and bitwise operations

### 6.6. Unary arithmetic and bitwise operations

Every unary arithmetic and bitwise operation shares the same priority:

```text

u_expr: power | "-" u_expr | "+" u_expr | "~" u_expr
```

The unary `-` (minus) operator produces the negation of its numeric argument; you can override the operation with the [`__neg__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__neg__) special method.

The unary `+` (plus) operator produces its numeric argument without alteration; you can override the operation with the [`__pos__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__pos__) special method.

The unary `~` (invert) operator produces, from its integer argument, that argument's bitwise inversion. For any `x`, this bitwise inversion is defined to be `-(x+1)`. It applies solely to integral numbers, or to custom objects that override the [`__invert__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__invert__) special method.

Across all three cases, when the argument lacks the proper type, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](the-power-operator.md) · [Following source section](binary-arithmetic-operations.md)

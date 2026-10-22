# 6.9. Binary bitwise operations

### 6.9. Binary bitwise operations

The three bitwise operations each sit at a distinct priority level:

```text

and_expr: shift_expr | and_expr "&" shift_expr
xor_expr: and_expr | xor_expr "^" and_expr
or_expr:  xor_expr | or_expr "|" xor_expr
```

The `&` operator produces the bitwise AND of its arguments, which have to be integers or else one of them has to be a custom object overriding the [`__and__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__and__) or [`__rand__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rand__) special methods.

The `^` operator produces the bitwise XOR (exclusive OR) of its arguments, which have to be integers or else one of them has to be a custom object overriding the [`__xor__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__xor__) or [`__rxor__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rxor__) special methods.

The `|` operator produces the bitwise (inclusive) OR of its arguments, which have to be integers or else one of them has to be a custom object overriding the [`__or__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__or__) or [`__ror__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ror__) special methods.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](shifting-operations.md) · [Following source section](comparisons.md)

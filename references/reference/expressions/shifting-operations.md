# 6.8. Shifting operations

### 6.8. Shifting operations

The shifting operations carry a lower priority than the arithmetic operations:

```text

shift_expr: a_expr | shift_expr ("<<" | ">>") a_expr
```

These operators take integers as their arguments. They move the first argument left or right by the count of bits supplied by the second argument.

You can customize the left shift operation through the special [`__lshift__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lshift__) and [`__rlshift__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rlshift__) methods. You can customize the right shift operation through the special [`__rshift__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rshift__) and [`__rrshift__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rrshift__) methods.

A right shift by *n* bits is defined to be floor division by `pow(2,n)`. A left shift by *n* bits is defined to be multiplication by `pow(2,n)`.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](binary-arithmetic-operations.md) · [Following source section](binary-bitwise-operations.md)

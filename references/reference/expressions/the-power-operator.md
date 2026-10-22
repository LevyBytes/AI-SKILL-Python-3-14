# 6.5. The power operator

### 6.5. The power operator

The power operator binds more tightly than the unary operators sitting on its left; it binds less tightly than the unary operators sitting on its right. Here is the syntax:

```text

power: (await_expr | primary) ["**" u_expr]
```

So, within an unparenthesized run of power and unary operators, evaluation of the operators proceeds from right to left (this places no restriction on the evaluation order of the operands): `-1**2` produces `-1`.

The power operator shares the same semantics as the two-argument form of the built-in [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) function: the left argument gets raised to the power given by the right one. Any numeric arguments are first [converted to a common type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic), and the result carries that type.

With int operands, the result shares the type of the operands unless the second argument is negative; in that situation, every argument is converted to float and a float result is produced. To illustrate, `10**2` returns `100`, whereas `10**-2` returns `0.01`.

Raising `0.0` to a negative power yields a [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError). Raising a negative number to a fractional power yields a [`complex`](https://docs.python.org/3.14/library/functions.html#complex) number. (Older versions raised a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) instead.)

You can customize this operation through the special [`__pow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__pow__) and [`__rpow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rpow__) methods.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](await-expression.md) · [Following source section](unary-arithmetic-and-bitwise-operations.md)

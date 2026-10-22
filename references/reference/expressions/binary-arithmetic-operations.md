# 6.7. Binary arithmetic operations

### 6.7. Binary arithmetic operations

The binary arithmetic operations follow the conventional priority levels. Be aware that a few of these operations apply to certain non-numeric types as well. Setting the power operator aside, there are merely two levels — one covering the multiplicative operators and one covering the additive operators:

```text

m_expr: u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
        m_expr "//" u_expr | m_expr "/" u_expr |
        m_expr "%" u_expr
a_expr: m_expr | a_expr "+" m_expr | a_expr "-" m_expr
```

The `*` (multiplication) operator produces the product of its arguments. Either both arguments must be numbers, or one argument must be an integer with the other being a sequence. In the first situation, the numbers get [converted to a common real type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) and then multiplied. In the second situation, sequence repetition takes place; a negative repetition factor produces an empty sequence.

You can customize this operation through the special [`__mul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__mul__) and [`__rmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rmul__) methods.

Changed in version 3.14: When only one operand is a complex number, the other operand gets converted to a floating-point number.

The `@` (at) operator is meant for matrix multiplication. None of the builtin Python types implement this operator.

You can customize this operation through the special [`__matmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__matmul__) and [`__rmatmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rmatmul__) methods.

Added in version 3.5.

The `/` (division) and `//` (floor division) operators produce the quotient of their arguments. The numeric arguments get [converted to a common type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) first. Dividing integers produces a float, whereas floor-dividing integers produces an integer; the result equals that of mathematical division with the ‘floor’ function applied to it. Dividing by zero raises the [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError) exception.

You can customize the division operation through the special [`__truediv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__truediv__) and [`__rtruediv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rtruediv__) methods. You can customize the floor division operation through the special [`__floordiv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__floordiv__) and [`__rfloordiv__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rfloordiv__) methods.

The `%` (modulo) operator produces the remainder from dividing the first argument by the second. The numeric arguments get [converted to a common type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) first. A right argument of zero raises the [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError) exception. The arguments are allowed to be floating-point numbers — for instance, `3.14%0.7` equals `0.34` (because `3.14` equals `4*0.7 + 0.34`.) The modulo operator always produces a result whose sign matches its second operand (or zero); the absolute value of the result stays strictly below the absolute value of the second operand [1].

The floor division and modulo operators relate through this identity: `x == (x//y)*y + (x%y)`. Floor division and modulo also relate to the built-in function [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod): `divmod(x, y) == (x//y, x%y)`. [2].

Beyond carrying out the modulo operation on numbers, the `%` operator is additionally overloaded by string objects to handle old-style string formatting (otherwise known as interpolation). The Python Library Reference covers the syntax for string formatting in section [printf-style String Formatting](https://docs.python.org/3.14/library/stdtypes.html#old-string-formatting).

You can customize the *modulo* operation through the special [`__mod__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__mod__) and [`__rmod__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rmod__) methods.

The floor division operator, the modulo operator, and the [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) function have no definition for complex numbers. Convert to a floating-point number with the [`abs()`](https://docs.python.org/3.14/library/functions.html#abs) function instead, where that is suitable.

The `+` (addition) operator produces the sum of its arguments. Either both arguments must be numbers, or both must be sequences of matching type. In the first situation, the numbers get [converted to a common real type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) and then added. In the second situation, the sequences get concatenated.

You can customize this operation through the special [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__) and [`__radd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__radd__) methods.

Changed in version 3.14: When only one operand is a complex number, the other operand gets converted to a floating-point number.

The `-` (subtraction) operator produces the difference of its arguments. The numeric arguments get [converted to a common real type](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-mixed-arithmetic) first.

You can customize this operation through the special [`__sub__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__sub__) and [`__rsub__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rsub__) methods.

Changed in version 3.14: When only one operand is a complex number, the other operand gets converted to a floating-point number.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](unary-arithmetic-and-bitwise-operations.md) · [Following source section](shifting-operations.md)

# 6.13. Conditional expressions

### 6.13. Conditional expressions

```text

conditional_expression: or_test ["if" or_test "else" expression]
expression:             conditional_expression | lambda_expr
```

A conditional expression (now and then named a “ternary operator”) offers a substitute for the if-else statement. Being an expression, it yields a value and is able to show up as a sub-expression.

In the expression `x if C else y`, the condition *C* is what gets evaluated first, ahead of *x*. When *C* is true, *x* is evaluated and its value returned; when not, *y* is evaluated and its value returned.

Turn to [**PEP 308**](https://peps.python.org/pep-0308/) for fuller detail on conditional expressions.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](assignment-expressions.md) · [Following source section](lambdas.md)

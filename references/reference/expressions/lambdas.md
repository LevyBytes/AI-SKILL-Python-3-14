# 6.14. Lambdas

### 6.14. Lambdas

```text

lambda_expr: "lambda" [parameter_list] ":" expression
```

Lambda expressions (occasionally referred to as lambda forms) serve to build anonymous functions. The expression `lambda parameters: expression` produces a function object. That nameless object acts just like a function object you would define with:

```none
def <lambda>(parameters):
    return expression

```

Refer to the [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) section for how parameter lists are spelled. Bear in mind that a function built from a lambda expression may hold neither statements nor annotations.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](conditional-expressions.md) · [Following source section](expression-lists.md)

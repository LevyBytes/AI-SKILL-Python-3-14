# 7.1. Expression statements

### 7.1. Expression statements

Expression statements serve (chiefly in interactive sessions) to compute and emit a value, or (more commonly) to invoke a procedure (a function whose return carries no meaningful result; Python procedures hand back the value `None`). Beyond those, expression statements have additional uses that are permitted and now and then handy. An expression statement obeys this grammar:

```text

expression_stmt: starred_expression
```

When an expression statement runs, it evaluates the expression list, which may consist of just one expression.

During interactive mode, when the value is not `None`, it gets turned into a string through the built-in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function, and that string is then written to standard output on its own line (the exception being a result of `None`, which keeps procedure calls from producing any output.)

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](simple-statements.md) · [Following source section](assignment-statements.md)

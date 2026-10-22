# Python 3.11.0 alpha 3 / core and builtins / python

[bpo-45764](https://bugs.python.org/issue?@action=redirect&bpo=45764): When the opening parenthesis `(` is omitted after a `def`-statement, the parser now reports a clearer error message:

```python
>>> def f:
  File "<stdin>", line 1
    def f:
         ^
SyntaxError: expected '('

```

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

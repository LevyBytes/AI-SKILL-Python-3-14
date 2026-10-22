# 6.12. Assignment expressions

### 6.12. Assignment expressions

```text

assignment_expression: [identifier ":="] expression
```

An assignment expression (also known at times as a “named expression” or “walrus”) binds an `expression` to an [`identifier`](https://docs.python.org/3.14/reference/lexical_analysis.html#grammar-token-python-grammar-identifier) and at the same time hands back the value of that `expression`.

A frequent application is dealing with matched regular expressions:

```python
if matching := pattern.search(data):
    do_something(matching)

```

Or else, while reading a file stream piece by piece:

```python
while chunk := file.read(9000):
    process(chunk)

```

You have to wrap assignment expressions in parentheses when they serve as expression statements and when they appear as sub-expressions inside slicing, conditional, lambda, keyword-argument, and comprehension-if expressions, as well as within `assert`, `with`, and `assignment` statements. Everywhere else they may be used, the parentheses are optional, `if` and `while` statements included.

Added in version 3.8: Consult [**PEP 572**](https://peps.python.org/pep-0572/) for fuller detail on assignment expressions.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](boolean-operations.md) · [Following source section](conditional-expressions.md)

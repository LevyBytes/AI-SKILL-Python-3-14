# What’s up with the comma operator’s precedence?

### What’s up with the comma operator’s precedence?

In Python, the comma isn't an operator at all. Take a look at this session:

```python
>>> "a" in "b", "a"
(False, 'a')

```

Because the comma serves to separate expressions rather than act as an operator, the line above is interpreted as though you had written:

```python
("a" in "b"), "a"

```

not:

```python
"a" in ("b", "a")

```

This holds for the assorted assignment operators as well (`=`, `+=`, and so on). Rather than being genuine operators, they function as syntactic delimiters within assignment statements.

[Subject index](INDEX.md)

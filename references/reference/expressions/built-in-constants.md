# 6.2.1. Built-in constants

### 6.2.1. Built-in constants

[Built-in constants](https://docs.python.org/3.14/library/constants.html#built-in-consts) are named by the keywords `True`, `False`, and `None`. The [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) constant is named by the token `...`.

When one of these atoms is evaluated, it produces the value it stands for.

Note

The interpreter exposes additional built-in constants through global variables, yet only the handful listed here count as [keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#keywords). As a consequence, you cannot rebind these particular names or treat them as attributes:

```pycon
>>> False = 123
  File "<input>", line 1
   False = 123
   ^^^^^
SyntaxError: cannot assign to False

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](atoms.md) · [Following source section](identifiers.md)

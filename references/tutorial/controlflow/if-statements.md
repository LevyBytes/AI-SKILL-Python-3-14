# 4.1. `if` Statements

### 4.1. `if` Statements

Probably the best-known kind of statement is the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement. Here is an example:

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More

```

You may include any number of [`elif`](https://docs.python.org/3.14/reference/compound_stmts.html#elif) sections (including none), and the [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) section may be omitted. Spelled ‘`elif`’, the keyword abbreviates ‘else if’ and helps cut down on deep indentation. A chain of `if` … `elif` … `elif` … takes the place of the `switch` or `case` constructs available elsewhere.

When you want to match one value against a number of constants, or to look for particular types or attributes, the `match` statement can come in handy too. Additional information appears under match Statements.

[Subject index](INDEX.md) · [Previous source section](more-control-flow-tools.md) · [Following source section](for-statements.md)

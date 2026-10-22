# 5.1.4. Nested List Comprehensions

### 5.1.4. Nested List Comprehensions

Whatever expression opens a list comprehension is free to be any arbitrary expression — even a second list comprehension.

Take this example of a 3x4 matrix realized as a list holding 3 lists, each of length 4:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

```

This list comprehension below swaps rows for columns:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```

Recall from the section before that the inner list comprehension gets evaluated within the scope of the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) trailing it, which makes this example amount to:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```

which is, in its own turn, identical to:

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```

When writing real code, lean on built-in functions rather than tangled flow statements. Here the [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) function handles this use case beautifully:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

```

Consult [Unpacking Argument Lists](https://docs.python.org/3.14/tutorial/controlflow.html#tut-unpacking-arguments) to learn what the asterisk on this line does.

[Subject index](INDEX.md) · [Previous source section](list-comprehension-filtering-and-flattening.md) · [Following source section](the-del-statement.md)

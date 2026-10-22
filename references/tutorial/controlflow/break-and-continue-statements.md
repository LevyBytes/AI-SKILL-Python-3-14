# 4.4. `break` and `continue` Statements

### 4.4. `break` and `continue` Statements

The [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) statement exits the nearest surrounding [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) loop:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(f"{n} equals {x} * {n//x}")
...             break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3

```

The [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement moves straight on to the loop’s following iteration:

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print(f"Found an even number {num}")
...         continue
...     print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9

```

[Subject index](INDEX.md) · [Previous source section](the-range-function.md) · [Following source section](else-clauses-on-loops.md)

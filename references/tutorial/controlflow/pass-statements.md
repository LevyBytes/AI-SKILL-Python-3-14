# 4.6. `pass` Statements

### 4.6. `pass` Statements

The [`pass`](https://docs.python.org/3.14/reference/simple_stmts.html#pass) statement carries out nothing at all. It comes in useful wherever the grammar demands a statement but you want no behavior to result. To illustrate:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...

```

A frequent application is to define bare-bones classes:

```python
>>> class MyEmptyClass:
...     pass
...

```

Yet another use for [`pass`](https://docs.python.org/3.14/reference/simple_stmts.html#pass) is as a stand-in for the body of a function or a conditional while drafting fresh code, which lets you go on reasoning at a higher level. The `pass` simply gets ignored:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...

```

In that final scenario, plenty of programmers reach for the ellipsis literal `...` rather than `pass`. Python attaches no particular meaning to this, and it doesn’t belong to the language specification (any constant expression would serve here), but `...` is the conventional pick for a placeholder body all the same. Refer to [The Ellipsis Object](https://docs.python.org/3.14/library/stdtypes.html#bltin-ellipsis-object).

[Subject index](INDEX.md) · [Previous source section](else-clauses-on-loops.md) · [Following source section](match-literals-or-patterns-and-tuple-captures.md)

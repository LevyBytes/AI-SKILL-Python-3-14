# Flag Members

### Flag Members

You can iterate over Flag members exactly as over the [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) class, and only the canonical members come back. For example:

```python
>>> list(Color)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]

```

(Note that `BLACK`, `PURPLE`, and `WHITE` do not show up.)

When a flag member is inverted, the result is the matching positive value instead of a negative one — for instance:

```python
>>> ~Color.RED
<Color.GREEN|BLUE: 6>

```

A Flag member’s length matches how many power-of-two values it holds. For example:

```python
>>> len(Color.PURPLE)
2

```

[Subject index](INDEX.md) · [Previous source context](enum-members.md) · [Following source context](enum-cookbook.md)

# Combining members of `Flag`

### Combining members of `Flag`

Looping over a combination of [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) members yields only those members made up of a single bit:

```python
>>> class Color(Flag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...     MAGENTA = RED | BLUE
...     YELLOW = RED | GREEN
...     CYAN = GREEN | BLUE
...
>>> Color(3)  # named combination
<Color.YELLOW: 3>
>>> Color(7)      # not named combination
<Color.RED|GREEN|BLUE: 7>

```

[Subject index](INDEX.md) · [Previous source context](enum-classes-with-methods.md) · [Following source context](intflag-color-setup-canonical-bits-and-pseudo-flag-names.md)

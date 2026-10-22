# IntFlag Color setup, canonical bits and pseudo-flag names

### `Flag` and `IntFlag` minutia

With the following snippet driving our examples:

```python
>>> class Color(IntFlag):
...     BLACK = 0
...     RED = 1
...     GREEN = 2
...     BLUE = 4
...     PURPLE = RED | BLUE
...     WHITE = RED | GREEN | BLUE
...

```

the statements below hold:

- single-bit flags are canonical

- multi-bit and zero-bit flags are aliases

- only canonical flags are returned during iteration:

```python
>>> list(Color.WHITE)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]

```

- applying negation to a flag, or to a flag set, hands back a fresh flag/flag set holding the matching positive integer value:

```python
>>> Color.BLUE
<Color.BLUE: 4>

>>> ~Color.BLUE
<Color.RED|GREEN: 3>

```

- names of pseudo-flags are constructed from their members’ names:

```python
>>> (Color.RED | Color.GREEN).name
'RED|GREEN'

>>> class Perm(IntFlag):
...     R = 4
...     W = 2
...     X = 1
...
>>> (Perm.R & Perm.W).name is None  # effectively Perm(0)
True

```

[Subject index](INDEX.md) · [Flag aliases and containment](flag-aliases-and-containment.md) · [STRICT, CONFORM, EJECT and KEEP boundary modes](strict-conform-eject-and-keep-boundary-modes.md) · [Previous source context](combining-members-of-flag.md) · [Following source context](flag-aliases-and-containment.md)

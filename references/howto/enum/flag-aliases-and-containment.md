# Flag aliases and containment

- multi-bit flags, aka aliases, can be returned from operations:

```python
>>> Color.RED | Color.BLUE
<Color.PURPLE: 5>

>>> Color(7)  # or Color(-1)
<Color.WHITE: 7>

>>> Color(0)
<Color.BLACK: 0>

```

- membership / containment checking: zero-valued flags are always considered to be contained:

```python
>>> Color.BLACK in Color.WHITE
True

```

otherwise, True comes back only when every bit of the first flag also sits inside the second flag:

```python
>>> Color.PURPLE in Color.WHITE
True

>>> Color.GREEN in Color.PURPLE
False

```

[Subject index](INDEX.md) · [IntFlag Color setup, canonical bits and pseudo-flag names](intflag-color-setup-canonical-bits-and-pseudo-flag-names.md) · [STRICT, CONFORM, EJECT and KEEP boundary modes](strict-conform-eject-and-keep-boundary-modes.md) · [Previous source context](intflag-color-setup-canonical-bits-and-pseudo-flag-names.md) · [Following source context](strict-conform-eject-and-keep-boundary-modes.md)

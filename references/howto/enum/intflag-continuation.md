# IntFlag continuation

Since [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) members are simultaneously instances of [`int`](https://docs.python.org/3.14/library/functions.html#int), you may mix them together (though doing so can drop their `IntFlag` membership:

```python
>>> Perm.X | 4
<Perm.R|X: 5>

>>> Perm.X + 8
9

```

Note

Applying the negation operator, `~`, will always yield an [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) member carrying a positive value:

```python
>>> (~Perm.X).value == (Perm.R|Perm.W).value == 6
True

```

You can likewise iterate across [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) members:

```python
>>> list(RW)
[<Perm.R: 4>, <Perm.W: 2>]

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source owning section](intflag.md) · [Following source context](flag.md)

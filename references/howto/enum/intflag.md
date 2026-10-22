# IntFlag

### IntFlag

The following [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) variant, [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag), likewise rests on [`int`](https://docs.python.org/3.14/library/functions.html#int). What sets it apart is that `IntFlag` members can be joined through the bitwise operators (&, |, ^, ~), and where possible the outcome stays an `IntFlag` member. As with [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum), `IntFlag` members count as integers too and serve anywhere an `int` would.

Note

Performing any operation other than the bit-wise ones on an [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) member drops the `IntFlag` membership.

Should a bit-wise operation produce an invalid [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) value, the `IntFlag` membership is lost. Consult [`FlagBoundary`](https://docs.python.org/3.14/library/enum.html#enum.FlagBoundary) for the specifics.

Added in version 3.6.

Changed in version 3.11.

A sample [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) class:

```python
>>> from enum import IntFlag
>>> class Perm(IntFlag):
...     R = 4
...     W = 2
...     X = 1
...
>>> Perm.R | Perm.W
<Perm.R|W: 6>
>>> Perm.R + Perm.W
6
>>> RW = Perm.R | Perm.W
>>> Perm.R in RW
True

```

You can also give the combinations names:

```python
>>> class Perm(IntFlag):
...     R = 4
...     W = 2
...     X = 1
...     RWX = 7
...
>>> Perm.RWX
<Perm.RWX: 7>
>>> ~Perm.RWX
<Perm: 0>
>>> Perm(7)
<Perm.RWX: 7>

```

Note

Named combinations count as aliases. While aliases stay hidden during iteration, by-value lookups can still surface them.

Changed in version 3.11.

One more notable contrast between [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) and [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum): when no flags are turned on (the value being 0), the boolean evaluation comes out [`False`](https://docs.python.org/3.14/library/constants.html#False):

```python
>>> Perm.R & Perm.X
<Perm: 0>
>>> bool(Perm.R & Perm.X)
False

```

[Subject index](INDEX.md) · [Following source continuation](intflag-continuation.md) · [Previous source context](strenum.md)

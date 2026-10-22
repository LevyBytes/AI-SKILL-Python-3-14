# What's New In Python 3.6 / enum — enum

### enum

A pair of fresh enumeration base classes joined the [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module: [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) and [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag). You use either to declare constants that the bitwise operators can join together. (Contributed by Ethan Furman in [bpo-23591](https://bugs.python.org/issue?@action=redirect&bpo=23591).)

A good number of standard library modules were revised to adopt the [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) class for their constants.

The new [`enum.auto`](https://docs.python.org/3.14/library/enum.html#enum.auto) value lets you hand values to enum members on its own:

```python
>>> from enum import Enum, auto
>>> class Color(Enum):
...     red = auto()
...     blue = auto()
...     green = auto()
...
>>> list(Color)
[<Color.red: 1>, <Color.blue: 2>, <Color.green: 3>]

```

[Subject index](INDEX.md) · [Previous source section](encodings.md) · [Next source section](faulthandler.md) · [Release/subject declaration](summary-release-highlights.md)

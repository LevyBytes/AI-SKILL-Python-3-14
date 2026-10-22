# enum: `enum.FlagBoundary`

*class *enum.FlagBoundary

`FlagBoundary` governs the treatment of out-of-range values within `Flag` and the classes that derive from it.

 STRICT

Out-of-range values trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) to be raised. For `Flag` this is the default:

```python
>>> from enum import Flag, STRICT, auto
>>> class StrictFlag(Flag, boundary=STRICT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> StrictFlag(2**2 + 2**4)
Traceback (most recent call last):
...
ValueError: <flag 'StrictFlag'> invalid value 20
    given 0b0 10100
  allowed 0b0 00111

```

 CONFORM

Out-of-range values get their invalid bits stripped away, leaving behind a valid `Flag` value:

```python
>>> from enum import Flag, CONFORM, auto
>>> class ConformFlag(Flag, boundary=CONFORM):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> ConformFlag(2**2 + 2**4)
<ConformFlag.BLUE: 4>

```

 EJECT

Out-of-range values shed their `Flag` membership and fall back to [`int`](https://docs.python.org/3.14/library/functions.html#int).

```python
>>> from enum import Flag, EJECT, auto
>>> class EjectFlag(Flag, boundary=EJECT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> EjectFlag(2**2 + 2**4)
20

```

 KEEP

Out-of-range values are retained, and `Flag` membership is preserved as well. For `IntFlag` this serves as the default:

[Subject index](INDEX.md) · [Previous](enum-enumcheck-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md) · [Required continuation of the source contract](enum-flagboundary-keep-behavior-and-intflag-default.md)

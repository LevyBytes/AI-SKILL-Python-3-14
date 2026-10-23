# enum - enum.FlagBoundary KEEP behavior and IntFlag default

```python
>>> from enum import Flag, KEEP, auto
>>> class KeepFlag(Flag, boundary=KEEP):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> KeepFlag(2**2 + 2**4)
<KeepFlag.BLUE|16: 20>

```

Added in version 3.11.

[Subject index](INDEX.md) · [Continue](enum-enumdict-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.FlagBoundary KEEP behavior and IntFlag default](enum-flagboundary-class.md) · [Preceding source contract and version conditions](enum-flagboundary-class.md)

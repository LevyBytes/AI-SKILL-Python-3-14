# What’s New In Python 3.8 / inspect — inspect

> (Contributed by Terry J. Reedy in [bpo-37765](https://bugs.python.org/issue?@action=redirect&bpo=37765).)

### inspect

The [`inspect.getdoc()`](https://docs.python.org/3.14/library/inspect.html#inspect.getdoc) function can now locate docstrings for `__slots__` whenever that attribute is a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) whose values serve as docstrings. That brings documentation choices much like the ones already available for [`property()`](https://docs.python.org/3.14/library/functions.html#property), [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod), and [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod):

```python
class AudioClip:
    __slots__ = {'bit_rate': 'expressed in kilohertz to one decimal place',
                 'duration': 'in seconds, rounded up to an integer'}
    def __init__(self, bit_rate, duration):
        self.bit_rate = round(bit_rate / 1000.0, 1)
        self.duration = ceil(duration)

```

[Subject index](INDEX.md) · [Previous source section](idle-and-idlelib.md) · [Next source section](io.md) · [Release/subject declaration](assignment-expressions.md)

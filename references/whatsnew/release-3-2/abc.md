# What's New In Python 3.2 / abc - abc

### abc

Support for [`abstractclassmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractclassmethod) and [`abstractstaticmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractstaticmethod) has been added to the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module.

With these, you can declare an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) that mandates a specific [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) or [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) be supplied by subclasses:

```python
class Temperature(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def from_fahrenheit(cls, t):
        ...
    @abc.abstractclassmethod
    def from_celsius(cls, t):
        ...

```

(Patch submitted by Daniel Urban; [bpo-5867](https://bugs.python.org/issue?@action=redirect&bpo=5867).)

[Subject index](INDEX.md) · [Previous source section](math.md) · [Next source section](io.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

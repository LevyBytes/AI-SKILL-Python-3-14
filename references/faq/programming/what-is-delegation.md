# What is delegation?

### What is delegation?

Delegation is an object-oriented technique (also referred to as a design pattern). Imagine you hold an object `x` and want to alter how just one of its methods behaves. You can write a fresh class that supplies a new version of the one method you mean to change while forwarding every other method to `x`’s matching method.

Delegation is straightforward to build in Python. As an illustration, the class below behaves like a file yet uppercases every piece of data it is asked to write:

```python
class UpperOut:

    def __init__(self, outfile):
        self._outfile = outfile

    def write(self, s):
        self._outfile.write(s.upper())

    def __getattr__(self, name):
        return getattr(self._outfile, name)

```

In this case the `UpperOut` class overrides the `write()` method so the string argument is uppercased before the wrapped `self._outfile.write()` method runs. Every remaining method is forwarded to the wrapped `self._outfile` object. That forwarding is handled through the [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) method; see [the language reference](https://docs.python.org/3.14/reference/datamodel.html#attribute-access) for further detail on managing attribute access.

Keep in mind that broader scenarios can make delegation messier. If attributes need to be assigned and not just read, the class also has to supply a [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) method, and that has to be written with care. A bare-bones `__setattr__()` is approximately the following:

```python
class X:
    ...
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    ...

```

A lot of [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) implementations invoke `object.__setattr__()` to assign an attribute on self while avoiding endless recursion:

```python
class X:
    def __setattr__(self, name, value):
        # Custom logic here...
        object.__setattr__(self, name, value)

```

You could instead assign attributes by writing entries straight into [`self.__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__).

[Subject index](INDEX.md)

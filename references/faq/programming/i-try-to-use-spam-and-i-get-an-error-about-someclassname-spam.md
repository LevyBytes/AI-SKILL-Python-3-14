# I try to use __spam and I get an error about _SomeClassName__spam.

### I try to use __spam and I get an error about _SomeClassName__spam.

Names that begin with two underscores get “mangled”, a plain yet workable mechanism for declaring class-private variables. Whenever an identifier takes the form `__spam` (no fewer than two leading underscores and no more than one trailing underscore), it is replaced textually with `_classname__spam`, in which `classname` denotes the current class name once any leading underscores have been stripped.

Within the class you can write the identifier as-is, but reaching it from outside the class means spelling out the mangled name:

```python
class A:
    def __one(self):
        return 1
    def two(self):
        return 2 * self.__one()

class B(A):
    def three(self):
        return 3 * self._A__one()

four = 4 * A()._A__one()

```

Notably, this offers no real privacy, since someone outside can still reach the private attribute on purpose if they choose; plenty of Python programmers simply never use private variable names.

See also

The [private name mangling specifications](https://docs.python.org/3.14/reference/expressions.html#private-name-mangling) for details and special cases.

[Subject index](INDEX.md)

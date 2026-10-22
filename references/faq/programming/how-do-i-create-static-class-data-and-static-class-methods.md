# How do I create static class data and static class methods?

### How do I create static class data and static class methods?

Python supports both static data and static methods, in the C++ or Java sense.

To get static data, just declare a class attribute. Putting a fresh value into that attribute requires naming the class explicitly on the left-hand side:

```python
class C:
    count = 0   # number of times C.__init__ called

    def __init__(self):
        C.count = C.count + 1

    def getcount(self):
        return C.count  # or return self.count

```

For any `c` where `isinstance(c, C)` is true, `c.count` likewise resolves to `C.count`, unless `c` itself shadows it or some class along the base-class search path running from `c.__class__` up to `C` does.

Caution: inside a method of C, writing `self.count = 42` makes a brand-new and independent instance attribute called “count” living in `self`’s own dict. Reassigning a class-static data name must always name the class, both within methods and outside them:

```python
C.count = 314

```

Static methods are possible:

```python
class C:
    @staticmethod
    def static(arg1, arg2, arg3):
        # No 'self' parameter!
        ...

```

That said, a much simpler way to achieve a static method’s behaviour is an ordinary module-level function:

```python
def getcount():
    return C.count

```

When you arrange your code to put a single class (or a closely linked class hierarchy) in each module, this delivers the encapsulation you’re after.

[Subject index](INDEX.md)

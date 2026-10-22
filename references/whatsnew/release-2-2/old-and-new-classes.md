# What’s New in Python 2.2 / Old and New Classes

### Old and New Classes

To start, be aware that Python 2.2 genuinely ships two distinct flavours of class: the classic (or old-style) kind, and the new-style kind. How the old-style variety behaves matches precisely the class model from prior Python releases. Everything new covered in this section pertains solely to new-style classes. This split isn’t meant to be permanent; old-style classes will be retired down the line, perhaps with Python 3.0.

So what’s the recipe for a new-style class? You build one by subclassing some already-existing new-style class. The majority of Python’s built-in types — integers, lists, dictionaries, files and so on — are new-style classes by now. There’s also a new-style class called [`object`](https://docs.python.org/3.14/library/functions.html#object), which is the base for every built-in type, so when none of the built-in types fit, you can simply subclass `object`:

```python
class C(object):
    def __init__ (self):
        ...
    ...

```

What this implies is that any [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) statement lacking base classes is always a classic class under Python 2.2. (You can in fact alter that too, by assigning a module-level variable called `__metaclass__` — the specifics live in [**PEP 253**](https://peps.python.org/pep-0253/) — though it’s simpler to just subclass [`object`](https://docs.python.org/3.14/library/functions.html#object).)

Through a neat trick, the type objects belonging to the built-in types are exposed as built-ins themselves. Python has long carried built-in functions called [`int()`](https://docs.python.org/3.14/library/functions.html#int), [`float()`](https://docs.python.org/3.14/library/functions.html#float), and [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str). As of 2.2 they’re no longer functions but type objects that act as factories whenever they’re called.

```python
>>> int
<type 'int'>
>>> int('123')
123

```

So that the lineup of types is whole, fresh type objects like [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) and `file()` were introduced. Here’s a livelier illustration that tacks a `lock()` method onto file objects:

```python
class LockableFile(file):
    def lock (self, operation, length=0, start=0, whence=0):
        import fcntl
        return fcntl.lockf(self.fileno(), operation,
                           length, start, whence)

```

The now-deprecated `posixfile` module held a class that imitated every method of a file object and threw in a `lock()` method on top, but that class couldn’t be handed to internal functions expecting a built-in file — something our new `LockableFile` manages just fine.

[Subject index](INDEX.md) · [Previous source section](peps-252-and-253-type-and-class-changes.md) · [Next source section](descriptors.md) · [Release/subject declaration](introduction.md)

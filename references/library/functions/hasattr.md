# hasattr

hasattr(*object*, *name*, */*)

The arguments consist of an object and a string. The outcome is `True` when the string names one of the object's attributes, and `False` otherwise. (Under the hood this works by calling `getattr(object, name)` and checking whether an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) gets raised or not.)

[Builtin task index](INDEX.md).

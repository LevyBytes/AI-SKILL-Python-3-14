# issubclass

issubclass(*class*, *classinfo*, */*)

Return `True` when *class* is a subclass (direct, indirect, or [virtual](https://docs.python.org/3.14/glossary.html#term-abstract-base-class)) of *classinfo*. A class counts as a subclass of itself. *classinfo* may take the form of a tuple of class objects (or, recursively, further such tuples) or a [Union Type](https://docs.python.org/3.14/library/stdtypes.html#types-union), in which event return `True` when *class* is a subclass of any member of *classinfo*. In every other situation, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised.

Changed in version 3.10: *classinfo* can be a [Union Type](https://docs.python.org/3.14/library/stdtypes.html#types-union).

[Builtin task index](INDEX.md).

# isinstance

isinstance(*object*, *classinfo*, */*)

Return `True` whenever the *object* argument turns out to be an instance of the *classinfo* argument, or of any (direct, indirect, or [virtual](https://docs.python.org/3.14/glossary.html#term-abstract-base-class)) subclass of it. Should *object* fail to be an object of that type, the function invariably hands back `False`. When *classinfo* is a tuple of type objects (or, recursively, further such tuples) or a [Union Type](https://docs.python.org/3.14/library/stdtypes.html#types-union) made of multiple types, return `True` when *object* is an instance of any of those types. When *classinfo* is neither a type nor a tuple of types and such tuples, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception is raised. `TypeError` might not be raised for an invalid type when an earlier check passes.

Changed in version 3.10: *classinfo* can be a [Union Type](https://docs.python.org/3.14/library/stdtypes.html#types-union).

[Builtin task index](INDEX.md).

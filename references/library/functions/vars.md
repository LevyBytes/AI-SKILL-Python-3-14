# vars

vars()

 vars(*object*, */*)

Hand back the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute belonging to a module, class, instance, or any other object that owns a `__dict__` attribute.

Things like modules and instances carry an updateable [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute; other objects, by contrast, may restrict writes to their `__dict__` attributes (for instance, classes employ a [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) to block direct dictionary updates).

Call it with no argument and `vars()` behaves the way `locals()` does.

A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception gets raised if you name an object that lacks a [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute (for instance, when its class defines the [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) attribute).

Changed in version 3.13: What this function returns when invoked argument-free has changed, matching the revision documented for the `locals()` builtin.

[Builtin task index](INDEX.md).

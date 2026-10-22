# module.__getattr__() / module.__dir__()

#### 3.3.2.1. Customizing module attribute access

 module.__getattr__()

 module.__dir__()

The special names `__getattr__` and `__dir__` can likewise serve to tailor access to module attributes. A module-level `__getattr__` function should accept a single argument — an attribute’s name — then hand back the computed value or else raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). When an attribute goes unfound on a module object through the normal lookup, that is, `object.__getattribute__()`, then `__getattr__` is sought within the module `__dict__` before an `AttributeError` is raised. Once found, it is invoked with the attribute name and the result is given back.

The `__dir__` function should take no arguments and return an iterable of strings standing for the names reachable on the module. When present, this function supersedes the standard [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) search across a module.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](object-dir.md) · [Following source section](module-class.md)

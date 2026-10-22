# 3.3.3.4. Preparing the class namespace

#### 3.3.3.4. Preparing the class namespace

After the appropriate metaclass has been settled, the class namespace gets prepared. When the metaclass owns a `__prepare__` attribute, it is invoked as `namespace = metaclass.__prepare__(name, bases, **kwds)` (any extra keyword arguments come from the class definition). You should implement the `__prepare__` method as a [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod). Whatever namespace `__prepare__` returns is fed into `__new__`, though when the final class object is built that namespace is copied into a fresh `dict`.

When the metaclass lacks a `__prepare__` attribute, the class namespace simply starts out as an empty ordered mapping.

See also

[**PEP 3115**](https://peps.python.org/pep-3115/) - Metaclasses in Python 3000

Introduced the `__prepare__` namespace hook

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](determining-the-appropriate-metaclass.md) · [Following source section](executing-the-class-body.md)

# object.__get__(*self*, *instance*, *owner=None*)

object.__get__(*self*, *instance*, *owner=None*)

Invoked to retrieve, on the owner class, that class’s attribute (class attribute access) or, on one of its instances, the instance’s attribute (instance attribute access). The optional *owner* argument names the owner class, while *instance* refers to whatever instance routed the access, or `None` should the *owner* itself be the access route.

This method should give back the computed attribute value or raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) exception.

[**PEP 252**](https://peps.python.org/pep-0252/) lays out that you may call `__get__()` using either one argument or two. The built-in descriptors shipped with Python honor this specification; even so, some third-party tools probably have descriptors that demand both arguments. Python’s own `__getattribute__()` implementation always supplies both arguments whether or not they are required.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Owning language section](implementing-descriptors.md) · [Previous source section](implementing-descriptors.md) · [Following source section](object-set.md)

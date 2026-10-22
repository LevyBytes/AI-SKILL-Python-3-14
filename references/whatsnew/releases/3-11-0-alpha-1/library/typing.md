# Python 3.11.0 alpha 1 / library / typing

[bpo-44468](https://bugs.python.org/issue?@action=redirect&bpo=44468): [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) now locates annotations on classes and base classes carrying an unexpected `__module__`. Earlier such MRO entries were passed over.

[bpo-44801](https://bugs.python.org/issue?@action=redirect&bpo=44801): Guarantee that the [`ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) variable inside Callable can be replaced only by a parameters expression (a list of types, an ellipsis, ParamSpec, or Concatenate).

[bpo-44806](https://bugs.python.org/issue?@action=redirect&bpo=44806): Non-protocol subclasses of [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) now disregard the `__init__` method handed down from protocol base classes.

[bpo-44490](https://bugs.python.org/issue?@action=redirect&bpo=44490): [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) now looks for type parameters inside `types.Union` objects. Likewise, `get_type_hints` will correctly resolve annotations that contain nested `types.Union` objects. Yurii Karabas provided the patch.

[bpo-44098](https://bugs.python.org/issue?@action=redirect&bpo=44098): `typing.ParamSpec` will no longer turn up in the `__parameters__` of most [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) generics outside the valid usage spots laid out by [**PEP 612**](https://peps.python.org/pep-0612/). That blocks improper forms such as `typing.List[P][int]`. As a result, improper usage that may have slipped by quietly in 3.10 beta 1 and before will now error.

[bpo-45166](https://bugs.python.org/issue?@action=redirect&bpo=45166): [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) now handles a [`Final`](https://docs.python.org/3.14/library/typing.html#typing.Final) that sits inside a [`ForwardRef`](https://docs.python.org/3.14/library/typing.html#typing.ForwardRef).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

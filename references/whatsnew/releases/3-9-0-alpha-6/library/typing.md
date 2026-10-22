# Python 3.9.0 alpha 6 / library / typing

[bpo-40398](https://bugs.python.org/issue?@action=redirect&bpo=40398): When given special generic aliases, [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args) at this point always returns an empty tuple.

[bpo-40396](https://bugs.python.org/issue?@action=redirect&bpo=40396): The [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin), [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args) and [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) functions at this point cope with generic aliases such as `list[int]`.

[bpo-39942](https://bugs.python.org/issue?@action=redirect&bpo=39942): Within [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), use ?__main__? as the fallback module name whenever ?__name__? is absent. Weipeng Hong supplied the patch.

[bpo-40257](https://bugs.python.org/issue?@action=redirect&bpo=40257): Better help arrived for the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module. Docstrings at this point appear for every special form plus special generic alias (such as `Union` and `List`). Calling `help()` on a generic alias like `List[int]` will surface the help belonging to the matching concrete type (`list` here).

[bpo-40182](https://bugs.python.org/issue?@action=redirect&bpo=40182): The `_field_types` attribute on the [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class has been dropped.

[bpo-36517](https://bugs.python.org/issue?@action=redirect&bpo=36517): Combining [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) with multiple inheritance now triggers an error rather than quietly disregarding the additional types.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

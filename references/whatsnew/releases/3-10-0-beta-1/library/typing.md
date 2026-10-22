# Python 3.10.0 beta 1 / library / typing

[bpo-42904](https://bugs.python.org/issue?@action=redirect&bpo=42904): To stay compatible with earlier minor Python releases, when [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) is handed no namespace dictionary arguments, `typing.get_type_hints()` will look first through the global namespace and then the local one while evaluating stringized type annotations (string forward references) located inside a class.

[bpo-43766](https://bugs.python.org/issue?@action=redirect&bpo=43766): Realize [**PEP 647**](https://peps.python.org/pep-0647/) inside the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module by introducing `TypeGuard`.

[gh-47383](https://github.com/python/cpython/issues/47383): The `P.args` and `P.kwargs` attributes on [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) are now instances of two new classes, [`typing.ParamSpecArgs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecArgs) and [`typing.ParamSpecKwargs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecKwargs), which makes for a more helpful `repr()`. Jelle Zijlstra wrote the patch.

[bpo-42904](https://bugs.python.org/issue?@action=redirect&bpo=42904): When resolving [**PEP 563**](https://peps.python.org/pep-0563/) annotations written inside a class, [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) now consults that class's local namespace as well.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

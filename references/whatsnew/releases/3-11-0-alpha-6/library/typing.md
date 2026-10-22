# Python 3.11.0 alpha 6 / library / typing

[bpo-46676](https://bugs.python.org/issue?@action=redirect&bpo=46676): Have [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) args and kwargs compare equal to themselves. Gregory Beauregard wrote the patch.

[bpo-46655](https://bugs.python.org/issue?@action=redirect&bpo=46655): Inside [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints), allow bare stringified `TypeAlias` annotations to be evaluated. Gregory Beauregard wrote the patch.

[bpo-46571](https://bugs.python.org/issue?@action=redirect&bpo=46571): Sharpen [`typing.no_type_check()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check).

It now leaves outside classes and functions untouched. Classmethods also get correctly flagged as exempt from type checking.

[bpo-46534](https://bugs.python.org/issue?@action=redirect&bpo=46534): Deliver [**PEP 673**](https://peps.python.org/pep-0673/) [`typing.Self`](https://docs.python.org/3.14/library/typing.html#typing.Self). James Hilton-Balfe wrote the patch.

[bpo-46475](https://bugs.python.org/issue?@action=redirect&bpo=46475): Introduce [`typing.Never`](https://docs.python.org/3.14/library/typing.html#typing.Never) and [`typing.assert_never()`](https://docs.python.org/3.14/library/typing.html#typing.assert_never). Jelle Zijlstra wrote the patch.

[bpo-46333](https://bugs.python.org/issue?@action=redirect&bpo=46333): The `__eq__()` and `__hash__()` methods on [`typing.ForwardRef`](https://docs.python.org/3.14/library/typing.html#typing.ForwardRef) now respect the `module` parameter of `typing.ForwardRef`. Forward references originating in different modules are kept distinct from one another.

[bpo-46195](https://bugs.python.org/issue?@action=redirect&bpo=46195): [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) stops appending `Optional` onto parameters whose default is `None`. That matches the PEP 484 revisions in [https://github.com/python/peps/pull/689](https://github.com/python/peps/pull/689)

[bpo-46333](https://bugs.python.org/issue?@action=redirect&bpo=46333): The `__repr__()` method on [`typing.ForwardRef`](https://docs.python.org/3.14/library/typing.html#typing.ForwardRef) now folds in the `module` parameter of `typing.ForwardRef` whenever that has been assigned.

[bpo-46643](https://bugs.python.org/issue?@action=redirect&bpo=46643): Within [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints), allow stringified `ParamSpecArgs` and `ParamSpecKwargs` annotations to be evaluated. Gregory Beauregard wrote the patch.

[bpo-46066](https://bugs.python.org/issue?@action=redirect&bpo=46066): Mark the kwargs-based syntax for [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) definitions as deprecated. Its meaning around totality was muddled, and hardly anyone relied on it. Jingchen Ye wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

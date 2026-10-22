# Python 3.11.0 alpha 4 / library / typing

[bpo-46244](https://bugs.python.org/issue?@action=redirect&bpo=46244): Stripped `__slots__` out of [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) and [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), since they served no purpose. Arie Bovenberg wrote the patch.

[bpo-45755](https://bugs.python.org/issue?@action=redirect&bpo=45755): Passing a [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) generic alias to `dir()` now surfaces the class attributes belonging to the underlying generic class. That matched the behavior through Python 3.6 before it shifted across 3.7-3.9.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

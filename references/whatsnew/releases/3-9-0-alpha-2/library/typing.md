# Python 3.9.0 alpha 2 / library / typing

[bpo-37838](https://bugs.python.org/issue?@action=redirect&bpo=37838): [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) now deals correctly with functions wrapped via [`functools.wraps()`](https://docs.python.org/3.14/library/functools.html#functools.wraps).

[bpo-38834](https://bugs.python.org/issue?@action=redirect&bpo=38834): [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) subclasses now record which keys are optional by way of the `__required_keys__` and `__optional_keys__` attributes, so downstream projects can perform runtime validation. Zac Hatfield-Dodds wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 3 / library / dataclasses

[bpo-45663](https://bugs.python.org/issue?@action=redirect&bpo=45663): Correct [`dataclasses.is_dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.is_dataclass) for dataclasses that subclass [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias).

[bpo-45662](https://bugs.python.org/issue?@action=redirect&bpo=45662): Correct the repr produced by [`dataclasses.InitVar`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.InitVar) when paired with a type alias to the built-in class, such as `InitVar[list[int]]`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

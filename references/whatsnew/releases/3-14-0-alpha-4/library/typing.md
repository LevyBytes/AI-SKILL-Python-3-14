# Python 3.14.0 alpha 4 / library / typing

[gh-128661](https://github.com/python/cpython/issues/128661): Addresses [`typing.evaluate_forward_ref()`](https://docs.python.org/3.14/library/typing.html#typing.evaluate_forward_ref) failing to surface a deprecation whenever the `type_params` arg goes unsupplied.

[gh-88834](https://github.com/python/cpython/issues/88834): Brought the instance check for [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) and [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) into line: `Union` now runs instance checks against its parameters rather than subclass checks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

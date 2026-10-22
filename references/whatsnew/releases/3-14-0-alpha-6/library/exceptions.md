# Python 3.14.0 alpha 6 / library / exceptions

[gh-130164](https://github.com/python/cpython/issues/130164): Repairs a failure to raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) within [`inspect.Signature.bind()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.bind) when positional-only arguments arrive by keyword alongside a variadic keyword argument (e.g. `**kwargs`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

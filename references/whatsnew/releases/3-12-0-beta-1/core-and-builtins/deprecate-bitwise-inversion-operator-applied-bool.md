# Python 3.12.0 beta 1 / core and builtins / deprecate bitwise inversion operator applied bool

[gh-82012](https://github.com/python/cpython/issues/82012): Deprecate the bitwise inversion operator (`~`) when applied to bool. It yields the bitwise inversion of the underlying `int` representation, so that `bool(~True) == True`, which is potentially confusing. For logical negation of bools, prefer `not`. On the uncommon occasion you genuinely want the bitwise inversion of the underlying `int`, cast to int first via `~int(x)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

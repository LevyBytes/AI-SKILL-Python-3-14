# Python 3.10.0 alpha 1 / core and builtins / decimal

[bpo-37999](https://bugs.python.org/issue?@action=redirect&bpo=37999): Builtin and extension functions accepting integer arguments will no longer take [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)s, [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)s, or other objects convertible to integers only with a loss (for instance, those defining [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) yet lacking [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

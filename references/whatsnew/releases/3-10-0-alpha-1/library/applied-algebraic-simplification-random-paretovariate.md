# Python 3.10.0 alpha 1 / library / applied algebraic simplification random paretovariate

[bpo-41421](https://bugs.python.org/issue?@action=redirect&bpo=41421): Applied an algebraic simplification to random.paretovariate(). It is now a little less prone to round-off error and a touch faster. Inputs that previously triggered ZeroDivisionError now trigger an OverflowError instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

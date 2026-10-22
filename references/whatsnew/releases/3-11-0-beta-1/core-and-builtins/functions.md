# Python 3.11.0 beta 1 / core and builtins / functions

[bpo-46961](https://bugs.python.org/issue?@action=redirect&bpo=46961): Integer mod/remainder operations — including [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) in its three-argument form — now reliably hand back ints drawn from the global small integer cache whenever that applies.

[gh-91603](https://github.com/python/cpython/issues/91603): Make [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) tests faster for [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType). Yurii Karabas authored the patch.

[gh-92203](https://github.com/python/cpython/issues/92203): Introduce a closure keyword-only argument on [`exec()`](https://docs.python.org/3.14/library/functions.html#exec). Supplying it is only valid while exec-ing a code object that depends on free variables. If given, it has to be a tuple holding precisely as many cell variables as the code object refers to. The default for closure is `None`, and it is required to be `None` whenever the code object references no free variables.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

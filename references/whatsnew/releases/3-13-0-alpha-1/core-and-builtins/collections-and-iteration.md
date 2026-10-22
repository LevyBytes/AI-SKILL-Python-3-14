# Python 3.13.0 alpha 1 / core and builtins / collections and iteration

[gh-105162](https://github.com/python/cpython/issues/105162): Corrected a defect inside generator.close()/throw() whereby an inner iterator got skipped once the outer iterator carried instrumentation.

[gh-106485](https://github.com/python/cpython/issues/106485): Cut the count of materialized instance dictionaries by dematerializing them wherever feasible.

[gh-109371](https://github.com/python/cpython/issues/109371): Instructions were deopted properly for tool initialization, and the faulty assertion in instrumentation was changed for the case where an earlier tool has already set INSTRUCTION events

[gh-109118](https://github.com/python/cpython/issues/109118): Nested scopes (lambdas, generator expressions, and comprehensions) are now forbidden inside PEP 695 annotation scopes that themselves sit within classes.

[gh-110164](https://github.com/python/cpython/issues/110164): regrtest: When the `SOURCE_DATE_EPOCH` environment variable is set, test randomization is now switched off by regrtest. Victor Stinner authored the patch.

[gh-109853](https://github.com/python/cpython/issues/109853): For subinterpreters, `sys.path[0]` is now set as it should be.

[gh-105486](https://github.com/python/cpython/issues/105486): Alter how the `ParamSpec` args list reprs within `types.GenericAlias`.

[gh-104770](https://github.com/python/cpython/issues/104770): Should a generator yield a value at the time it is closed, that value is henceforth handed back by [`generator.close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close).

[gh-107263](https://github.com/python/cpython/issues/107263): The C recursion limit for functions besides the main interpreter was raised from 800 to 1500. With that, functions such as `list.__repr__` and `json.dumps` should manage every input they could before 3.12

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

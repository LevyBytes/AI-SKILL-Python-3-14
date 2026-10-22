# Python 3.11.0 alpha 2 / core and builtins / collections and iteration

[bpo-45530](https://bugs.python.org/issue?@action=redirect&bpo=45530): Sorting that relies on tuples for keys can become markedly quicker in certain situations. Tim Peters wrote the patch.

The ordering of the outcome can diverge from prior releases when the tuple elements lack a total ordering (consult [Value comparisons](https://docs.python.org/3.14/reference/expressions.html#expressions-value-comparisons) for details about total ordering). As a rule, what sorting produces simply isn’t well-defined when the list elements lack a total ordering.

[bpo-40116](https://bugs.python.org/issue?@action=redirect&bpo=40116): Revise how split dictionaries are implemented. Classes whose instances vary either in the precise set of attributes or in the sequence in which those attributes get assigned can still share keys. Users of Python or the C-API should notice no effect from this. Mark Shannon wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

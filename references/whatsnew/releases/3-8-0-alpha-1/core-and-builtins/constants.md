# Python 3.8.0 alpha 1 / core and builtins / constants

[bpo-34100](https://bugs.python.org/issue?@action=redirect&bpo=34100): The compiler now merges constants found within tuples and frozensets in a recursive manner. Code attributes such as `co_names` get merged as well.

[bpo-32925](https://bugs.python.org/issue?@action=redirect&bpo=32925): Made iteration and membership checks faster for literal lists whose entries are not all constants: `x in [a, b]` and `for x in [a, b]`. Lists where every element is constant had already received this optimization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

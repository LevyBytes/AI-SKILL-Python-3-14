# Python 3.10.0 alpha 4 / library / random

[bpo-42470](https://bugs.python.org/issue?@action=redirect&bpo=42470): [`random.sample()`](https://docs.python.org/3.14/library/random.html#random.sample) stops warning about a sequence that doubles as a set.

[bpo-42222](https://bugs.python.org/issue?@action=redirect&bpo=42222): Brought [`random.randrange()`](https://docs.python.org/3.14/library/random.html#random.randrange) argument handling in line with [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range).

  - Inside `randrange()`, the integer test and conversion now relies on [`operator.index()`](https://docs.python.org/3.14/library/operator.html#operator.index).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 4 / core and builtins / stdtypes

[bpo-43413](https://bugs.python.org/issue?@action=redirect&bpo=43413): Undo the changes to `set.__init__`. Any subclass of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) must supply a `__init__()` method whenever it supplies a `__new__()` method that takes extra keyword parameters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

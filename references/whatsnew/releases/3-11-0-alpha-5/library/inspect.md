# Python 3.11.0 alpha 5 / library / inspect

[bpo-43118](https://bugs.python.org/issue?@action=redirect&bpo=43118): Squash a bug in [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) that made it fail on certain subclasses of classes whose `__text_signature__` references module globals. Weipeng Hong wrote the patch.

[bpo-46103](https://bugs.python.org/issue?@action=redirect&bpo=46103): From now on [`inspect.getmembers()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmembers) reads the `__bases__` attribute only from the class type. Weipeng Hong contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

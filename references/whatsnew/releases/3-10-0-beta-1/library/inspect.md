# Python 3.10.0 beta 1 / library / inspect

[bpo-43817](https://bugs.python.org/issue?@action=redirect&bpo=43817): Introduce [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) for safely computing the annotations declared on an object. It sidesteps the oddities of reading annotations off various object types and assumes very little about whatever object you hand it. `inspect.get_annotations()` is likewise able to correctly un-stringize stringized annotations.

[`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature), `inspect.from_callable()`, and `inspect.from_function()` now route through [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) to fetch annotations. Consequently `inspect.signature()` and `inspect.from_callable()` are now able to un-stringize stringized annotations as well.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

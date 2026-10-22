# Python 3.11.0 alpha 5 / library / pathlib

[bpo-46483](https://bugs.python.org/issue?@action=redirect&bpo=46483): Drop [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) from [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath), since this class was never meant to be generic.

[bpo-46316](https://bugs.python.org/issue?@action=redirect&bpo=46316): Make [`pathlib.Path.iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir) faster by dropping a needless check for special entries.

[bpo-29688](https://bugs.python.org/issue?@action=redirect&bpo=29688): Provide documentation for [`pathlib.Path.absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.absolute) (a method that has always been present).

[bpo-43012](https://bugs.python.org/issue?@action=redirect&bpo=43012): The pathlib module's outdated internal `_Accessor` class is gone, clearing the way for forthcoming improvements to the module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

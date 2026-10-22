# Python 3.8.0 alpha 2 / core and builtins / functions and types

[bpo-36012](https://bugs.python.org/issue?@action=redirect&bpo=36012): Made class variable writes twice as fast. Updating a non-dunder attribute previously triggered a needless call that updated slots.

[bpo-36016](https://bugs.python.org/issue?@action=redirect&bpo=36016): `gc.get_objects` accepts an optional argument now that names a generation whose objects should be returned. Patch by Pablo Galindo.

[bpo-35992](https://bugs.python.org/issue?@action=redirect&bpo=35992): Repair `__class_getitem__()` failing to be invoked on a class whose custom metaclass is non-subscriptable.

[bpo-35911](https://bugs.python.org/issue?@action=redirect&bpo=35911): Permit constructing cell objects by introducing a `cell.__new__` method, and surface the `cell` type within `Lib/types.py` as CellType. Patch by Pierre Glaser.

[bpo-31506](https://bugs.python.org/issue?@action=redirect&bpo=31506): Make clearer the errors surfaced when `object.__new__` and `object.__init__` are handed more than a single argument. Contributed by Sanyam Khurana.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 1 / core and builtins / functions and types

[bpo-33930](https://bugs.python.org/issue?@action=redirect&bpo=33930): Resolved a segmentation fault triggered by deep recursion while tidying up method objects. Augusto Goulart and Pablo Galindo contributed the patch.

[bpo-44635](https://bugs.python.org/issue?@action=redirect&bpo=44635): The union type constructor now turns `None` into `type(None)`.

[bpo-44606](https://bugs.python.org/issue?@action=redirect&bpo=44606): Corrected `__instancecheck__` and `__subclasscheck__` for the union type.

[bpo-33346](https://bugs.python.org/issue?@action=redirect&bpo=33346): Comprehensions inside asynchronous functions may now contain asynchronous comprehensions. Any outer comprehensions then implicitly turn asynchronous.

[bpo-44963](https://bugs.python.org/issue?@action=redirect&bpo=44963): Add the `send()` and `throw()` methods to `anext_awaitable` objects. Pablo Galindo contributed the patch.

[bpo-44184](https://bugs.python.org/issue?@action=redirect&bpo=44184): Corrected a crash during Python exit triggered when a deallocator function drops the final strong reference to a heap type. Victor Stinner wrote the patch.

[bpo-44114](https://bugs.python.org/issue?@action=redirect&bpo=44114): Corrected wrong dictkeys_reversed and dictitems_reversed function signatures within the C code, which had broken webassembly builds.

[bpo-44490](https://bugs.python.org/issue?@action=redirect&bpo=44490): Gave `types.Union` a `__parameters__` attribute together with a `__getitem__` operator. Yurii Karabas provided the patch.

[bpo-44483](https://bugs.python.org/issue?@action=redirect&bpo=44483): Corrected a crash within `types.Union` objects when building a union of an object that has a bad `__module__` field.

[bpo-44732](https://bugs.python.org/issue?@action=redirect&bpo=44732): Renamed `types.Union` to `types.UnionType`.

[bpo-44676](https://bugs.python.org/issue?@action=redirect&bpo=44676): Made `types.Union` objects serialisable. Yurii Karabas provided the patch.

[bpo-44662](https://bugs.python.org/issue?@action=redirect&bpo=44662): Gave `types.Union` a `__module__`. As a side benefit this clears up `types.Union` trouble with `typing.Annotated`. Yurii Karabas provided the patch.

[bpo-44655](https://bugs.python.org/issue?@action=redirect&bpo=44655): Errors about an unset __slots__ attribute now mention the type's name. Pablo Galindo wrote this change.

[bpo-44655](https://bugs.python.org/issue?@action=redirect&bpo=44655): When suggesting candidates for a missing attribute, skip any missing attribute whose name matches the one that failed. Pablo Galindo authored this.

[bpo-44646](https://bugs.python.org/issue?@action=redirect&bpo=44646): Corrected the hash of the union type so it no longer varies with argument ordering.

[bpo-44914](https://bugs.python.org/issue?@action=redirect&bpo=44914): Class version tags will no longer be recycled.

What this means is that a version tag acts as a unique marker for a class's state. Effective specialization of LOAD_ATTR and the other instructions depends on this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

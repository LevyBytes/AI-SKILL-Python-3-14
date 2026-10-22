# Python 3.11.0 alpha 4 / library / functions and types

[bpo-46342](https://bugs.python.org/issue?@action=redirect&bpo=46342): When applied, the `@typing.final` decorator now writes a `__final__` attribute onto the decorated object so runtime introspection becomes possible. Jelle Zijlstra wrote the patch.

[bpo-46278](https://bugs.python.org/issue?@action=redirect&bpo=46278): Honor the `context` argument within the `AbstractEventLoop.call_*()` methods. Loop implementations already accommodate it.

[bpo-44893](https://bugs.python.org/issue?@action=redirect&bpo=44893): EntryPoint objects have stopped being tuples. The advised approach for reaching values is via attribute (‘.name’, ‘.group’) or accessor (‘.load()’). Indexed access is deprecated and now triggers a deprecation warning.

[bpo-22047](https://bugs.python.org/issue?@action=redirect&bpo=22047): Invoking `add_argument_group()` upon an argument group is now deprecated. Likewise, invoking `add_argument_group()` or `add_mutually_exclusive_group()` upon a mutually exclusive group is deprecated.

Such usages were never meant to be supported and behave inconsistently. They surfaced on the API only by accident of inheritance, and a future release will drop them.

[bpo-46014](https://bugs.python.org/issue?@action=redirect&bpo=46014): Permit `typing.Union` and `types.UnionType` to serve as the dispatch argument for `functools.singledispatch`. Yurii Karabas provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

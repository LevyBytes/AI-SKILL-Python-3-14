# Python 3.14.0 alpha 1 / core and builtins / functions and types

[gh-122888](https://github.com/python/cpython/issues/122888): Stop a crash on some `str()` calls given positional arguments of the wrong type. Jelle Zijlstra contributed the fix.

[gh-120080](https://github.com/python/cpython/issues/120080): A direct call to `int.__round__()` now treats `None` as a valid argument.

[gh-119821](https://github.com/python/cpython/issues/119821): Repair the execution of [annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) inside classes whenever `globals` points at a non-dict. Jelle Zijlstra contributed the fix.

[gh-119726](https://github.com/python/cpython/issues/119726): Tune the code layout for JIT calls into C functions on AArch64. Diego Russo contributed the patch.

[gh-118921](https://github.com/python/cpython/issues/118921): Give `FrameLocalsProxy` a `copy()` method that hands back a snapshot `dict` holding the local variables.

[gh-123339](https://github.com/python/cpython/issues/123339): When a class has its `__module__` attribute assigned, the `__firstlineno__` entry is now dropped from the type's dict, which keeps the two from drifting out of sync.

[gh-115776](https://github.com/python/cpython/issues/115776): Turn on inline values — Python's counterpart to hidden classes — for every class whose instances have a fixed size.

[gh-117482](https://github.com/python/cpython/issues/117482): Builtin static types in subinterpreters no longer end up with unexpected slot wrappers created for them.

[gh-114091](https://github.com/python/cpython/issues/114091): Reworded the message raised on awaiting a non-awaitable.

> Previously: ?object &lt;type&gt; can't be used in an await expression?.

> Now: ??&lt;type&gt;? object can't be awaited?.

[bpo-24766](https://bugs.python.org/issue?@action=redirect&bpo=24766): Repair how the `doc` argument is handled for subclasses of `property`.

[gh-119258](https://github.com/python/cpython/issues/119258): Drop the type version guards from the tier two interpreter.

Be aware that assigning `tp_version_tag` by hand (something never supported) can lead to crashes.

[gh-119311](https://github.com/python/cpython/issues/119311): Repair a defect where, in the bases of generic classes, names get mangled unexpectedly.

[gh-119395](https://github.com/python/cpython/issues/119395): Repair a defect where names following a generic class undergo mangling as though they sat inside that generic class.

[gh-124513](https://github.com/python/cpython/issues/124513): A crash in the FrameLocalsProxy constructor is fixed by validating the argument count. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

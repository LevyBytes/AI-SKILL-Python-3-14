# Python 3.14.0 alpha 1 / library / exceptions

[gh-124390](https://github.com/python/cpython/issues/124390): Resolves the [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) seen when pairing `asyncio.staggered.staggered_race()` together with [`asyncio.eager_task_factory`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.eager_task_factory).

[gh-122400](https://github.com/python/cpython/issues/122400): Cope with any [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) thrown by [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) within [`filecmp.dircmp`](https://docs.python.org/3.14/library/filecmp.html#filecmp.dircmp) and [`filecmp.cmpfiles()`](https://docs.python.org/3.14/library/filecmp.html#filecmp.cmpfiles). Patch by Bénédikt Tran.

[gh-123446](https://github.com/python/cpython/issues/123446): Repairs the blank function name shown in [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when [`csv.reader()`](https://docs.python.org/3.14/library/csv.html#csv.reader), [`csv.writer()`](https://docs.python.org/3.14/library/csv.html#csv.writer), or [`csv.register_dialect()`](https://docs.python.org/3.14/library/csv.html#csv.register_dialect) get called without the args they require.

[gh-122170](https://github.com/python/cpython/issues/122170): Cope with any [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) thrown by [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) within [`linecache`](https://docs.python.org/3.14/library/linecache.html#module-linecache). Patch by Bénédikt Tran.

[gh-121804](https://github.com/python/cpython/issues/121804): Display error locations accurately whenever a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) is raised within the new repl. Patch by Sergey B Kirpichev.

[gh-119577](https://github.com/python/cpython/issues/119577): The [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) raised when checking the truthiness of an [`xml.etree.ElementTree.Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) now states that a future release will unconditionally yield `True`, instead of describing an exception that Python 3.14 would raise.

[gh-119555](https://github.com/python/cpython/issues/119555): Trap any [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) coming from [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) inside the runsource() method belonging to InteractiveColoredConsole. Sergey B Kirpichev wrote the patch.

[gh-118803](https://github.com/python/cpython/issues/118803): Both `typing.ByteString` and `collections.abc.ByteString` no longer exist. A [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) had been raised for them since Python 3.12.

[gh-114053](https://github.com/python/cpython/issues/114053): Eliminate a spurious [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) raised by [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) under `eval_str=True`` on a class that made use of [**PEP 695**](https://peps.python.org/pep-0695/) type parameters in a module that had `from __future__ import annotations` placed at the file's head. Alex Waygood supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

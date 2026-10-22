# Python 3.12.0 alpha 1 / library / functions and types

[gh-64373](https://github.com/python/cpython/issues/64373): Port `_functools` over to argument clinic.

[gh-94597](https://github.com/python/cpython/issues/94597): Marked the `asyncio.AbstractEventLoopPolicy.get_child_watcher()` and `asyncio.AbstractEventLoopPolicy.set_child_watcher()` methods deprecated, slated for removal in Python 3.14. Kumar Aditya wrote the patch.

[gh-94597](https://github.com/python/cpython/issues/94597): The `MultiLoopChildWatcher`, `FastChildWatcher` and `SafeChildWatcher` child watcher classes are now deprecated, due for removal in Python 3.14. Kumar Aditya wrote the patch.

[gh-96385](https://github.com/python/cpython/issues/96385): `TypeVarTuple.__typing_prepare_subst__` is corrected. Formerly `TypeError` failed to fire when more than a single `TypeVarTuple`, such as `[*T, *V]`, appeared in type alias substitutions.

[gh-95861](https://github.com/python/cpython/issues/95861): The existing statistics.correlation() function picks up the ability to compute Spearman’s correlation coefficient.

[gh-90817](https://github.com/python/cpython/issues/90817): The `locale.resetlocale()` function has been deprecated and is slated for removal in Python 3.13. Reach for `locale.setlocale(locale.LC_ALL, "")` instead. Victor Stinner supplied the patch.

[gh-92728](https://github.com/python/cpython/issues/92728): The `re.template()` function together with its matching `re.TEMPLATE` and `re.T` flags, dropped in 3.11.0b1, have been brought back, although they now carry a deprecation and may disappear in Python 3.13.

[gh-92839](https://github.com/python/cpython/issues/92839): Eliminated a crash that came from invoking bisect.insort() or bisect.insort_left() while passing a key argument other than `None`.

[gh-96865](https://github.com/python/cpython/issues/96865): adjust Flag so that it applies boundary CONFORM.

This brings back the older Flag semantics that let flags carrying non-sequential values be merged together; for instance:

class Skip(Flag): TWO = 2 EIGHT = 8

Skip.TWO | Skip.EIGHT -> <Skip.TWO|EIGHT: 10>

[gh-96741](https://github.com/python/cpython/issues/96741): The dataclass field `pstats.FunctionProfile.ncalls` now carries the right type annotation, namely `str`.

[gh-96538](https://github.com/python/cpython/issues/96538): The `bisect.bisect()` family runs quicker by leaning on type-stability.

[gh-94199](https://github.com/python/cpython/issues/94199): The `ssl.match_hostname()` function is removed. `ssl.match_hostname()` carried a deprecation as of Python 3.7. OpenSSL has handled hostname matching since Python 3.7, and Python stopped using the `ssl.match_hostname()` function. Victor Stinner wrote the patch.

[gh-91456](https://github.com/python/cpython/issues/91456): Deprecate the present default auto() behaviour: starting in 3.13 the default becomes auto() always handing back the largest member value plus 1, and it will raise whenever incompatible value types get mixed.

[gh-91102](https://github.com/python/cpython/issues/91102): `_warnings.warn_explicit()` gets ported across to Argument Clinic.

[bpo-41246](https://bugs.python.org/issue?@action=redirect&bpo=41246): Use one shared completion callback for the finished overlapped operation across the `recv`, `recv_into`, `recvfrom`, `sendto`, `send` and `sendfile` functions within `IocpProactor`.

[gh-93973](https://github.com/python/cpython/issues/93973): Introduce the `all_errors` keyword argument on `asyncio.create_connection`, letting several connection failures surface together as an `ExceptionGroup`.

[gh-93963](https://github.com/python/cpython/issues/93963): Formally deprecate the `importlib.abc` classes that have relocated to `importlib.resources.abc`.

[bpo-47063](https://bugs.python.org/issue?@action=redirect&bpo=47063): Introduce an index_pages parameter that enables index page names other than the defaults.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

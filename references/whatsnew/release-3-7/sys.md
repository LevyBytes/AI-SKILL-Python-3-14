# What's New In Python 3.7 / sys - asyncio, sys

### sys

[`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint), which is built in, now invokes the freshly added [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook) hook function. (Contributed by Barry Warsaw in [bpo-31353](https://bugs.python.org/issue?@action=redirect&bpo=31353).)

The freshly added [`sys.getandroidapilevel()`](https://docs.python.org/3.14/library/sys.html#sys.getandroidapilevel) reports the build-time Android API version when running on Android. (Contributed by Victor Stinner in [bpo-28740](https://bugs.python.org/issue?@action=redirect&bpo=28740).)

A pair of new functions handle coroutine origin tracking depth: [`sys.get_coroutine_origin_tracking_depth()`](https://docs.python.org/3.14/library/sys.html#sys.get_coroutine_origin_tracking_depth) reports the depth presently in effect, while [`sys.set_coroutine_origin_tracking_depth()`](https://docs.python.org/3.14/library/sys.html#sys.set_coroutine_origin_tracking_depth) assigns it. Rather than the deprecated `sys.set_coroutine_wrapper()`, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) now relies on this new API. (Contributed by Nathaniel J. Smith in [bpo-32591](https://bugs.python.org/issue?@action=redirect&bpo=32591).)

### sys

Both `sys.set_coroutine_wrapper()` and `sys.get_coroutine_wrapper()` are now deprecated.

The undocumented `sys.callstats()` function is now deprecated and is scheduled to disappear in an upcoming Python version. (Contributed by Victor Stinner in [bpo-28799](https://bugs.python.org/issue?@action=redirect&bpo=28799).)

[Subject index](INDEX.md) · [Previous source section](subprocess.md) · [Next source section](time.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](sunau.md) · [Next source section](wave.md)

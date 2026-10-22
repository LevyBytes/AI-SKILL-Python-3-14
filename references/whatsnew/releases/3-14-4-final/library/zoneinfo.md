# Python 3.14.4 final / library / zoneinfo

[gh-146076](https://github.com/python/cpython/issues/146076): [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo): corrects crashes triggered by deleting `_weak_cache` from a [`zoneinfo.ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo) subclass.

[gh-145883](https://github.com/python/cpython/issues/145883): [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo): Corrects heap buffer overflow reads stemming from malformed TZif data. OSS Fuzz uncovered it, issues [#492245058](https://issues.oss-fuzz.com/issues/492245058) and [#492230068](https://issues.oss-fuzz.com/issues/492230068).

[gh-142781](https://github.com/python/cpython/issues/142781): [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo): a crash that occurred while building [`ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo) objects whose internal class-level cache had become inconsistent has been resolved.

[gh-142763](https://github.com/python/cpython/issues/142763): A race between [`zoneinfo.ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo) construction and [`zoneinfo.ZoneInfo.clear_cache()`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo.clear_cache), which had the potential to raise [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError), is now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

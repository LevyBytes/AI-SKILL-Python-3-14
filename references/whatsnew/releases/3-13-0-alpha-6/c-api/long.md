# Python 3.13.0 alpha 6 / c api / long

[gh-117021](https://github.com/python/cpython/issues/117021): Repair an integer overflow within [`PyLong_AsPid()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsPid) on non-Windows 64-bit platforms.

[gh-111140](https://github.com/python/cpython/issues/111140): Supply extra flags to [`PyLong_AsNativeBytes()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsNativeBytes) and [`PyLong_FromNativeBytes()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromNativeBytes) so the caller can decide how edge cases get handled when values fill up the whole buffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

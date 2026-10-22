# Python 3.14.0 alpha 1 / core and builtins / stdtypes

[gh-122239](https://github.com/python/cpython/issues/122239): Unpacking a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) that holds too many elements now surfaces the true length within the error message.

[gh-120397](https://github.com/python/cpython/issues/120397): Raise the throughput as much as twofold for the [`str.count()`](https://docs.python.org/3.14/library/stdtypes.html#str.count), [`bytes.count()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.count) and [`bytearray.count()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.count) methods while they count single characters.

[gh-77894](https://github.com/python/cpython/issues/77894): A potential garbage-collector crash, triggered when it attempts to break a reference loop that contains a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object, is fixed. A `memoryview` object may now be cleared only when no buffers still refer to it.

[gh-118561](https://github.com/python/cpython/issues/118561): Repair a free-threaded-build race in which [`list.extend()`](https://docs.python.org/3.14/library/stdtypes.html#list.extend) might leak uninitialised memory to readers running concurrently.

[gh-84978](https://github.com/python/cpython/issues/84978): Introduce the class methods [`float.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#float.from_number) and [`complex.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#complex.from_number).

[gh-111999](https://github.com/python/cpython/issues/111999): Correct the signature on [`str.format_map()`](https://docs.python.org/3.14/library/stdtypes.html#str.format_map).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 alpha 3 / core and builtins / collections and iteration

[gh-127058](https://github.com/python/cpython/issues/127058): `PySequence_Tuple` builds its resulting tuple in one atomic step now, so half-built tuples are never exposed to the garbage collector or via `gc.get_referrers()`

[gh-127010](https://github.com/python/cpython/issues/127010): Streamline how the GC tracks dictionaries. Every dictionary is now tracked the moment it is created, instead of waiting until some trackable object got inserted. That trims the code substantially and yields a small performance gain.

[gh-126091](https://github.com/python/cpython/issues/126091): Keep stack traces whole when something is thrown into a generator chain whose tail is a custom generator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

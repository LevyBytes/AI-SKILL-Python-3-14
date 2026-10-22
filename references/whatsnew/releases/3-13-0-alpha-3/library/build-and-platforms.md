# Python 3.13.0 alpha 3 / library / build and platforms

[gh-111615](https://github.com/python/cpython/issues/111615): Repair a regression stemming from the [gh-93162](https://github.com/python/cpython/issues/93162) fix, which had made it impossible to configure a `QueueHandler` unless handlers were specified.

[gh-112970](https://github.com/python/cpython/issues/112970): Where it exists on Linux (for instance glibc-2.34), `closefrom()` is now used in place of restricting that call to FreeBSD alone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

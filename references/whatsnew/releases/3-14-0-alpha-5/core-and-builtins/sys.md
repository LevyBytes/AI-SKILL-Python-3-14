# Python 3.14.0 alpha 5 / core and builtins / sys

[gh-129393](https://github.com/python/cpython/issues/129393): On FreeBSD, [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform) no longer carries the major version. It is consistently `'freebsd'` now, in place of `'freebsd13'` or `'freebsd14'`.

[gh-128807](https://github.com/python/cpython/issues/128807): Give the free-threaded GC a marking phase, mirroring the work tracked in [gh-126491](https://github.com/python/cpython/issues/126491). Because that GC lacks generations and is not incremental, its marking phase hunts for every object reachable from known roots. Roots are the objects guaranteed not to be garbage, such as the module dictionary for [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys). For the majority of programs this marking phase should speed the GC up a little, since usually less work happens per object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

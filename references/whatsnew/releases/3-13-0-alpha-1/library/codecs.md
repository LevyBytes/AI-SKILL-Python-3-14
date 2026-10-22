# Python 3.13.0 alpha 1 / library / codecs

[gh-66143](https://github.com/python/cpython/issues/66143): The [`codecs.CodecInfo`](https://docs.python.org/3.14/library/codecs.html#codecs.CodecInfo) object can now be copied and pickled. Robert Lehmann and Furkan Onder provided the patch.

[gh-50644](https://github.com/python/cpython/issues/50644): Trying to pickle, or to make a shallow or deep copy of, [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) streams now raises a TypeError. Previously copying broke with a RecursionError, whereas pickling generated incorrect results that ultimately made unpickling fail with a RecursionError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

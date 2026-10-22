# What's New In Python 3.6 / New dict implementation

### New [dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping) implementation

The [dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping) type now leans on a "compact" layout drawn from [a proposal by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html) that was [first implemented by PyPy](https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html). The fresh [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) takes up somewhere between 20% and 25% less memory than its Python 3.5 counterpart.

Treat the order-preserving behavior of this fresh layout as an implementation detail you should not lean on (it could shift down the road, though the intent is to let this new dict implementation settle in the language across a handful of releases before any spec change mandates order-preserving semantics for every present and future Python implementation; this also keeps backwards-compatibility with earlier language versions where iteration order stays arbitrary, e.g. Python 3.5).

(Contributed by INADA Naoki in [bpo-27350](https://bugs.python.org/issue?@action=redirect&bpo=27350). Idea [originally suggested by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html).)

[Subject index](INDEX.md) · [Previous source section](pep-468-preserving-keyword-argument-order.md) · [Next source section](pep-523-adding-a-frame-evaluation-api-to-cpython.md) · [Release/subject declaration](summary-release-highlights.md)

# Python 3.14.0 alpha 1 / library / pickle

[gh-118830](https://github.com/python/cpython/issues/118830): Raise the default [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) protocol up to `5`.

[gh-122311](https://github.com/python/cpython/issues/122311): Make errors better in the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module. Where it once surfaced [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), [`PicklingError`](https://docs.python.org/3.14/library/pickle.html#pickle.PicklingError) now appears more frequently, with the originating exception chained behind it. The Python and C versions also gain clearer, unified error text.

[gh-122459](https://github.com/python/cpython/issues/122459): Make [`pickling`](https://docs.python.org/3.14/library/pickle.html#module-pickle) faster for by-name objects lacking the `__module__` attribute.

[gh-122311](https://github.com/python/cpython/issues/122311): Correct a few error messages within [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle).

[gh-120380](https://github.com/python/cpython/issues/120380): Repair the Python implementation of [`pickle.Pickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler) handling [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects under protocol version 5. Bénédikt Tran contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.3 final / library / pickle

[gh-143308](https://github.com/python/cpython/issues/143308): [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle): use-after-free crashes triggered when a [`PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer) is mutated concurrently by a custom buffer callback while pickling are now fixed. Bénédikt Tran and Aaron Wieczorek supplied the patch.

[gh-143638](https://github.com/python/cpython/issues/143638): For the C implementation, reentrant calls into the [`pickle.Pickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler) and [`pickle.Unpickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler) methods are now forbidden. This previously risked a crash or data corruption; now overlapping calls to the same object's methods raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

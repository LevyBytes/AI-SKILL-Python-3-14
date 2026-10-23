# What’s New in Python 2.3 / PEP 307: Pickle Enhancements - pickle

### PEP 307: Pickle Enhancements

During the 2.3 development cycle the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and `cPickle` modules got some work. Under 2.2 you could pickle new-style classes without trouble, yet the output wasn't very compact; [**PEP 307**](https://peps.python.org/pep-0307/) cites a small example in which a new-style class produces a pickled string three times the length of the one for a classic class.

The fix was a brand-new pickle protocol. For a long while the [`pickle.dumps()`](https://docs.python.org/3.14/library/pickle.html#pickle.dumps) function has carried a text-or-binary flag. Under 2.3 that flag goes from a Boolean to an integer: 0 means the old text-mode pickle format, 1 means the old binary format, and 2 now selects a fresh format specific to 2.3. There's a new constant, [`pickle.HIGHEST_PROTOCOL`](https://docs.python.org/3.14/library/pickle.html#pickle.HIGHEST_PROTOCOL), for picking whatever the most advanced available protocol is.

Treating unpickling as safe is no longer warranted. The [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) shipped with 2.2 included hooks meant to keep unsafe classes from being unpickled (namely a `__safe_for_unpickling__` attribute), but none of that code was ever reviewed, so it has all been stripped out in 2.3. Under no version of Python should you unpickle data you don't trust.

To trim the pickling cost for new-style classes, a new way to customize pickling arrived through three special methods: [`__getstate__()`](https://docs.python.org/3.14/library/pickle.html#object.__getstate__), [`__setstate__()`](https://docs.python.org/3.14/library/pickle.html#object.__setstate__), and [`__getnewargs__()`](https://docs.python.org/3.14/library/pickle.html#object.__getnewargs__). See [**PEP 307**](https://peps.python.org/pep-0307/) for these methods' complete semantics.

To shrink pickles even more, you can now use integer codes rather than long strings to name pickled classes. The Python Software Foundation will keep a registry of standardized codes; a range is also reserved for private use. As of now none have been assigned.

See also

[**PEP 307**](https://peps.python.org/pep-0307/) - Extensions to the pickle protocol

Written and implemented by Guido van Rossum and Tim Peters.

[Subject index](INDEX.md) · [Previous source section](pep-305-comma-separated-files.md) · [Next source section](extended-slices.md) · [Release/subject declaration](standard-set-type.md)

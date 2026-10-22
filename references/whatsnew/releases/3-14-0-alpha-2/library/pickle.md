# Python 3.14.0 alpha 2 / library / pickle

[gh-125631](https://github.com/python/cpython/issues/125631): Bring back the ability to assign [`persistent_id`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.persistent_id) plus [`persistent_load`](https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler.persistent_load) attributes on instances of the `Pickler` together with `Unpickler` classes inside the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module.

[gh-126489](https://github.com/python/cpython/issues/126489): For the value returned by `persistent_id()`, Python’s [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) implementation no longer invokes [`pickle.Pickler.persistent_id()`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.persistent_id).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

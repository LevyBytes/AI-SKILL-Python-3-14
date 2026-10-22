# Python 3.14.5 release candidate 1 / library / pickle

[gh-148914](https://github.com/python/cpython/issues/148914): Repair memoization of in-band [`PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer) inside the Python [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) implementation. Formerly, equal `PickleBuffer`s lost their identity, and an empty writable `PickleBuffer` memoized an empty bytearray object where `b''` belonged, so later references to `b''` came back unpickled as an empty bytearray object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

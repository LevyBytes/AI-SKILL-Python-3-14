# Python 3.13.0 beta 1 / core and builtins / fix case where object s dict drifted out sync

[gh-117750](https://github.com/python/cpython/issues/117750): Fix the case where an object's dict drifted out of sync with the object's internal values during clearing. `obj.__dict__.clear()` now wipes the internal values yet keeps the dict bound to the object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 1 / library / python

[gh-91577](https://github.com/python/cpython/issues/91577): Lift the imports inside `SharedMemory` methods up to module level so they remain runnable late during python finalization.

[gh-92546](https://github.com/python/cpython/issues/92546): An undocumented `python -m pprint` benchmark relocates into the `pprint` suite within pyperformance. Oleg Iarygin wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

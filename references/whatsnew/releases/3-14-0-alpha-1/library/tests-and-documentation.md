# Python 3.14.0 alpha 1 / library / tests and documentation

[gh-119121](https://github.com/python/cpython/issues/119121): Resolve a NameError occurring within `asyncio.staggered.staggered_race`. That function now has test coverage.

[gh-121381](https://github.com/python/cpython/issues/121381): Take out the `subprocess._USE_VFORK` escape hatch code along with its documentation. It went in purely as a precaution, and no known case actually needs it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

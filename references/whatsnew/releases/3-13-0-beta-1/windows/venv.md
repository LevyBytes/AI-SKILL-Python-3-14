# Python 3.13.0 beta 1 / windows / venv

[gh-90329](https://github.com/python/cpython/issues/90329): Mutes the warning shown during virtual environment creation whenever the requested and created paths diverge only by a short (8.3 style) name. The warning still appears if a junction or symlink along the path drove the venv to be built somewhere other than the requested location.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

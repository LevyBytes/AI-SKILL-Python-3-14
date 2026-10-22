# Python 3.8.0 alpha 1 / library / throw typeerror rather than crashing whenever collections deque subclass hands

[bpo-31608](https://bugs.python.org/issue?@action=redirect&bpo=31608): Throw a `TypeError` rather than crashing whenever a `collections.deque` subclass hands back a non-deque out of `__new__`. Patch by Oren Milman.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.0 beta 4 / library / logging

[gh-91555](https://github.com/python/cpython/issues/91555): A prior change, first added in 3.14.0b2, has now been undone. That change had turned off logging for a logger while that same logger was processing its own log messages. Following this reversion, the behaviour matches what it was before 3.14.0b2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

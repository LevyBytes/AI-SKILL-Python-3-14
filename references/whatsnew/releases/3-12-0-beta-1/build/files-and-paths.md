# Python 3.12.0 beta 1 / build / files and paths

[gh-100220](https://github.com/python/cpython/issues/100220): Swap the `SHELL` Makefile variable's default from `/bin/sh` to `/bin/sh -e`, so that intricate recipes are guaranteed to abort after an error. Up to now, `make install` might skip installing certain files and still report success.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

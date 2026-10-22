# Python 3.14.0 alpha 3 / library / faulthandler

[gh-123967](https://github.com/python/cpython/issues/123967): Correct faulthandler when it encounters trampoline frames: it now skips the top-most frame if that frame is a trampoline. Victor Stinner provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

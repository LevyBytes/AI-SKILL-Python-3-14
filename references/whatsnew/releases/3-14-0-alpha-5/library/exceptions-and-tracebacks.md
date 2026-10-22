# Python 3.14.0 alpha 5 / library / exceptions and tracebacks

[gh-115514](https://github.com/python/cpython/issues/115514): Resolve exceptions and partial writes that occurred after `asyncio._SelectorTransport` was closed before its writes finished.

[gh-128894](https://github.com/python/cpython/issues/128894): Keep `traceback.TracebackException._format_syntax_error` from failing when exceptions carry custom metadata.

[gh-128479](https://github.com/python/cpython/issues/128479): Stop `asyncio.staggered.staggered_race()` from both leaking tasks and surfacing an unhandled exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

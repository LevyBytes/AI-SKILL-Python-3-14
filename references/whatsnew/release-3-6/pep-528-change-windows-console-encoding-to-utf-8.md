# What's New In Python 3.6 / PEP 528: Change Windows console encoding to UTF-8

### PEP 528: Change Windows console encoding to UTF-8

On Windows the default console will from now on take every Unicode character and feed correctly decoded str objects through to Python code. The streams `sys.stdin`, `sys.stdout` and `sys.stderr` now fall back to utf-8 encoding.

This behavior kicks in only with an interactive console — not when files or pipes are redirected. To restore the earlier behaviour for interactive console sessions, set [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO).

See also

[**PEP 528**](https://peps.python.org/pep-0528/): Change Windows console encoding to UTF-8

PEP written and implemented by Steve Dower.

[Subject index](INDEX.md) · [Previous source section](pep-529-change-windows-filesystem-encoding-to-utf-8.md) · [Next source section](pep-520-preserving-class-attribute-definition-order.md) · [Release/subject declaration](summary-release-highlights.md)

# PYTHONLEGACYWINDOWSSTDIO

PYTHONLEGACYWINDOWSSTDIO

When set to a non-empty string, it skips the new console reader and writer. This means Unicode characters get encoded per the active console code page, instead of relying on utf-8.

This variable gets disregarded when the standard streams are redirected (to files or pipes) rather than pointing at console buffers.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous source section](pythonlegacywindowsfsencoding.md) · [Following source section](pythoncoerceclocale.md)

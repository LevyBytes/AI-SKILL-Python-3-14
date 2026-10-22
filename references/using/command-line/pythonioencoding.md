# PYTHONIOENCODING

PYTHONIOENCODING

When this is set ahead of running the interpreter, it supersedes the encoding applied to stdin/stdout/stderr, taking the form `encodingname:errorhandler`. Each of the `encodingname` and `:errorhandler` pieces is optional and carries the same sense as in [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode).

For stderr, the `:errorhandler` piece is disregarded; the handler is always `'backslashreplace'`.

Changed in version 3.4: The `encodingname` part is now optional.

Changed in version 3.6: On Windows, interactive console buffers disregard the encoding named by this variable unless `PYTHONLEGACYWINDOWSSTDIO` gets specified too. Files plus pipes routed through the standard streams stay unaffected.

[Subject index](INDEX.md) · [Previous source section](pythonintmaxstrdigits.md) · [Following source section](pythonnousersite.md)

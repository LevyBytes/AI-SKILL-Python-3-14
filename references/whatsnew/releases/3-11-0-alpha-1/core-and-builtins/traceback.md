# Python 3.11.0 alpha 1 / core and builtins / traceback

[bpo-45083](https://bugs.python.org/issue?@action=redirect&bpo=45083): When an exception is rendered by the interpreter, the name now carries a full qualname. Earlier, only the class name was joined to the module name, which now and then produced a wrong full name on screen.

(Only the C-code exception rendering was affected by this; the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module already relied on qualname).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

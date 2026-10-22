# Python 3.6.0 alpha 1 / core and builtins / exceptions and tracebacks

[bpo-22836](https://bugs.python.org/issue?@action=redirect&bpo=22836): Make sure the exception reports coming from PyErr_Display() and PyErr_WriteUnraisable() stay sensible even when formatting them spawns secondary errors. The reports affected are those that sys.__excepthook__() produces and the ones emitted when __del__() raises an exception.

[bpo-4806](https://bugs.python.org/issue?@action=redirect&bpo=4806): Keep the original TypeError exception from being masked when star (`*`) unpacking is used in function calls. Hagen Fürstenau and Daniel Urban's patch served as the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

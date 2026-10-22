# Python 3.11.0 alpha 1 / library / exceptions and tracebacks

[bpo-44678](https://bugs.python.org/issue?@action=redirect&bpo=44678): A distinct error message now covers discontinuous padding in *binascii.a2b_base64* strict mode.

[bpo-44594](https://bugs.python.org/issue?@action=redirect&bpo=44594): An `ExitStack` and `AsyncExitStack` corner case in exception chaining was fixed. Their behavior now lines up with a `with` block when `__context__` is deliberately set to `None` while the exception is still in flight.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

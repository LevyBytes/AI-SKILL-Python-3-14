# Python 3.11.0 alpha 3 / core and builtins / exceptions

[bpo-46004](https://bugs.python.org/issue?@action=redirect&bpo=46004): Correct the reported [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) position for failures tied to for loops carrying invalid targets. The patch came from Pablo Galindo

[bpo-45607](https://bugs.python.org/issue?@action=redirect&bpo=45607): A `__note__` field now exists on [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException). Its default value is `None`, yet you may assign a string, which then gets appended to the exception's traceback.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

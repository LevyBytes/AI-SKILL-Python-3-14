# Python 3.14.0 release candidate 1 / library / exceptions

[gh-136380](https://github.com/python/cpython/issues/136380): Throws [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) upon reaching [`concurrent.futures.InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor) while subinterpreters are unavailable.

[gh-134759](https://github.com/python/cpython/issues/134759): Repair the [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) within [`email.message.Message.get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) that arose when the payload being decoded is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. Kliment Lamonov contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

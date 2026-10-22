# Python 3.11.0 alpha 4 / library / traceback

[bpo-45615](https://bugs.python.org/issue?@action=redirect&bpo=45615): Within the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module, functions now raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) in place of [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) whenever an exception argument fails to be of type [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

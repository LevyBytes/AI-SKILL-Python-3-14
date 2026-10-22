# Python 3.6.0 alpha 1 / library / functions

[bpo-26637](https://bugs.python.org/issue?@action=redirect&bpo=26637): During Python shutdown, if [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) runs after [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) has already been cleared (set to `None`), the [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) module now raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) in place of a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

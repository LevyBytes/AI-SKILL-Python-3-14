# What’s New In Python 3.5 / API and Feature Removals - asyncio, ftplib

### Removed

### API and Feature Removals

These obsolete and formerly deprecated APIs and features were taken out:

- From the email package, the `__version__` attribute has been dropped. The email code stopped shipping apart from the stdlib a long while back, and across the last several releases the `__version__` string went unchanged.

- In the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) module the internal `Netrc` class, deprecated back in 3.4, is now gone. (Contributed by Matt Chaput in [bpo-6623](https://bugs.python.org/issue?@action=redirect&bpo=6623).)

- The whole notion of `.pyo` files is gone.

- Within the provisional [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module the JoinableQueue class, deprecated in 3.4.4, is now gone. (Contributed by A. Jesse Jiryu Davis in [bpo-23464](https://bugs.python.org/issue?@action=redirect&bpo=23464).)

[Subject index](INDEX.md) · [Previous source section](deprecated-python-modules-functions-and-methods.md) · [Next source section](porting-to-python-3-5.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.9 / importlib — importlib, importlib.resources

### importlib

For better alignment with import statements, [`importlib.util.resolve_name()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.resolve_name) will now raise [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when a relative import attempt is invalid. (Contributed by Ngalim Siregar in [bpo-37444](https://bugs.python.org/issue?@action=redirect&bpo=37444).)

Loaders that expose immutable module objects are now able to expose immutable packages as well, not just standalone modules. (Contributed by Dino Viehland in [bpo-39336](https://bugs.python.org/issue?@action=redirect&bpo=39336).)

The [`importlib.resources.files()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.files) function was added, handling subdirectories inside package data and mirroring the backport found in `importlib_resources` version 1.5. (Contributed by Jason R. Coombs in [bpo-39791](https://bugs.python.org/issue?@action=redirect&bpo=39791).)

Updated `importlib.metadata` to track `importlib_metadata` version 1.6.1.

[Subject index](INDEX.md) · [Previous source section](imaplib.md) · [Next source section](inspect.md) · [Release/subject declaration](summary-release-highlights.md)

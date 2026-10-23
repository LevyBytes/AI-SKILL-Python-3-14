# What's New In Python 3.4 / venv - venv

### venv

[`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) now ships activation scripts targeting the `csh` and `fish` shells. (Contributed by Andrew Svetlov in [bpo-15417](https://bugs.python.org/issue?@action=redirect&bpo=15417).)

[`EnvBuilder`](https://docs.python.org/3.14/library/venv.html#venv.EnvBuilder) along with its [`create()`](https://docs.python.org/3.14/library/venv.html#venv.create) convenience helper accept a fresh keyword argument *with_pip*, defaulting to `False`, which governs whether `EnvBuilder` guarantees a `pip` install inside the created environment. (Contributed by Nick Coghlan in [bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552), forming one piece of the [**PEP 453**](https://peps.python.org/pep-0453/) implementation.)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](wave.md) · [Release/subject declaration](release-highlights.md)

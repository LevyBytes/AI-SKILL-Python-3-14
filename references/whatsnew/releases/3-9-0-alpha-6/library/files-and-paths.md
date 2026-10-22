# Python 3.9.0 alpha 6 / library / files and paths

[bpo-40148](https://bugs.python.org/issue?@action=redirect&bpo=40148): A `pathlib.Path.with_stem()` was added that builds a fresh Path carrying a swapped stem.

[bpo-39682](https://bugs.python.org/issue?@action=redirect&bpo=39682): Drop the undocumented ability to *close* a `pathlib.Path` object through its context manager. The context manager dunder methods stay, yet they are now a no-op, which renders `Path` objects immutable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

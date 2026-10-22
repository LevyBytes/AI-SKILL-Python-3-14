# Python 3.11.0 alpha 1 / library / pdb

[bpo-44682](https://bugs.python.org/issue?@action=redirect&bpo=44682): The [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) *commands* directive was changed so that it refuses to attach commands to an invalid breakpoint and instead surfaces a suitable error.

[bpo-44461](https://bugs.python.org/issue?@action=redirect&bpo=44461): Fixed a [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) bug in how it dealt with an import failure caused by a package that lacks a `__main__` module

[bpo-28528](https://bugs.python.org/issue?@action=redirect&bpo=28528): A [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) bug was fixed where `checkline()` raised [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when invoked after `reset()`.

[bpo-34266](https://bugs.python.org/issue?@action=redirect&bpo=34266): Exceptions thrown while parsing the argument of the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) run/restart command are now handled.

[bpo-37022](https://bugs.python.org/issue?@action=redirect&bpo=37022): With its `p` and `pp` commands, [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) now surfaces exceptions raised by `repr()`.

[bpo-43318](https://bugs.python.org/issue?@action=redirect&bpo=43318): Corrected a defect in which [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) would not reliably echo breakpoints after they were cleared.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

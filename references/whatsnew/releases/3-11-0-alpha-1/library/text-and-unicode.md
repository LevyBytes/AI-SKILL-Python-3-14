# Python 3.11.0 alpha 1 / library / text and unicode

[bpo-44929](https://bugs.python.org/issue?@action=redirect&bpo=44929): Resolve a few edge cases in how `enum.Flag` renders as a string within the REPL. Pablo Galindo contributed the patch.

[bpo-44258](https://bugs.python.org/issue?@action=redirect&bpo=44258): Support PEP 515 for Fraction’s initialization from string.

[bpo-38693](https://bugs.python.org/issue?@action=redirect&bpo=38693): Prefer f-strings to `.format` in importlib.resources.

[bpo-33693](https://bugs.python.org/issue?@action=redirect&bpo=33693): Importlib.metadata now prefers f-strings to .format.

[bpo-39549](https://bugs.python.org/issue?@action=redirect&bpo=39549): The reprlib.Repr code formerly relied on a hardcoded ‘…’ string; this PR swaps that for a “fillvalue” attribute that defaults to ‘…’ and can be overridden on individual reprlib.Repr instances or on subclasses derived from it.

[bpo-41137](https://bugs.python.org/issue?@action=redirect&bpo=41137): The reader for .pdbrc files now assumes utf-8 encoding. Srinivas Reddy Thatiparthy authored the change

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

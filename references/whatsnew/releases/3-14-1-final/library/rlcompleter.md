# Python 3.14.1 final / library / rlcompleter

[gh-139289](https://github.com/python/cpython/issues/139289): Performs a genuine lazy-import of [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb), and puts back the previously installed completer once `rlcompleter` has been imported.

[gh-138860](https://github.com/python/cpython/issues/138860): Imports [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) lazily within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) so as to dodge a deadlock in subprocess.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

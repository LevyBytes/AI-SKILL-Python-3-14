# Python 3.6.0 alpha 1 / library / collections and iteration

[bpo-22227](https://bugs.python.org/issue?@action=redirect&bpo=22227): The TarFile iterator was rewritten using a generator. That approach is simpler than relying on a class.

[bpo-25718](https://bugs.python.org/issue?@action=redirect&bpo=25718): Corrected pickling and copying of the accumulate() iterator when total is None.

[bpo-24874](https://bugs.python.org/issue?@action=redirect&bpo=24874): Sped up itertools.cycle() while also making its pickle more compact.

- A crash within itertools.cycle.__setstate__() was fixed for cases where the first argument was not a list.

[bpo-13938](https://bugs.python.org/issue?@action=redirect&bpo=13938): 2to3 now turns StringTypes into a tuple. Mark Hammond submitted the patch.

[bpo-26492](https://bugs.python.org/issue?@action=redirect&bpo=26492): A spent array.array iterator now behaves like iterators over other mutable sequences: once exhausted it stays exhausted even when the underlying array gets extended.

[bpo-25195](https://bugs.python.org/issue?@action=redirect&bpo=25195): Addressed a regression in mock.MagicMock. Because _Call subclasses tuple (and changeset 3603bae63c13 only handled classes), we have to supply __ne__ on our own. Andrew Plummer contributed the patch.

[bpo-26870](https://bugs.python.org/issue?@action=redirect&bpo=26870): Introduce readline.set_auto_history(), which lets you keep entries from being added to the history list automatically. Tyler Crompton's patch served as the basis.

[bpo-25994](https://bugs.python.org/issue?@action=redirect&bpo=25994): The os.scandir() iterator gained a close() method along with support for the context manager protocol.

[bpo-26117](https://bugs.python.org/issue?@action=redirect&bpo=26117): The os.scandir() iterator now releases its file descriptor not just at the end of iteration but also when iteration fails with an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

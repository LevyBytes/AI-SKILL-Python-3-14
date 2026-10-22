# Python 3.5.2 release candidate 1 / library / collections and iteration

[bpo-26117](https://bugs.python.org/issue?@action=redirect&bpo=26117): The os.scandir() iterator now releases its file descriptor not only at the end of iteration but also when iteration fails with an error.

[bpo-25195](https://bugs.python.org/issue?@action=redirect&bpo=25195): Fix a regression affecting mock.MagicMock. Since _Call is a subclass of tuple (changeset 3603bae63c13 only handles classes), we have to supply __ne__ on our own. Andrew Plummer contributed the patch.

[bpo-25718](https://bugs.python.org/issue?@action=redirect&bpo=25718): Pickling and copying of the accumulate() iterator when total is None has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

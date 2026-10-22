# Python 3.8.0 alpha 1 / library / subprocess popen duplicates startupinfo argument original stays untouched edits copy

[bpo-34044](https://bugs.python.org/issue?@action=redirect&bpo=34044): `subprocess.Popen` now duplicates the *startupinfo* argument so the original stays untouched: it edits the copy, which lets one `STARTUPINFO` object be reused on several occasions.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)

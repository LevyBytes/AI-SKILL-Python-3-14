# Python 3.8.0 alpha 3 / library / pdb

[bpo-35931](https://bugs.python.org/issue?@action=redirect&bpo=35931): The [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) `debug` command now handles every exception gracefully.

[bpo-36130](https://bugs.python.org/issue?@action=redirect&bpo=36130): Repair `pdb` with `skip=...` while stepping into a frame that lacks a `__name__` global. Anthony Sottile wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

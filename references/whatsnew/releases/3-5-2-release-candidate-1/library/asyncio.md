# Python 3.5.2 release candidate 1 / library / asyncio

[bpo-26848](https://bugs.python.org/issue?@action=redirect&bpo=26848): Corrected asyncio/subprocess.communicate() so that empty input is handled. Jack O — Connor supplied the patch.

[bpo-27041](https://bugs.python.org/issue?@action=redirect&bpo=27041): asyncio: a loop.create_future method was introduced

[bpo-27223](https://bugs.python.org/issue?@action=redirect&bpo=27223): asyncio: corrected _read_ready and _write_ready so that they honor _conn_lost. ??ukasz Langa wrote the patch.

[bpo-22970](https://bugs.python.org/issue?@action=redirect&bpo=22970): asyncio: repaired an inconsistency when cancelling Condition.wait. David Coles supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

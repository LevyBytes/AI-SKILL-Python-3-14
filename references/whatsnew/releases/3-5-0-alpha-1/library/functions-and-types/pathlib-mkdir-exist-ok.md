# Python 3.5.0 alpha 1 / library / exists ok argument added pathlib mkdir can imitate what mkdir p

[bpo-21539](https://bugs.python.org/issue?@action=redirect&bpo=21539): An *exists_ok* argument was added to `Pathlib.mkdir()` so it can imitate what `mkdir -p` and `os.makedirs()` do. Setting it true causes `FileExistsErrors` to be ignored. Berker Peksag wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)

# What's New In Python 3.7 / dbm — dbm

### dbm

Read-only files can now be read by [`dbm.dumb`](https://docs.python.org/3.14/library/dbm.html#module-dbm.dumb), and it skips writing the index file whenever nothing has changed.

### dbm

[`dbm.dumb`](https://docs.python.org/3.14/library/dbm.html#module-dbm.dumb) can now read read-only files and skips writing the index file whenever it stays unchanged. When the index file is absent and gets recreated under the `'r'` and `'w'` modes, a deprecation warning now fires (and that will become an error in upcoming Python releases). (Contributed by Serhiy Storchaka in [bpo-28847](https://bugs.python.org/issue?@action=redirect&bpo=28847).)

[Subject index](INDEX.md) · [Previous source section](datetime.md) · [Next source section](decimal.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](collections.md) · [Next source section](enum.md)

# Python 3.6.6 release candidate 1 / library / imports and modules

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Small repairs in the typing module: annotations were added to `NamedTuple.__new__`, and `*args` plus `**kwds` now pass through `Generic.__new__`. The first PRs came from Paulius ?arka and Chad Dombrova.

[bpo-31908](https://bugs.python.org/issue?@action=redirect&bpo=31908): Repaired the cover-file output of the `trace` module command-line tool, which formerly wrote cover files only if the `--missing` option had been supplied. Michael Selik sent the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

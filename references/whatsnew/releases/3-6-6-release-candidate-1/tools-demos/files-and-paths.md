# Python 3.6.6 release candidate 1 / tools demos / files and paths

[bpo-31920](https://bugs.python.org/issue?@action=redirect&bpo=31920): Repaired how directories are handled when passed as arguments to the `pygettext` script. The work builds on a patch from Oleg Krasnikov.

[bpo-32885](https://bugs.python.org/issue?@action=redirect&bpo=32885): Introduced an `-n` flag on `Tools/scripts/pathfix.py` that turns off the automatic backup creation (the files bearing a `~` suffix).

[bpo-31583](https://bugs.python.org/issue?@action=redirect&bpo=31583): Repaired 2to3 so it works with the ?add-suffix option yet without the ?output-dir option for a relative path to files in the current directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

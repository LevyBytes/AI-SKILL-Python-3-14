# Python 3.6.0 beta 2 / library / files and paths

[bpo-27998](https://bugs.python.org/issue?@action=redirect&bpo=27998): Repaired bytes path handling in os.scandir() under Windows. Eryk Sun wrote the patch.

[bpo-26293](https://bugs.python.org/issue?@action=redirect&bpo=26293): Repaired writing of ZIP archives that do not begin at byte zero of the file. Per the specification, offsets within a ZIP file are now measured relative to where the archive begins.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

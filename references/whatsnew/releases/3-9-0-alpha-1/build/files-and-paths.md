# Python 3.9.0 alpha 1 / build / files and paths

[bpo-37936](https://bugs.python.org/issue?@action=redirect&bpo=37936): The `.gitignore` file consistently keeps every rule "rooted" with a non-trailing slash when that rule is supposed to target files at one particular spot in the repo. Earlier, whenever the file we meant to ignore sat at the repo root, we would frequently end up ignoring files and directories sharing that name anywhere across the tree by accident.

[bpo-37936](https://bugs.python.org/issue?@action=redirect&bpo=37936): The `.gitignore` file no longer covers any file that is actually tracked inside the Git repository. Greg Price supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

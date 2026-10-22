# Python 3.11.0 beta 1 / library / venv

[bpo-43218](https://bugs.python.org/issue?@action=redirect&bpo=43218): Block the creation of a venv whose path holds the PATH separator. Such a path could break how the activate script is used. Dustin Rodrigues authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.4 final / library / venv

[gh-145417](https://github.com/python/cpython/issues/145417): [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv): Stops the incorrect preservation of SELinux context while copying the `Activate.ps1` script. That script had inherited the SELinux security context belonging to the system template directory rather than that of the destination project directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

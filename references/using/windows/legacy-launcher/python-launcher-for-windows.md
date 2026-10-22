# 4.12. Python launcher for Windows (deprecated)

### 4.12. Python launcher for Windows (deprecated)

Deprecated since version 3.14: The Python Install Manager covered earlier now takes the place of both the launcher and this documentation. It stays here for the time being only as a matter of historical record.

Added in version 3.3.

The Python launcher for Windows is a utility that helps locate and run the various Python versions. It lets scripts (or the command-line) signal a preference for a particular Python version, then finds and runs that version.

In contrast to the `PATH` variable, the launcher picks the best-suited version of Python on its own. Per-user installs win out over system-wide ones, and the ordering goes by language version rather than by whichever was installed last.

The launcher first received its specification in [**PEP 397**](https://peps.python.org/pep-0397/).

[Subject index](INDEX.md) · [Previous source section](../legacy-installer/installing-free-threaded-binaries.md) · [Following source section](from-the-command-line.md)

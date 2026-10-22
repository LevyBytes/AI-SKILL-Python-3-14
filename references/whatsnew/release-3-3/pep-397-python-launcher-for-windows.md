# What's New In Python 3.3 / PEP 397: Python Launcher for Windows

### PEP 397: Python Launcher for Windows

A `py` launcher application now ships with the Python 3.3 Windows installer, and it serves to start Python applications without tying you to a specific version.

Double-clicking `*.py` files triggers this launcher behind the scenes. Should the system hold just one Python version, that one runs the file. When several versions are present, the newest version runs by default, though a Unix-style ?shebang line? placed inside the Python script can override that choice.

You may also call the launcher directly on the command line as the `py` application. Invoking `py` obeys the same version selection rules as launching scripts implicitly, but you can pin a more specific version by supplying the right arguments (for example `-3` to ask for Python 3 when Python 2 is installed too, or `-2.6` to single out an earlier Python version when a newer one is present).

Beyond the launcher itself, the Windows installer now offers a choice to append the freshly installed Python onto the system PATH. (Contributed by Brian Curtin in [bpo-3561](https://bugs.python.org/issue?@action=redirect&bpo=3561).)

See also

[**PEP 397**](https://peps.python.org/pep-0397/) - Python Launcher for Windows

PEP written by Mark Hammond and Martin v. Löwis; implementation by Vinay Sajip.

Launcher documentation: [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher)

Installer PATH modification: [Python install manager](https://docs.python.org/3.14/using/windows.html#windows-path-mod)

[Subject index](INDEX.md) · [Previous source section](performance-and-resource-usage.md) · [Next source section](pep-3151-reworking-the-os-and-io-exception-hierarchy.md) · [Release/subject declaration](summary-release-highlights.md)

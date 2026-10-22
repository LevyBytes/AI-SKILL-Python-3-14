# 4.1.1. Installation

### 4.1. Python install manager

### 4.1.1. Installation

You can get the Python install manager from the [Microsoft Store app](https://apps.microsoft.com/detail/9NQ7512CXL7T) or grab and install it from [python.org/downloads](https://www.python.org/downloads/). Both versions are the same.

For the Store route, just click "Install". Once that finishes, launch a terminal and enter `python` to begin.

For the file fetched from python.org, either double-click it and pick "Install", or execute `Add-AppxPackage <path to MSIX>` from Windows Powershell.

Following installation, the `python`, `py`, and `pymanager` commands ought to be present. Where Python is already installed, or where you have altered your `PATH` variable, removing them or reverting the changes may be necessary. Consult Troubleshooting for further assistance repairing commands that do not work.

The first time you install a runtime, you will probably be asked to append a directory to your `PATH`. That step is optional if you would rather rely on the `py` command, but it exists for anyone who wants the complete set of aliases (for instance, `python3.14.exe`) on hand. That directory defaults to `%LocalAppData%\Python\bin`, although an administrator can change it. To reach the system settings page where you add the path, click Start and look up "Edit environment variables for your account".

Every Python runtime you install gets its own directory for scripts. Those directories likewise must go on `PATH` should you wish to use them.

The Python install manager updates itself to new releases automatically. Doing so leaves any Python runtime installs untouched. Removing the Python install manager does not remove any Python runtimes.

When installing an MSIX is not possible in your situation, for instance because your automated deployment software lacks support for it, or because Windows Server 2019 is your target, refer to Advanced installation below for additional details.

[Subject index](INDEX.md) · [Previous source section](using-python-on-windows.md) · [Following source section](basic-use.md)

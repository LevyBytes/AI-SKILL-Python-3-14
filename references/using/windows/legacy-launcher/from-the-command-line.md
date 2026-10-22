# 4.12.1.1. From the command-line

### 4.12.1. Getting started

#### 4.12.1.1. From the command-line

Changed in version 3.6.

System-wide installs of Python 3.3 and newer drop the launcher onto your `PATH`. Because the launcher works with every available Python release, the particular version installed makes no difference. To confirm the launcher is present, run the command below in Command Prompt:

```none
py

```

What you should observe is the newest Python you have installed starting up - you can quit it as usual, and any extra command-line arguments you supply get forwarded straight to Python.

Where several Python versions are installed (say, 3.7 and 3.14), you will have spotted that Python 3.14 came up - to fire up Python 3.7 instead, try the command:

```none
py -3.7

```

To get the newest Python 2 you have installed, try the command:

```none
py -2

```

Should you encounter the error below, the launcher is not installed:

```none
'py' is not recognized as an internal or external command,
operable program or batch file.

```

The command:

```none
py --list

```

shows the currently installed version(s) of Python.

The `-x.y` argument is shorthand for the `-V:Company/Tag` argument, by which you can pin a particular Python runtime, even ones sourced from outside python.org. Any runtime registered in line with [**PEP 514**](https://peps.python.org/pep-0514/) becomes discoverable. The `--list` command enumerates every available runtime in the `-V:` format.

With the `-V:` argument, naming the Company restricts the choice to runtimes from that vendor, whereas naming only the Tag draws from every vendor. Note that leaving out the slash is read as a tag:

```none
# Select any '3.*' tagged runtime
py -V:3

# Select any 'PythonCore' released runtime
py -V:PythonCore/

# Select PythonCore's latest Python 3 runtime
py -V:PythonCore/3

```

The short form of the argument (`-3`) always picks only from core Python releases, never from other distributions. The longer form (`-V:3`), by contrast, may pick from any of them.

Matching of the Company is against the whole string and is case-insensitive. The Tag is matched against either the whole string or a prefix, as long as the character that follows is a dot or a hyphen. That is what lets `-V:3.1` match `3.1-32` yet not `3.10`. Tags get ordered numerically (`3.10` is newer than `3.1`), but the comparison is textual (`-V:3.01` will not match `3.1`).

[Subject index](INDEX.md) · [Previous source section](python-launcher-for-windows.md) · [Following source section](virtual-environments.md)

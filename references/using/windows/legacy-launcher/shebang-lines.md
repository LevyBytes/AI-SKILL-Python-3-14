# 4.12.2. Shebang lines

### 4.12.2. Shebang lines

When the opening line of a script file begins with `#!`, it goes by the name of a "shebang" line. Linux along with other Unix-like operating systems natively understands such lines, and on those systems they are routinely used to convey how a script ought to be run. This launcher brings the very same mechanism to Python scripts on Windows, and the examples above show it in action.

So that shebang lines in Python scripts stay portable across Unix and Windows, this launcher recognizes a set of 'virtual' commands for naming the interpreter to use. Those supported virtual commands are:

- `/usr/bin/env`

- `/usr/bin/python`

- `/usr/local/bin/python`

- `python`

For instance, if your script's opening line begins with

```sh
#! /usr/bin/python

```

Then the default Python, or an active virtual environment, will be found and used. Since plenty of Python scripts written for Unix will already carry this line, you should find such scripts work under the launcher with no changes. When you are authoring a fresh script on Windows that you hope will prove handy on Unix too, you ought to use one of the shebang lines beginning with `/usr`.

Each of the virtual commands above can take a trailing explicit version (either just the major version, or both major and minor). On top of that, you can ask for the 32-bit build by tacking on "-32" after the minor version. That is, `/usr/bin/python3.7-32` requests use of the 32-bit Python 3.7. Where a virtual environment is active, the version gets disregarded and the environment is used.

Added in version 3.7: From python launcher 3.7 onward you can ask for a 64-bit version via the "-64" suffix. What is more, you can give a major version plus architecture while omitting the minor (that is, `/usr/bin/python3-64`).

Changed in version 3.11: The "-64" suffix is deprecated, and now means "any architecture that is not provably i386/32-bit". To pin a specific environment, use the new `-V:*TAG*` argument carrying the full tag.

Changed in version 3.13: Virtual commands that mention `python` now favour an active virtual environment over a search of `PATH`. This covers the situation where the shebang reads `/usr/bin/env python3` while `python3.exe` is absent from the active environment.

The `/usr/bin/env` style of shebang line carries one extra special trait. Ahead of hunting for installed Python interpreters, this style searches the executable `PATH` for a Python executable whose name matches the first argument given. That mirrors how the Unix `env` program behaves, performing a `PATH` lookup. Should no executable matching the first argument after the `env` command turn up, but that argument starts with `python`, it gets handled as laid out for the other virtual commands. Setting the environment variable `PYLAUNCHER_NO_SEARCH_PATH` (to any value) skips this `PATH` search.

Shebang lines that fit none of these patterns are resolved against the `[commands]` section of the launcher's .INI file. You can use this to deal with certain commands in whatever way suits your system. The command's name has to be a single argument (no spaces inside the shebang executable), and the value put in its place is the full path to the executable (any extra arguments named in the .INI get quoted as part of the filename).

```ini
[commands]
/bin/xpython=C:\Program Files\XPython\python.exe

```

Any commands missing from the .INI file are taken as **Windows** executable paths, either absolute or relative to the directory that holds the script file. That is a convenience for Windows-only scripts, like those an installer generates, given that the behavior does not carry over to Unix-style shells. Such paths may be quoted and may carry several arguments, after which the path to the script and any further arguments are tacked on.

[Subject index](INDEX.md) · [Previous source section](from-file-associations.md) · [Following source section](arguments-in-shebang-lines.md)

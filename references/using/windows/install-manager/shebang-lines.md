# 4.1.9. Shebang lines

### 4.1.9. Shebang lines

When a script file's first line opens with `#!`, that line is called a "shebang" line. Linux and other Unix like operating systems support such lines natively and they see common use there to signal how a script ought to run. The `python` and `py` commands bring the same capabilities to Python scripts on Windows.

So that shebang lines in Python scripts stay portable between Unix and Windows, several "virtual" commands are supported for naming which interpreter to use. The virtual commands that are supported are:

- `/usr/bin/env <ALIAS>`

- `/usr/bin/env -S <ALIAS>`

- `/usr/bin/<ALIAS>`

- `/usr/local/bin/<ALIAS>`

- `<ALIAS>`

As an example, when the first line of your script opens with

```sh
#! /usr/bin/python

```

The default Python or an active virtual environment gets found and used. Because so many Python scripts written for Unix already carry this line, you should be able to run those scripts through the launcher without changing them. When writing a fresh script on Windows that you hope will prove useful on Unix, you should pick one of the shebang lines beginning with `/usr`.

Each of the virtual commands above can have `<ALIAS>` swapped for an alias from an installed runtime. In other words, any command produced in the global aliases directory (which you might have added to your `PATH` environment variable) is usable in a shebang, even when it is absent from your `PATH`. That makes shebangs like `/usr/bin/python3.12` work to select a specific runtime.

When no runtimes are installed, or when automatic installation is turned on, the requested runtime gets installed if needed. Refer to Configuration for details on configuration settings.

The `/usr/bin/env` style of shebang line will additionally scan the `PATH` environment variable for commands it does not recognize. This matches the behaviour of the Unix `env` program, which runs the same search, yet it favours launching known Python commands. A warning may show up while searching for arbitrary executables, and you can switch off that search through the `shebang_can_run_anything` configuration option.

Shebang lines matching none of the patterns get handled as *Windows* executable paths, either absolute or relative to the directory that holds the script file. That is a convenience for Windows-only scripts, like those an installer generates, since the behavior does not work with Unix-style shells. Such paths may be quoted and may carry several arguments, after which the path to the script plus any further arguments get appended. You can switch off this functionality through the `shebang_can_run_anything` configuration option.

Starting with version 26.3 of the Python install manager, you can add custom shebang templates to your configuration file. Add the `shebang_templates` object with one member per template (the string to match) plus the command to run when that template matches. The bulk of commands should be `py -V:<tag>` (or `pyw`) to start one of your installed runtimes. The `py -3.<version>` form works too, as does a bare `py` to start the default. No further arguments are supported.

```json5
{
    "shebang_templates": {
        "/usr/bin/python": "py",
        "/usr/bin/my_custom_python": "py -V:MyCustomPython/3"
    }
}

```

When the substitute command is neither `py` nor `pyw`, it gets written back into the shebang and normal handling carries on. If launching arbitrary executables is allowed, then giving a full path lets you redirect from Python to any executable. The template ought to match either the entire line (with leading and trailing whitespace disregarded), or everything before the first space within the shebang line.

Note

How shebangs behave in the Python install manager differs subtly from the earlier `py.exe` launcher, and the old configuration options no longer take effect. Should you depend specifically on the old behaviour or configuration, we suggest installing the [legacy launcher](https://www.python.org/ftp/python/3.14.0/win32/launcher.msi). That legacy launcher's `py` command will by default take precedence over PyManager's one, and you will have to use `pymanager` commands for installing and uninstalling.

[Subject index](INDEX.md) · [Previous source section](configuration.md) · [Following source section](advanced-installation.md)

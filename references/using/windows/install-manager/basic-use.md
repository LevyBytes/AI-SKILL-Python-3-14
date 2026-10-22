# 4.1.2. Basic use

### 4.1.2. Basic use

For starting Python, the suggested command is `python`, which will start whichever version the launched script asks for, an active virtual environment, or the default installed version, which is the latest stable release unless you have set things up differently. When no version is explicitly asked for and there are no runtimes installed whatsoever, the current latest release gets installed for you.

Across all cases that involve more than one runtime version, `py` is the suggested command. You can substitute it anywhere for `python` or the legacy `py.exe` launcher. Out of the box, `py` mirrors the behaviour of `python`, yet it additionally accepts command line options to pick a particular version plus subcommands to administer installations. Those are described below.

Since the previous version may have already claimed the `py` command, an unambiguous `pymanager` command exists as well. Scripted installs that intend to rely on the Python install manager ought to think about using `pymanager`, given the reduced odds of clashing with existing installs. These two commands differ only when run with no arguments: `py` starts your default interpreter, whereas `pymanager` shows help (`pymanager exec ...` gives behaviour equivalent to `py ...`).

Each of these commands additionally comes in a windowed variant that skips creating a console window. Those are `pyw`, `pythonw` and `pymanagerw`. There is also a `python3` command that imitates the `python` command. Its role is to catch accidental uses of the usual POSIX command on Windows, but it is neither meant for broad use nor recommended.

To start your default runtime, run `python` or `py` together with the arguments you want handed to the runtime (such as script files or the module to launch):

```none
$> py
...
$> python my-script.py
...
$> py -m this
...

```

You can override the default runtime with the `PYTHON_MANAGER_DEFAULT` environment variable, or through a configuration file. Refer to Configuration for details on configuration settings.

To start a particular runtime, the `py` command takes a `-V:<TAG>` option. You must give this option ahead of any others. The tag is some or all of the identifier for the runtime; for runtimes from the CPython team, it resembles the version, possibly along with the platform. For compatibility reasons, the `V:` can be left out when the tag denotes an official release and begins with `3`.

```none
$> py -V:3.14 ...
$> py -V:3-arm64 ...

```

Runtimes from other distributors may also need the *company* to be supplied. Separate it from the tag with a slash, and it may be a prefix. Supplying the company is optional when it equals `PythonCore`, and supplying the tag is optional (though not the slash) when you want the newest release from a particular company.

```none
$> py -V:Distributor\1.0 ...
$> py -V:distrib/ ...

```

When no version is given but a script file is supplied, the script gets examined for a *shebang line*. That is a special format for a file's first line that permits overriding the command. Refer to Shebang lines for more details. If there is no shebang line, or it cannot be resolved, the script gets launched with the default runtime.

While you are operating inside an active virtual environment, have not asked for any specific version, and there is no shebang line, that virtual environment becomes the default runtime. Under such conditions, the `python` command was probably already overridden and none of these checks happened. Still, this behaviour guarantees the `py` command remains interchangeable.

Where no runtimes are installed, any launch command will attempt to install the requested version and start it. Yet once any version is installed, only the `py exec ...` and `pymanager exec ...` commands will install when the requested version is missing. Other command forms will show an error and point you toward using `py install` first.

[Subject index](INDEX.md) · [Previous source section](installation.md) · [Following source section](command-help.md)

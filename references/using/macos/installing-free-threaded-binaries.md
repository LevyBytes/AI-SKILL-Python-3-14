# 5.5.1. Installing Free-threaded Binaries

### 5.5. Advanced Topics

### 5.5.1. Installing Free-threaded Binaries

Added in version 3.13.

The `python.org` Python for macOS installer package can, as an option, install an extra build of Python 3.14 supporting [**PEP 703**](https://peps.python.org/pep-0703/), the free-threading feature (running with the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) turned off). Look at the release page on `python.org` for any updated information.

Free-threaded mode functions and keeps getting better, yet single-threaded workloads carry some extra overhead next to the regular build. On top of that, third-party packages, especially those bearing an [extension module](https://docs.python.org/3.14/glossary.html#term-extension-module), may not yet be ready to run in a free-threaded build, and will switch the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) back on. For that reason, free-threading support is not installed by default. It ships as a distinct install option, reachable by pressing the **Customize** button at the **Installation Type** step of the installer, as outlined above.

 (Figure: ../_images/mac_installer_09_custom_install_free_threaded.png)

When the box beside the **Free-threaded Python** package name is checked, a separate `PythonT.framework` gets installed too, sitting next to the usual `Python.framework` in `/Library/Frameworks`. With this arrangement, a free-threaded Python 3.14 build can co-exist on your system alongside a conventional (GIL only) Python 3.14 build at minimal risk while you install or test. This installation layout could change in future releases.

Known cautions and limitations:

- The **UNIX command-line tools** package, selected by default, installs links in `/usr/local/bin` for `python3.14t`, the free-threaded interpreter, and `python3.14t-config`, a configuration utility that package builders may find handy. Because `/usr/local/bin` is normally part of your shell `PATH`, in most situations no edits to your `PATH` environment variables should be required to use `python3.14t`.

- For this release, neither the **Shell profile updater** package nor the `Update Shell Profile.command` in `/Applications/Python 3.14/` supports the free-threaded package.

- The free-threaded build and the traditional build keep separate search paths and separate `site-packages` directories, so by default any package you need in both builds may have to be installed in each. For use with `python3.14t`, the free-threaded package installs its own separate instance of **pip**.

  - To install a package using **pip** without a **venv**:

```
python3.14t -m pip install <package_name>
```

- Whenever you juggle multiple Python environments, the safest and simplest course is usually to [create and use virtual environments](https://docs.python.org/3.14/tutorial/venv.html#tut-venv). That can head off potential command name clashes and confusion over which Python is active:

```
python3.14t -m venv <venv_name>
```

then **activate**.

- To run a free-threaded version of IDLE:

```
python3.14t -m idlelib
```

- Both builds' interpreters honor the same [PYTHON environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-envvars), which can give surprising results, for instance when you have `PYTHONPATH` set in a shell profile. Where needed, [command line options](https://docs.python.org/3.14/using/cmdline.html#using-on-interface-options) such as `-E` exist to disregard these environment variables.

- The free-threaded build links against the third-party shared libraries, `OpenSSL` and `Tk` for example, installed within the traditional framework. As a result, both builds also share a single set of trust certificates as laid down by the **Install Certificates.command** script, so it has to be run only once.

- If you cannot rely on the link in `/usr/local/bin` pointing at the `python.org` free-threaded `python3.14t` (say, because you want to put your own version there or another distribution does), you can set your shell `PATH` environment variable explicitly so it includes the `PythonT` framework `bin` directory:

```
export PATH="/Library/Frameworks/PythonT.framework/Versions/3.14/bin":"$PATH"
```

The traditional framework installation does much the same by default, only for `Python.framework`. Note that keeping both framework `bin` directories in `PATH` can cause confusion when duplicate names like `python3.14` exist in both; which one actually runs hinges on the order in which they show up in `PATH`. To see which path is in use, the `which python3.x` or `which python3.xt` commands can help. Virtual environments are a way to steer clear of such ambiguities. Yet another option is to set up a shell **alias** pointing at the interpreter you want, such as:

```
alias py3.14="/Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14"
alias py3.14t="/Library/Frameworks/PythonT.framework/Versions/3.14/bin/python3.14t"
```

[Subject index](INDEX.md) · [Previous source section](gui-programming.md) · [Following source section](installing-using-the-command-line.md)

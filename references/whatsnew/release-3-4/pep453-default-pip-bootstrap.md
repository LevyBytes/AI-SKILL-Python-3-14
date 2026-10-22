# What's New In Python 3.4 / PEP 453: Explicit Bootstrapping of PIP in Python Installations / Bootstrapping pip By Default — ensurepip, venv

### New Features

### PEP 453: Explicit Bootstrapping of PIP in Python Installations

#### Bootstrapping pip By Default

The fresh [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module (specified by [**PEP 453**](https://peps.python.org/pep-0453/)) supplies a uniform cross-platform way to bootstrap the pip installer into both Python installations and virtual environments. The `pip` build shipped alongside Python 3.4.0 is `pip` 1.5.4, and later 3.4.x maintenance releases will refresh the bundled build to whatever `pip` version exists when the release candidate gets built.

Out of the box, the `pipX` and `pipX.Y` commands get installed across every platform (here X.Y denotes the Python installation's version), together with the `pip` Python package plus its dependencies. Under Windows and within virtual environments on any platform, the unversioned `pip` command is installed as well. Elsewhere, the system wide unversioned `pip` command usually points at the independently installed Python 2 build.

The `pyvenv` command line utility together with the [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) module rely on the [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module so that `pip` is readily available inside virtual environments. With the command line utility, `pip` arrives by default, whereas with the `venv` module [API](https://docs.python.org/3.14/library/venv.html#venv-api) you must explicitly ask for `pip` to be installed.

For CPython [source builds on POSIX systems](https://docs.python.org/3.14/using/unix.html#building-python-on-unix), both the `make install` and `make altinstall` targets bootstrap `pip` automatically. Configure options govern this behaviour, and Makefile options can override it.

Under Windows and Mac OS X, the CPython installers now bring `pip` along with CPython by default (during setup users are free to decline installing it). To get `pip` callable from the command line by default, Windows users must opt in to the automatic `PATH` adjustments; absent that, it remains reachable via the Python launcher for Windows as `py -m pip`.

As [**discussed in the PEP**](https://peps.python.org/pep-0453/#recommendations-for-downstream-distributors) platform packagers are free to skip installing these commands by default, provided that, when run, they give clear and straightforward guidance on installing them for that platform (typically via the system package manager).

Note

So that parallel Python 2 and Python 3 installations don't clash, invoking `ensurepip` directly bootstraps only the versioned `pip3` and `pip3.4` commands by default - supplying the `--default-pip` option additionally requests the unversioned `pip` command. The `pyvenv` tool and the Windows installer guarantee that the unqualified `pip` command exists in those environments, and `pip` may always be run through the `-m` switch instead of directly, sidestepping ambiguity where several Python installations coexist.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights-argument-clinic-pep-436.md) · [Next source section](pep453-pip-documentation.md) · [Release/subject declaration](release-highlights.md)

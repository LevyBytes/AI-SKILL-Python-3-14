# What’s New in Python 2.7 / PEP 477: Backport ensurepip (PEP 453) to Python 2.7 / Bootstrapping pip By Default - ensurepip

#### Bootstrapping pip By Default

A standard, cross-platform way of bootstrapping the pip installer into Python installations is what the new [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module (set out in [**PEP 453**](https://peps.python.org/pep-0453/)) delivers. The `pip` version that ships with Python 2.7.9 is `pip` 1.5.6, and each later 2.7.x maintenance release will refresh the bundled copy to whatever `pip` version is current when the release candidate is built.

Out of the box, the `pip`, `pipX`, and `pipX.Y` commands get installed everywhere (with X.Y denoting the version of the Python installation), accompanied by the `pip` Python package together with its dependencies.

When doing CPython [source builds on POSIX systems](https://docs.python.org/3.14/using/unix.html#building-python-on-unix), the `make install` and `make altinstall` commands skip bootstrapping `pip` by default. You can steer this behaviour with configure options and override it with Makefile options.

Under Windows and Mac OS X, the CPython installers now install `pip` alongside CPython itself by default (people are free to decline it while installing). Windows users have to opt into the automatic `PATH` edits if they want `pip` reachable from the command line by default; short of that, it stays accessible by way of the Python launcher for Windows as `py -m pip`.

As [**discussed in the PEP**](https://peps.python.org/pep-0477/#disabling-ensurepip-by-downstream-distributors), platform packagers are at liberty to leave these commands out of the default install, provided that running them yields plain, easy instructions for installing them on that platform (typically via the system package manager).

[Subject index](INDEX.md) · [Previous source section](pep-477-backport-ensurepip-to-python-2-7.md) · [Next source section](pep477-ensurepip-documentation.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](pep-477-backport-ensurepip-to-python-2-7.md)

# Per-user, scientific, and multiple-interpreter installation

### How do I …?

What follows are brief answers, or pointers, covering a handful of frequent tasks.

### … install packages just for the current user?

Adding the `--user` option to `python -m pip install` installs a package solely for the account you're using, instead of for everyone on the machine.

### … install scientific Python packages?

Quite a few scientific Python packages carry tangled binary dependencies that aren't, at present, simple to set up through **pip** on its own. Users will frequently find it smoother to obtain such packages by [other means](https://packaging.python.org/science/) rather than going through **pip**.

See also

[Python Packaging User Guide: Installing Scientific Packages](https://packaging.python.org/science/)

### … work with multiple versions of Python installed in parallel?

Across Linux, macOS, and the rest of the POSIX systems, pair the version-numbered Python commands with the `-m` switch so the right copy of **pip** runs:

```shell
python3    -m pip install SomePackage  # default Python 3
python3.14 -m pip install SomePackage  # specifically Python 3.14

```

Suitably version-numbered **pip** commands might be on hand as well.

Over on Windows, reach for the **py** Python launcher together with the `-m` switch:

```shell
py -3    -m pip install SomePackage  # default Python 3
py -3.14 -m pip install SomePackage  # specifically Python 3.14

```

[Subject index](INDEX.md) · [Previous source section](install-version-pin-upgrade-and-use-virtual-environments.md) · [Next source section](system-python-safety-missing-pip-and-binary-extensions.md)

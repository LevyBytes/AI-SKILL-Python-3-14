# Install, version-pin, upgrade, and use virtual environments

### Basic usage

Every one of the standard packaging tools is built for command-line operation.

Running the command below pulls the newest release of a module, plus whatever it depends on, from PyPI:

```shell
python -m pip install SomePackage

```

Note

If you're on POSIX (macOS and Linux included), the examples here take for granted that you're working inside a [virtual environment](https://docs.python.org/3.14/glossary.html#term-virtual-environment).

On Windows, the examples here take for granted that you ticked the option to update the system PATH environment variable back when Python was installed.

You may also pin an exact or lowest acceptable version right on the command line. Whenever comparator operators like `>`, `<`, or any other character the shell would otherwise interpret come into play, wrap both the package name and the version in double quotes:

```shell
python -m pip install SomePackage==1.0.4    # specific version
python -m pip install "SomePackage>=1.0.4"  # minimum version

```

As a rule, when a fitting module is already present, asking to install it once more does nothing. Bringing already-installed modules up to date has to be asked for on purpose:

```shell
python -m pip install --upgrade SomePackage

```

Further details and material on **pip** and everything it can do live in the [Python Packaging User Guide](https://packaging.python.org).

Virtual environments are produced via the [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) module. To install packages into a virtual environment that's currently active, you use the same commands given above.

See also

[Python Packaging User Guide: Installing Python Distribution Packages](https://packaging.python.org/installing/)

[Subject index](INDEX.md) · [Previous source section](installation-policy-pip-venv-and-package-indexes.md) · [Next source section](per-user-scientific-and-multiple-interpreter-installation.md)

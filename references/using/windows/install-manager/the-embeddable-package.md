# 4.2. The embeddable package

### 4.2. The embeddable package

Added in version 3.5.

A ZIP file holding a minimal Python environment makes up the embedded distribution. Its purpose is to operate as a component of another application instead of being used directly by end-users.

We suggest installing an embedded distribution with `py install` together with the `--target` option:

```none
$> py install 3.14-embed --target=<directory>

```

Once extracted, the embedded distribution stays (nearly) completely isolated from the user’s system -- environment variables, system registry settings, and installed packages alike. The standard library ships as pre-compiled, optimized `.pyc` files inside a ZIP, and `python3.dll`, `python313.dll`, `python.exe` and `pythonw.exe` are all supplied. Left out are Tcl/tk (and everything that depends on it, such as Idle), pip, and the Python documentation.

The distribution carries a default `._pth` file, which narrows the default search paths further (see Finding modules below). Embedders are expected to edit this file as they require.

The application installer should place third-party packages next to the embedded distribution. Managing dependencies with pip the way you would for an ordinary Python installation is not supported here, although with care you might be able to bundle and use pip for automatic updates. As a rule, treat third-party packages as part of the application (“vendoring”), letting the developer confirm compatibility with newer versions before shipping updates to users.

The two recommended use cases for this distribution are described below.

[Subject index](INDEX.md) · [Previous source section](troubleshooting.md) · [Following source section](python-application.md)

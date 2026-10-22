# What's New In Python 3.4 / ensurepip — ensurepip

### ensurepip

The fresh [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module forms the core infrastructure behind the [**PEP 453**](https://peps.python.org/pep-0453/) implementation. Under ordinary circumstances end users won't have to touch this module, though it serves to manually bootstrap `pip` whenever the automatic bootstrapping into an installation or virtual environment was turned down.

[`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) carries a bundled copy of `pip`, current as of the first release candidate for the CPython release it ships with (this holds for both maintenance releases and feature releases). `ensurepip` never reaches out to the internet. Should the installation have internet access, once `ensurepip` has run the bundled `pip` can serve to upgrade `pip` to a newer release than the bundled one. (Bear in mind that such an upgraded `pip` counts as a separately installed package and won't be removed if Python gets uninstalled.)

The module bears the name *ensure*pip because, when called while `pip` is already installed, it takes no action. It additionally offers an `--upgrade` option that makes it install the bundled copy of `pip` whenever the currently installed `pip` version predates the bundled copy.

### enum

[Subject index](INDEX.md) · [Previous source section](asyncio.md) · [Release/subject declaration](release-highlights.md) · [Following release/subject continuation](enum.md)

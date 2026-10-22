# Python 3.10.0 alpha 5 / build / ensurepip

[bpo-42856](https://bugs.python.org/issue?@action=redirect&bpo=42856): Give the `./configure` script a `--with-wheel-pkg-dir=PATH` option. When it is supplied, the [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module hunts for `setuptools` and `pip` wheel packages inside that directory: when both turn up, those wheel packages stand in for the ensurepip bundled wheel packages.

Certain Linux distribution packaging policies discourage bundling dependencies. Fedora, for one, drops its wheel packages into the `/usr/share/python-wheels/` directory and leaves the `ensurepip._bundled` package uninstalled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

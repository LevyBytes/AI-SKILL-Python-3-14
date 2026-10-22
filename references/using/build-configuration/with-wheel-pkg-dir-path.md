# --with-wheel-pkg-dir=PATH

--with-wheel-pkg-dir=PATH

The directory holding wheel packages that the [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module uses (none by default).

Certain Linux distribution packaging policies discourage bundling dependencies. Fedora, for one, places wheel packages into the `/usr/share/python-wheels/` directory and skips installing the `ensurepip._bundled` package.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous source section](with-platlibdir-dirname.md) · [Following source section](with-pkg-config-check-yes-no.md)

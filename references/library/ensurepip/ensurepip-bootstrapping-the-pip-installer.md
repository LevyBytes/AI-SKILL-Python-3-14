# ensurepip — `ensurepip` — Bootstrapping the `pip` installer

## ensurepip — Bootstrapping the pip installer

### `ensurepip` — Bootstrapping the `pip` installer

Added in version 3.4.

**Source code:** [Lib/ensurepip](https://github.com/python/cpython/tree/3.14/Lib/ensurepip)

---

What the `ensurepip` package gives you is a way to bootstrap the `pip` installer into a Python installation or virtual environment that already exists. Bootstrapping makes sense here because `pip` is a project of its own that ships on its own schedule, with the newest stable build folded into the CPython reference interpreter's maintenance and feature releases.

For the most part, Python's end users won't have to call this module by hand, since `pip` ought to be bootstrapped automatically; you'd reach for it only when `pip` installation got skipped during Python's setup (or while a virtual environment was being made), or once you've deliberately removed `pip`.

Note

This module *does not* reach out to the internet. Every piece required to bootstrap `pip` already lives inside the package itself.

This counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your CPython copy not include it, turn to documentation from your distributor — whoever handed Python to you. If you happen to be that distributor, consult [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

See also

[Installing Python modules](https://docs.python.org/3.14/installing/index.html#installing-index)

The end user guide for installing Python packages

[**PEP 453**](https://peps.python.org/pep-0453/): Explicit bootstrapping of pip in Python installations

The original rationale and specification for this module.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

There is no support for this module on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or on [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

[Subject index](INDEX.md) · [Continue](command-line-interface.md)

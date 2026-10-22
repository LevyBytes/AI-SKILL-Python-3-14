# Build-time version constants

## API and ABI Versioning

### API and ABI Versioning

### Build-time version constants

The macros listed here are how CPython publishes its version number. Keep in mind they reflect the version the code was **built** against; for the value seen at **run time**, look at `Py_Version`.

A treatment of how API and ABI stability holds up from one version to the next appears in [C API Stability](https://docs.python.org/3.14/c-api/stable.html#stable).

 PY_MAJOR_VERSION

The `3` in `3.4.1a2`.

 PY_MINOR_VERSION

The `4` in `3.4.1a2`.

 PY_MICRO_VERSION

The `1` in `3.4.1a2`.

 PY_RELEASE_LEVEL

Corresponds to the `a` in `3.4.1a2`. Its value is `0xA` for alpha, `0xB` for beta, `0xC` for a release candidate, or `0xF` once final.

 PY_RELEASE_SERIAL

The `2` in `3.4.1a2`. Zero for final releases.

 PY_VERSION_HEX

Holds the Python version number packed into one integer; the packing scheme is described under `Py_PACK_FULL_VERSION()`.

Reach for this when doing numeric comparisons, such as `#if PY_VERSION_HEX >= ...`.

You’ll find these macros defined in [Include/patchlevel.h](https://github.com/python/cpython/tree/3.14/Include/patchlevel.h).

[Subject index](INDEX.md) · [Previous source contract](../allocating-objects-on-the-heap/soft-deprecated-aliases.md) · [Following source contract](py-version.md)

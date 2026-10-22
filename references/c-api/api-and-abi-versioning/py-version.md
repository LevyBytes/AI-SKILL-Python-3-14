# const unsigned long Py_Version

### Run-time version

 const unsigned long Py_Version

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

A single constant integer that packs the Python runtime version number — the version active at run time — with the packing layout explained at `Py_PACK_FULL_VERSION()`.

Reach for this when doing numeric comparisons, such as `if (Py_Version >= ...)`.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](build-time-version-constants.md) · [Following source contract](py-pack-full-version-to-py-pack-version.md)

# Limited C API

### Limited C API

The *Limited API*, a subset of Python's C API, arrived in Python 3.2. An extension confined to the Limited API can be built a single time and then loaded under several Python versions. The Limited API's contents appear in the list below.

 Py_LIMITED_API

Set this macro ahead of including `Python.h` to commit to the Limited API alone and to pick the Limited API version.

Set `Py_LIMITED_API` to the [`PY_VERSION_HEX`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.PY_VERSION_HEX) value matching the earliest Python version your extension targets. That extension stays ABI-compatible with every Python 3 release from the chosen one forward, and may draw on Limited API added up through that version.

Instead of reaching for the `PY_VERSION_HEX` macro itself, write a fixed minimum minor version (for example `0x030A0000` for Python 3.10) so things stay stable when you build against later Python versions.

Setting `Py_LIMITED_API` to `3` is another option. It behaves just like `0x03020000` (Python 3.2, the release where Limited API debuted).

[Subject index](INDEX.md) · [Previous source contract](stable-application-binary-interface.md) · [Following source contract](stable-abi.md)

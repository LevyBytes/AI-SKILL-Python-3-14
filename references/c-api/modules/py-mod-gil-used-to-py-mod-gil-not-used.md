# modules C API: `Py_MOD_GIL_USED`, `Py_MOD_GIL_NOT_USED`

Py_MOD_GIL_USED

The module leans on the global interpreter lock (GIL) being present, and it may touch global state without any synchronization.

 Py_MOD_GIL_NOT_USED

The module is safe to run without an active GIL.

Python builds that aren't configured with [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) disregard this slot. In every other case, it decides whether importing the module automatically switches the GIL on. Consult [Free-threaded CPython](https://docs.python.org/3.14/whatsnew/3.13.html#whatsnew313-free-threaded-cpython) for further detail.

A single module definition cannot name more than one `Py_mod_gil` slot.

Without `Py_mod_gil` specified, the import machinery falls back on `Py_MOD_GIL_USED`.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymoduledef-slot-to-py-mod-gil.md) · [Following source contract](pymodule-create-to-pymodule-execdef.md)

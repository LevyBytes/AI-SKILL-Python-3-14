# type Py_ssize_t

type Py_ssize_t

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A signed integer type for which `sizeof(Py_ssize_t) == sizeof(size_t)` holds. There is no direct C99 equivalent for this (size_t being an unsigned integer type). Consult [**PEP 353**](https://peps.python.org/pep-0353/) for the particulars. `PY_SSIZE_T_MAX` denotes the greatest positive value a `Py_ssize_t` can hold.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](types.md) · [Following source contract](exceptions.md)

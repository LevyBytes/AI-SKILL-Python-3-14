# unicode C API: `Py_UNICODE`, `PyUnicode_READY()`, `PyUnicode_IS_READY()`

type Py_UNICODE

A typedef for `wchar_t`, this stands for either a 16-bit or a 32-bit type according to the platform. Favor `wchar_t` on its own from now on.

Changed in version 3.3: Earlier on, whether this came out 16-bit or 32-bit hinged on your having picked a “narrow” or “wide” Unicode build of Python at compile time.

Deprecated since version 3.13, will be removed in version 3.15.

 int PyUnicode_READY([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Take no action and give back `0`. The sole reason this API survives is backward compatibility, yet removing it isn't on the agenda.

Added in version 3.3.

Deprecated since version 3.10: Ever since Python 3.12 this API has been a no-op. Formerly you had to invoke it on every string built through the old API (`PyUnicode_FromUnicode()` and the like).

 unsigned int PyUnicode_IS_READY([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

Take no action and give back `1`. The sole reason this API survives is backward compatibility, yet removing it isn't on the agenda.

Added in version 3.3.

Deprecated since version 3.14: Ever since Python 3.12 this API has been a no-op. Formerly it served to check whether a `PyUnicode_READY()` call was needed.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](deprecated-api.md)

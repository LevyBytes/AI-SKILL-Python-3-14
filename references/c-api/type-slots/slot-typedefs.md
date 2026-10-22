# slot typedefs

### slot typedefs

| typedef | Parameter Types | Return Type |
| --- | --- | --- |
| `allocfunc` | `PyTypeObject` * `Py_ssize_t` | `PyObject` * |
| `destructor` | `PyObject` * | void |
| `freefunc` | void * | void |
| `traverseproc` | `PyObject` * `visitproc` void * | int |
| `newfunc` | `PyTypeObject` * `PyObject` * `PyObject` * | `PyObject` * |
| `initproc` | `PyObject` * `PyObject` * `PyObject` * | int |
| `reprfunc` | `PyObject` * | `PyObject` * |
| `getattrfunc` | `PyObject` * const char * | `PyObject` * |
| `setattrfunc` | `PyObject` * const char * `PyObject` * | int |
| `getattrofunc` | `PyObject` * `PyObject` * | `PyObject` * |
| `setattrofunc` | `PyObject` * `PyObject` * `PyObject` * | int |
| `descrgetfunc` | `PyObject` * `PyObject` * `PyObject` * | `PyObject` * |
| `descrsetfunc` | `PyObject` * `PyObject` * `PyObject` * | int |
| `hashfunc` | `PyObject` * | Py_hash_t |
| `richcmpfunc` | `PyObject` * `PyObject` * int | `PyObject` * |
| `getiterfunc` | `PyObject` * | `PyObject` * |
| `iternextfunc` | `PyObject` * | `PyObject` * |
| `lenfunc` | `PyObject` * | `Py_ssize_t` |
| `getbufferproc` | `PyObject` * `Py_buffer` * int | int |
| `releasebufferproc` | `PyObject` * `Py_buffer` * | void |
| `inquiry` | `PyObject` * | int |
| `unaryfunc` | `PyObject` * | `PyObject` * |
| `binaryfunc` | `PyObject` * `PyObject` * | `PyObject` * |
| `ternaryfunc` | `PyObject` * `PyObject` * `PyObject` * | `PyObject` * |
| `ssizeargfunc` | `PyObject` * `Py_ssize_t` | `PyObject` * |
| `ssizeobjargproc` | `PyObject` * `Py_ssize_t` `PyObject` * | int |
| `objobjproc` | `PyObject` * `PyObject` * | int |
| `objobjargproc` | `PyObject` * `PyObject` * `PyObject` * | int |

See Slot Type typedefs below for more detail.

[Subject index](INDEX.md) · [Previous source contract](sub-slots.md) · [Following source contract](type-header-operation-gc-and-iteration-slots.md)

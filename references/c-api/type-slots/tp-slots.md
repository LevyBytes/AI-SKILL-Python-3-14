# “tp slots”

### Quick Reference

### “tp slots”

| PyTypeObject Slot [1] | Type | special methods/attrs | Info [2] |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| O | T | D | I |  |  |  |
| &lt;R&gt; `tp_name` | const char * | __name__ | X | X |  |  |
| `tp_basicsize` | `Py_ssize_t` |  | X | X |  | X |
| `tp_itemsize` | `Py_ssize_t` |  |  | X |  | X |
| `tp_dealloc` | `destructor` |  | X | X |  | X |
| `tp_vectorcall_offset` | `Py_ssize_t` |  |  | X |  | X |
| (`tp_getattr`) | `getattrfunc` | __getattribute__, __getattr__ |  |  |  | G |
| (`tp_setattr`) | `setattrfunc` | __setattr__, __delattr__ |  |  |  | G |
| `tp_as_async` | `PyAsyncMethods` * | sub-slots |  |  |  | % |
| `tp_repr` | `reprfunc` | __repr__ | X | X |  | X |
| `tp_as_number` | `PyNumberMethods` * | sub-slots |  |  |  | % |
| `tp_as_sequence` | `PySequenceMethods` * | sub-slots |  |  |  | % |
| `tp_as_mapping` | `PyMappingMethods` * | sub-slots |  |  |  | % |
| `tp_hash` | `hashfunc` | __hash__ | X |  |  | G |
| `tp_call` | `ternaryfunc` | __call__ |  | X |  | X |
| `tp_str` | `reprfunc` | __str__ | X |  |  | X |
| `tp_getattro` | `getattrofunc` | __getattribute__, __getattr__ | X | X |  | G |
| `tp_setattro` | `setattrofunc` | __setattr__, __delattr__ | X | X |  | G |
| `tp_as_buffer` | `PyBufferProcs` * | sub-slots |  |  |  | % |
| `tp_flags` | unsigned long |  | X | X |  | ? |
| `tp_doc` | const char * | __doc__ | X | X |  |  |
| `tp_traverse` | `traverseproc` |  |  | X |  | G |
| `tp_clear` | `inquiry` |  |  | X |  | G |
| `tp_richcompare` | `richcmpfunc` | __lt__, __le__, __eq__, __ne__, __gt__, __ge__ | X |  |  | G |
| (`tp_weaklistoffset`) | `Py_ssize_t` |  |  | X |  | ? |
| `tp_iter` | `getiterfunc` | __iter__ |  |  |  | X |
| `tp_iternext` | `iternextfunc` | __next__ |  |  |  | X |
| `tp_methods` | `PyMethodDef` [] |  | X | X |  |  |
| `tp_members` | `PyMemberDef` [] |  |  | X |  |  |
| `tp_getset` | `PyGetSetDef` [] |  | X | X |  |  |
| `tp_base` | `PyTypeObject` * | __base__ |  |  | X |  |
| `tp_dict` | `PyObject` * | __dict__ |  |  | ? |  |
| `tp_descr_get` | `descrgetfunc` | __get__ |  |  |  | X |
| `tp_descr_set` | `descrsetfunc` | __set__, __delete__ |  |  |  | X |
| (`tp_dictoffset`) | `Py_ssize_t` |  |  | X |  | ? |
| `tp_init` | `initproc` | __init__ | X | X |  | X |
| `tp_alloc` | `allocfunc` |  | X |  | ? | ? |
| `tp_new` | `newfunc` | __new__ | X | X | ? | ? |
| `tp_free` | `freefunc` |  | X | X | ? | ? |
| `tp_is_gc` | `inquiry` |  |  | X |  | X |
| <`tp_bases`> | `PyObject` * | __bases__ |  |  | ~ |  |
| <`tp_mro`> | `PyObject` * | __mro__ |  |  | ~ |  |
| [`tp_cache`] | `PyObject` * |  |  |  |  |  |
| [`tp_subclasses`] | void * | __subclasses__ |  |  |  |  |
| [`tp_weaklist`] | `PyObject` * |  |  |  |  |  |
| (`tp_del`) | `destructor` |  |  |  |  |  |
| [`tp_version_tag`] | unsigned int |  |  |  |  |  |
| `tp_finalize` | `destructor` | __del__ |  |  |  | X |
| `tp_vectorcall` | `vectorcallfunc` |  |  |  |  |  |
| [`tp_watched`] | unsigned char |  |  |  |  |  |

[Subject index](INDEX.md) · [Previous source contract](type-object-structures.md) · [Following source contract](sub-slots.md)

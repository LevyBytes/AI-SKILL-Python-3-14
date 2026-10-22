# Audit events table — ctypes

| Audit event | Arguments | References |
| --- | --- | --- |
| ctypes.addressof | `obj` | [1] |
| ctypes.call_function | `func_pointer`, `arguments` | [1] |
| ctypes.cdata | `address` | [1] |
| ctypes.cdata/buffer | `pointer`, `size`, `offset` | [1][2] |
| ctypes.create_string_buffer | `init`, `size` | [1] |
| ctypes.create_unicode_buffer | `init`, `size` | [1] |
| ctypes.dlopen | `name` | [1] |
| ctypes.dlsym | `library`, `name` | [1] |
| ctypes.dlsym/handle | `handle`, `name` | [1] |
| ctypes.get_errno |  | [1] |
| ctypes.get_last_error |  | [1] |
| ctypes.memoryview_at | `address`, `size`, `readonly` | [1] |
| ctypes.set_errno | `errno` | [1] |
| ctypes.set_exception | `code` | [1] |
| ctypes.set_last_error | `error` | [1] |
| ctypes.string_at | `ptr`, `size` | [1] |
| ctypes.wstring_at | `ptr`, `size` | [1] |

[Subject index](INDEX.md) · [Previous](audit-events-table-cpython.md) · [Continue](audit-events-table-ensurepip.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)

# sub-slots

### sub-slots

| Slot | Type | special methods |
| --- | --- | --- |
| `am_await` | `unaryfunc` | __await__ |
| `am_aiter` | `unaryfunc` | __aiter__ |
| `am_anext` | `unaryfunc` | __anext__ |
| `am_send` | `sendfunc` |  |
| `nb_add` | `binaryfunc` | __add__ __radd__ |
| `nb_inplace_add` | `binaryfunc` | __iadd__ |
| `nb_subtract` | `binaryfunc` | __sub__ __rsub__ |
| `nb_inplace_subtract` | `binaryfunc` | __isub__ |
| `nb_multiply` | `binaryfunc` | __mul__ __rmul__ |
| `nb_inplace_multiply` | `binaryfunc` | __imul__ |
| `nb_remainder` | `binaryfunc` | __mod__ __rmod__ |
| `nb_inplace_remainder` | `binaryfunc` | __imod__ |
| `nb_divmod` | `binaryfunc` | __divmod__ __rdivmod__ |
| `nb_power` | `ternaryfunc` | __pow__ __rpow__ |
| `nb_inplace_power` | `ternaryfunc` | __ipow__ |
| `nb_negative` | `unaryfunc` | __neg__ |
| `nb_positive` | `unaryfunc` | __pos__ |
| `nb_absolute` | `unaryfunc` | __abs__ |
| `nb_bool` | `inquiry` | __bool__ |
| `nb_invert` | `unaryfunc` | __invert__ |
| `nb_lshift` | `binaryfunc` | __lshift__ __rlshift__ |
| `nb_inplace_lshift` | `binaryfunc` | __ilshift__ |
| `nb_rshift` | `binaryfunc` | __rshift__ __rrshift__ |
| `nb_inplace_rshift` | `binaryfunc` | __irshift__ |
| `nb_and` | `binaryfunc` | __and__ __rand__ |
| `nb_inplace_and` | `binaryfunc` | __iand__ |
| `nb_xor` | `binaryfunc` | __xor__ __rxor__ |
| `nb_inplace_xor` | `binaryfunc` | __ixor__ |
| `nb_or` | `binaryfunc` | __or__ __ror__ |
| `nb_inplace_or` | `binaryfunc` | __ior__ |
| `nb_int` | `unaryfunc` | __int__ |
| `nb_reserved` | void * |  |
| `nb_float` | `unaryfunc` | __float__ |
| `nb_floor_divide` | `binaryfunc` | __floordiv__ |
| `nb_inplace_floor_divide` | `binaryfunc` | __ifloordiv__ |
| `nb_true_divide` | `binaryfunc` | __truediv__ |
| `nb_inplace_true_divide` | `binaryfunc` | __itruediv__ |
| `nb_index` | `unaryfunc` | __index__ |
| `nb_matrix_multiply` | `binaryfunc` | __matmul__ __rmatmul__ |
| `nb_inplace_matrix_multiply` | `binaryfunc` | __imatmul__ |
| `mp_length` | `lenfunc` | __len__ |
| `mp_subscript` | `binaryfunc` | __getitem__ |
| `mp_ass_subscript` | `objobjargproc` | __setitem__, __delitem__ |
| `sq_length` | `lenfunc` | __len__ |
| `sq_concat` | `binaryfunc` | __add__ |
| `sq_repeat` | `ssizeargfunc` | __mul__ |
| `sq_item` | `ssizeargfunc` | __getitem__ |
| `sq_ass_item` | `ssizeobjargproc` | __setitem__ __delitem__ |
| `sq_contains` | `objobjproc` | __contains__ |
| `sq_inplace_concat` | `binaryfunc` | __iadd__ |
| `sq_inplace_repeat` | `ssizeargfunc` | __imul__ |
| `bf_getbuffer` | `getbufferproc()` | __buffer__ |
| `bf_releasebuffer` | `releasebufferproc()` | __release_buffer__ |

[Subject index](INDEX.md) · [Previous source contract](tp-slots.md) · [Following source contract](slot-typedefs.md)

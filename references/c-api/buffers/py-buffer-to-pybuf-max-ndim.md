# buffers C API: `Py_buffer`, `PyBUF_MAX_NDIM`

type Py_buffer

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members) since version 3.11.*

 void *buf

A pointer marking the start of the logical structure that the buffer fields describe. It may land at any spot inside the exporter's underlying physical memory block. As an example, when `strides` are negative the value can point at the end of the memory block.

For [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous) arrays, the value points to the beginning of the memory block.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj

A new reference to the exporting object. The consumer owns this reference, which `PyBuffer_Release()` automatically releases (that is, decrements the reference count) and assigns `NULL`. This field corresponds to the return value of any ordinary C-API function.

There is a special case: for *temporary* buffers wrapped by [`PyMemoryView_FromBuffer()`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyMemoryView_FromBuffer) or `PyBuffer_FillInfo()`, the field is `NULL`. As a rule, exporting objects MUST NOT adopt this scheme.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len

`product(shape) * itemsize`. For contiguous arrays, this gives the length of the underlying memory block. For non-contiguous arrays, it gives the length the logical structure would have if it were copied into a contiguous form.

Reaching `((char *)buf)[0] up to ((char *)buf)[len-1]` is valid only when the buffer came from a request that guarantees contiguity. Typically that request will be `PyBUF_SIMPLE` or `PyBUF_WRITABLE`.

 int readonly

A flag signaling whether the buffer is read-only. The `PyBUF_WRITABLE` flag governs this field.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) itemsize

The size, in bytes, of one element. This matches the result of [`struct.calcsize()`](https://docs.python.org/3.14/library/struct.html#struct.calcsize) invoked on non-`NULL` `format` values.

A notable exception: when a consumer asks for a buffer without the `PyBUF_FORMAT` flag, `format` becomes `NULL`, yet `itemsize` keeps the value that corresponds to the original format.

When `shape` is present, the relation `product(shape) * itemsize == len` continues to hold, and the consumer may rely on `itemsize` to traverse the buffer.

When `shape` is `NULL` because of a `PyBUF_SIMPLE` or a `PyBUF_WRITABLE` request, the consumer must ignore `itemsize` and treat `itemsize == 1`.

 char *format

A *NULL* terminated string, written in the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module's style of syntax, that describes the contents of a single item. When this is `NULL`, `"B"` (unsigned bytes) is assumed.

The `PyBUF_FORMAT` flag governs this field.

 int ndim

How many dimensions the memory stands for as an n-dimensional array. When it equals `0`, `buf` points at a single item that represents a scalar. In that situation, `shape`, `strides`, and `suboffsets` MUST be `NULL`. `PyBUF_MAX_NDIM` sets the upper bound on the number of dimensions.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *shape

An array of [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), of length `ndim`, that conveys the shape of the memory viewed as an n-dimensional array. Be aware that `shape[0] * ... * shape[ndim-1] * itemsize` MUST equal `len`.

Shape entries are constrained to `shape[n] >= 0`. The situation `shape[n] == 0` calls for special handling. Consult complex arrays for more detail.

For the consumer, the shape array is read-only.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *strides

An array of [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), of length `ndim`, that states how many bytes to advance in order to reach the next element along each dimension.

Stride entries may take any integer value. With ordinary arrays, strides are normally positive, but a consumer MUST cope with the situation `strides[n] <= 0`. Consult complex arrays for more detail.

For the consumer, the strides array is read-only.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *suboffsets

An array of [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), of length `ndim`. When `suboffsets[n] >= 0`, the values held along the nth dimension are pointers, and the suboffset value specifies how many bytes to add to each pointer once it has been de-referenced. A negative suboffset value signals that no de-referencing is to take place (striding within a contiguous memory block).

When every suboffset is negative (that is, no de-referencing is required), this field must be `NULL` (its default value).

The Python Imaging Library (PIL) uses this style of array representation. Consult complex arrays for more detail on reaching elements of such an array.

For the consumer, the suboffsets array is read-only.

 void *internal

This is reserved for the exporting object's own internal use. The exporter could, for instance, re-cast it as an integer and use it to record flags indicating whether the shape, strides, and suboffsets arrays need to be freed when the buffer is released. The consumer MUST NOT change this value.

Constants:

 PyBUF_MAX_NDIM

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

The greatest number of dimensions the memory may stand for. Exporters MUST honor this cap, while consumers of multi-dimensional buffers SHOULD manage up to `PyBUF_MAX_NDIM` dimensions. At present it is fixed at 64.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](buffer-structure.md) · [Following source contract](buffer-request-types.md)

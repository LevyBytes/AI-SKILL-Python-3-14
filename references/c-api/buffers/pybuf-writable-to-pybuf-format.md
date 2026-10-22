# readonly, format

### readonly, format

>

 PyBUF_WRITABLE

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Governs the `readonly` field. When set, the exporter MUST hand back a writable buffer or otherwise signal failure. When not set, the exporter MAY hand back either a read-only or a writable buffer, but it MUST make that choice consistently across every consumer. As an example, PyBUF_SIMPLE | PyBUF_WRITABLE serves to request a simple writable buffer.

 PyBUF_WRITEABLE

This is a [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) alias to `PyBUF_WRITABLE`.

 PyBUF_FORMAT

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Governs the `format` field. When set, that field MUST be filled in correctly. When not set, that field MUST be `NULL`.

`PyBUF_WRITABLE` may be |'d with any of the flags listed in the next section. Because `PyBUF_SIMPLE` is defined as 0, `PyBUF_WRITABLE` works as a stand-alone flag for requesting a simple writable buffer.

`PyBUF_FORMAT` must be |'d with any of the flags other than `PyBUF_SIMPLE`, since the latter already implies the format `B` (unsigned bytes). `PyBUF_FORMAT` cannot be used by itself.

[Subject index](INDEX.md) · [Previous source contract](request-independent-fields.md) · [Following source contract](shape-strides-suboffsets.md)

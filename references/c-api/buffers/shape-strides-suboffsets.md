# shape, strides, suboffsets

### shape, strides, suboffsets

The flags governing the logical structure of the memory appear below in decreasing order of complexity. Observe that each flag includes every bit of the flags beneath it.

| Request | shape | strides | suboffsets |
| --- | --- | --- | --- |
| PyBUF_INDIRECT * Part of the Stable ABI since version 3.11.* | yes | yes | if needed |
| PyBUF_STRIDES * Part of the Stable ABI since version 3.11.* | yes | yes | NULL |
| PyBUF_ND * Part of the Stable ABI since version 3.11.* | yes | NULL | NULL |
| PyBUF_SIMPLE * Part of the Stable ABI since version 3.11.* | NULL | NULL | NULL |

[Subject index](INDEX.md) · [Previous source contract](pybuf-writable-to-pybuf-format.md) · [Following source contract](contiguity-requests.md)

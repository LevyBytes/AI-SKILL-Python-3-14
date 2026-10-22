# contiguity requests

### contiguity requests

C or Fortran [contiguity](https://docs.python.org/3.14/glossary.html#term-contiguous) may be requested outright, either with or without stride data. Lacking stride data, the buffer must be C-contiguous.

| Request | shape | strides | suboffsets | contig |
| --- | --- | --- | --- | --- |
| PyBUF_C_CONTIGUOUS * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | C |
| PyBUF_F_CONTIGUOUS * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | F |
| PyBUF_ANY_CONTIGUOUS * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | C or F |
| `PyBUF_ND` | yes | NULL | NULL | C |

[Subject index](INDEX.md) · [Previous source contract](shape-strides-suboffsets.md) · [Following source contract](compound-requests.md)

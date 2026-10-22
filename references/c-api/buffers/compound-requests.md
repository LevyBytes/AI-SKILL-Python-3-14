# compound requests

### compound requests

Every possible request is fully specified by some mixture of the flags from the prior section. As a convenience, the buffer protocol offers commonly used mixtures as single flags.

In the table below, *U* denotes undefined contiguity. The consumer would need to invoke `PyBuffer_IsContiguous()` to establish contiguity.

| Request | shape | strides | suboffsets | contig | readonly | format |
| --- | --- | --- | --- | --- | --- | --- |
| PyBUF_FULL * Part of the Stable ABI since version 3.11.* | yes | yes | if needed | U | 0 | yes |
| PyBUF_FULL_RO * Part of the Stable ABI since version 3.11.* | yes | yes | if needed | U | 1 or 0 | yes |
| PyBUF_RECORDS * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | U | 0 | yes |
| PyBUF_RECORDS_RO * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | U | 1 or 0 | yes |
| PyBUF_STRIDED * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | U | 0 | NULL |
| PyBUF_STRIDED_RO * Part of the Stable ABI since version 3.11.* | yes | yes | NULL | U | 1 or 0 | NULL |
| PyBUF_CONTIG * Part of the Stable ABI since version 3.11.* | yes | NULL | NULL | C | 0 | NULL |
| PyBUF_CONTIG_RO * Part of the Stable ABI since version 3.11.* | yes | NULL | NULL | C | 1 or 0 | NULL |

[Subject index](INDEX.md) · [Previous source contract](contiguity-requests.md) · [Following source contract](numpy-style-shape-and-strides.md)

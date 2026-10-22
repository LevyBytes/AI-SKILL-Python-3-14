# Python 3.14.3 final / build / files and paths

[gh-142454](https://github.com/python/cpython/issues/142454): While computing the digest over the JIT stencils input, order the hashed files by their filenames before feeding their content into the hasher. Doing so yields deterministic hash input, and thus a deterministic hash, regardless of filesystem ordering.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

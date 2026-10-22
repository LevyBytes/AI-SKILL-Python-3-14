# Python 3.12.0 alpha 3 / core and builtins / memory and lifetimes

[gh-99729](https://github.com/python/cpython/issues/99729): Address a problem where frames could remain observable to Python code while being torn down, a situation that risked memory corruption or hard interpreter crashes.

[gh-99581](https://github.com/python/cpython/issues/99581): Repaired a defect that produced a buffer overflow whenever the tokenizer copied a line lacking the newline character out of a file whose length matched the available tokenizer buffer. Pablo galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

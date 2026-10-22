# Python 3.13.0 alpha 3 / core and builtins / revise api contract pyexecutorobject hands back next instr pointer place

[gh-108866](https://github.com/python/cpython/issues/108866): Revise the API and contract of `_PyExecutorObject` so it hands back the next_instr pointer in place of the frame, and so it always runs at least a single instruction.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

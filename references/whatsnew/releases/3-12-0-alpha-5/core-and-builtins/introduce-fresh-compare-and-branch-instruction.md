# Python 3.12.0 alpha 5 / core and builtins / introduce fresh compare and branch instruction

[gh-100982](https://github.com/python/cpython/issues/100982): Introduce a fresh `COMPARE_AND_BRANCH` instruction. It runs somewhat more efficiently for a comparison directly followed by a branch, and it brings back the PEP 659 design goal that specializations stay confined to one instruction.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

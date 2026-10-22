# Python 3.8.0 alpha 3 / core and builtins / compiler and parser

[bpo-35808](https://bugs.python.org/issue?@action=redirect&bpo=35808): Retired pgen and instead generate the parser with a tweaked pgen2. Pablo Galindo wrote the patch.

[bpo-36256](https://bugs.python.org/issue?@action=redirect&bpo=36256): Repair a parsermodule bug encountered when parsing a DFA state holding two or more arcs whose labels share the same type. Pablo Galindo wrote the patch.

[bpo-35975](https://bugs.python.org/issue?@action=redirect&bpo=35975): Introduce a `feature_version` flag for `ast.parse()` (documented) plus `compile()` (hidden) that lets you nudge the parser into supporting earlier grammar versions. Specifically, when `feature_version` equals 5 or 6, the PEP 492 workarounds for the `async` and `await` keyword come back. (At 7 and above, those are always treated as keywords, though they remain special tokens rather than the `NAME` tokens the parser driver picks up.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

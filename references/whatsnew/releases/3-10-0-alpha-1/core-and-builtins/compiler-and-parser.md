# Python 3.10.0 alpha 1 / core and builtins / compiler and parser

[bpo-40939](https://bugs.python.org/issue?@action=redirect&bpo=40939): Renames the `PyPegen*` functions to `PyParser*`, letting us drop the old `PyParser*` set that depended on the old parser while staying backwards-compatible throughout.

[bpo-40939](https://bugs.python.org/issue?@action=redirect&bpo=40939): Deletes the leftover files belonging to the old parser plus the `symbol` module.

[bpo-39934](https://bugs.python.org/issue?@action=redirect&bpo=39934): Makes the compiler tally control blocks within "except" accurately. This guarantees that deeply nested, named exception handlers raise a syntax error rather than a fatal error.

[bpo-40903](https://bugs.python.org/issue?@action=redirect&bpo=40903): Corrected a segfault risk in the new PEG parser while it builds error messages for malformed assignments shaped like `p=p=`. Pablo Galindo provided the patch.

[bpo-40939](https://bugs.python.org/issue?@action=redirect&bpo=40939): Strips out the old parser, the `parser` module, and every piece of supporting code, command-line option, and environment variable tied to it. Pablo Galindo contributed the patch.

[bpo-41215](https://bugs.python.org/issue?@action=redirect&bpo=41215): Supplies non-NULL defaults across the PEG parser keyword list to work past a defect that kept Python from compiling cleanly with the XLC compiler. Pablo Galindo contributed the patch.

[bpo-41218](https://bugs.python.org/issue?@action=redirect&bpo=41218): A Python 3.8.3 regression saw compilation with ast.PyCF_ALLOW_TOP_LEVEL_AWAIT over-eagerly flag list comprehension as CO_COROUTINE. Going forward, only a list comprehension that actually uses async/await will be tagged that way.

[bpo-41323](https://bugs.python.org/issue?@action=redirect&bpo=41323): Bytecode optimization now runs straight on the control flow graph. Under some conditions that yields marginally tighter code objects.

[bpo-41690](https://bugs.python.org/issue?@action=redirect&bpo=41690): Fixes a stack overflow the parser could hit while reading functions and classes that carry an enormous count of arguments. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

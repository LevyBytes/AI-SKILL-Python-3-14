# Stable ABI

### Stable ABI

To make that feasible, Python offers a *Stable ABI*: a collection of symbols guaranteed to stay ABI-compatible across Python 3.x versions.

Note

The Stable ABI heads off ABI trouble, such as linker errors from absent symbols or data corruption from shifts in structure layouts or function signatures. Even so, other Python changes can alter the *behavior* of extensions. Consult Python's Backwards Compatibility Policy ([**PEP 387**](https://peps.python.org/pep-0387/)) for the particulars.

Beyond the symbols surfaced in the Limited API, the Stable ABI holds additional ones – for example, functions required to keep older Limited API versions working.

Under Windows, extensions built on the Stable ABI ought to link against `python3.dll` instead of a version-pinned library like `python39.dll`.

On certain platforms, Python seeks out and loads shared library files carrying the `abi3` tag (for example `mymodule.abi3.so`). It performs no check that those extensions actually meet a Stable ABI. Ensuring that, say, extensions built against the 3.10+ Limited API never land on lower Python versions falls to the user (or to their packaging tools).

Within Python's shared library every Stable ABI function exists as a real function rather than merely a macro. That makes them reachable from languages that forgo the C preprocessor.

[Subject index](INDEX.md) · [Previous source contract](py-limited-api.md) · [Following source contract](limited-api-scope-and-performance.md)

# What's New In Python 3.3 / A Finer-Grained Import Lock

### A Finer-Grained Import Lock

CPython releases up to this point had consistently leaned on a single global import lock. That arrangement caused surprising headaches, for instance deadlocks whenever importing a module set off code execution in another thread as a side-effect. Awkward stopgaps occasionally got pressed into service, among them the [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock) C API function.

Under Python 3.3 a per-module lock is acquired when a module is imported. That properly serializes importing any single module across several threads — so partly built modules never leak out — and at the same time clears away the headaches noted above.

(Contributed by Antoine Pitrou in [bpo-9260](https://bugs.python.org/issue?@action=redirect&bpo=9260).)

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](builtin-functions-and-types.md) · [Release/subject declaration](summary-release-highlights.md)

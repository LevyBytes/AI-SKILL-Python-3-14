# What's New In Python 3.4 / PEP 451: A ModuleSpec Type for the Import System

### PEP 451: A ModuleSpec Type for the Import System

[**PEP 451**](https://peps.python.org/pep-0451/) furnishes an encapsulation of the details about a module that the import machinery relies on to load it (in other words, a module specification). This eases both the import implementation and a number of import-related APIs. It also serves as a stepping stone toward [several future import-related improvements](https://mail.python.org/pipermail/python-dev/2013-November/130111.html).

The PEP's public-facing alterations are completely backward-compatible. Beyond that, they ought to be invisible to all but importer authors. Although key finder and loader methods are now deprecated, they will keep functioning. Fresh importers ought to adopt the new methods the PEP describes. Existing importers ought to be revised to implement those new methods. Consult the Deprecated section for the roster of methods needing replacement along with their replacements.

[Subject index](INDEX.md) · [Previous source section](improvements-to-codec-handling.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](release-highlights.md)

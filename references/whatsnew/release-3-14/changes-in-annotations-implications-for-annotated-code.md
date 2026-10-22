# What's new in Python 3.14 / Changes in annotations (**PEP 649** and **PEP 749**) / Implications for annotated code

#### Implications for annotated code

Should you write annotations in your code (say, for a static type checker), this change very likely leaves you unaffected: you can carry on authoring annotations exactly as you did in earlier Python releases.

Quoted strings in annotations, so often used for forward references, will probably become removable. By the same token, if you depend on `from __future__ import annotations` to dodge writing annotation strings, you can quite possibly drop that import once your floor is Python 3.14 or later. That said, when you lean on third-party libraries that read annotations, those libraries may require updates to handle unquoted annotations before everything behaves as intended.

[Subject index](INDEX.md) · [Previous source section](changes-in-annotations.md) · [Next source section](annotation-reader-behavior-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](changes-in-annotations.md)

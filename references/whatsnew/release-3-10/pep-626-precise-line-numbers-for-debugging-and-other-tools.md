# What's New In Python 3.10 / PEP 626: Precise line numbers for debugging and other tools

### PEP 626: Precise line numbers for debugging and other tools

PEP 626 delivers sharper, more dependable line numbers aimed at debuggers, profilers and coverage tooling. Trace events carrying the right line number fire for every executed line of code, and solely for the lines that actually run.

A frame object's [`f_lineno`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lineno) attribute will at all times hold the line number you expect.

On [code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects), the [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) attribute is now deprecated and slated for removal in 3.12. Anything that has to translate an offset into a line number ought to switch to the fresh [`co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method.

[Subject index](INDEX.md) · [Previous source section](better-error-messages-nameerrors.md) · [Next source section](pep-634-structural-pattern-matching.md) · [Release/subject declaration](summary-release-highlights.md)

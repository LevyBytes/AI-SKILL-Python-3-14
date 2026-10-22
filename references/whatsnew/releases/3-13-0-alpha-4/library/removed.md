# Python 3.13.0 alpha 4 / library / removed

[gh-113951](https://github.com/python/cpython/issues/113951): Correct how the three-argument form of the `tag_unbind()` methods on `tkinter.Text` and `tkinter.Canvas` behaves. Earlier, `widget.tag_unbind(tag, sequence, funcid)` wiped out the present binding for *sequence*, left *sequence* unbound, and removed the *funcid* command. It now strips just *funcid* from the binding belonging to *sequence*, retains the remaining commands, and removes the *funcid* command. Only when *funcid* was the final bound command does it leave *sequence* unbound.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.12.0 alpha 1 / library / corrects default name generation tkinter checkbutton

[gh-73588](https://github.com/python/cpython/issues/73588): Corrects the default name generation for `tkinter.Checkbutton`. Formerly, checkbuttons under different parent widgets could end up with the same short name and share one state whenever the "name" and "variable" arguments went unspecified. They are now globally unique.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

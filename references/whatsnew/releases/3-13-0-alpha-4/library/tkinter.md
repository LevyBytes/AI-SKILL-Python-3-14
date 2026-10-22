# Python 3.13.0 alpha 4 / library / tkinter

[gh-43457](https://github.com/python/cpython/issues/43457): Repair the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) widget method `wm_attributes()`. To read window attributes it now takes the attribute name lacking the minus prefix, and it permits attributes and values to be supplied as keyword arguments for setting them. A new optional keyword argument *return_python_dict* arrives: invoking `w.wm_attributes(return_python_dict=True)` yields the attributes as a dict rather than a tuple. Invoking `w.wm_attributes()` now yields a tuple instead of a string whenever *wantobjects* had been set to 0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

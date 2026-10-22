# tkinter — `tkinter` — Python interface to Tcl/Tk

### `tkinter` — Python interface to Tcl/Tk

**Source code:** [Lib/tkinter/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/__init__.py)

---

Serving as the standard Python binding to the Tcl/Tk GUI toolkit, the `tkinter` package takes its name from “Tk interface”. You can find both Tk and `tkinter` across the majority of Unix platforms — macOS included — and on Windows machines too.

To confirm `tkinter` is set up correctly, run `python -m tkinter` at the command line; a window should appear that demonstrates a basic Tk interface. That window also reports which Tcl/Tk version you have, so you can consult the Tcl/Tk documentation that matches it.

A variety of Tcl/Tk versions work with Tkinter, whether those versions were compiled with thread support or without it. Tcl/Tk 8.6 threaded ships inside the official Python binary release. Consult the source of the `_tkinter` module if you want further detail on which versions are supported.

Rather than being a thin wrapper, Tkinter layers in a good deal of its own logic to give the toolkit a more pythonic feel. Accordingly, this documentation focuses on those additions and modifications, deferring to the official Tcl/Tk documentation for anything left unchanged.

Note

A modern collection of themed user interface components, together with a new API for using them, arrived with Tcl/Tk 8.5 (2007). The original API and the newer one both remain usable. A great deal of the documentation you encounter online continues to rely on the old API and may be badly out of date.

This is an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should it be absent from your CPython build, check for documentation supplied by your distributor (in other words, whoever handed you Python). If that distributor is you, consult [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

See also

- [TkDocs](https://tkdocs.com/)

A thorough tutorial on building user interfaces with Tkinter. It walks through the core concepts and demonstrates the recommended techniques using the modern API.

- [Tkinter 8.5 reference: a GUI for Python](https://www.tkdocs.com/shipman/)

Reference material for Tkinter 8.5 that documents the classes, methods, and options on offer.

Tcl/Tk Resources:

- [Tk commands](https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm)

A complete reference covering every one of the underlying Tcl/Tk commands that Tkinter relies on.

- [Tcl/Tk Home Page](https://www.tcl.tk)

Further documentation, plus links into the core development of Tcl/Tk.

Books:

- [Modern Tkinter for Busy Python Developers](https://tkdocs.com/book.html)

By Mark Roseman. (ISBN 978-1999149567)

- [Python GUI programming with Tkinter](https://www.packtpub.com/en-us/product/python-gui-programming-with-tkinter-9781788835886)

By Alan D. Moore. (ISBN 978-1788835886)

- [Programming Python](https://learning-python.com/about-pp4e.html)

By Mark Lutz; offers superb Tkinter coverage. (ISBN 978-0596158101)

- [Tcl and the Tk Toolkit (2nd edition)](https://www.amazon.com/exec/obidos/ASIN/032133633X)

By John Ousterhout — the creator of Tcl/Tk — and Ken Jones; Tkinter is not covered. (ISBN 978-0321336330)

[Subject index](INDEX.md) · [Continue](architecture.md)

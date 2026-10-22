# Graphical user interfaces with Tk — Section introduction and initial examples

### Graphical user interfaces with Tk

For a long while Tk/Tcl has been a core piece of Python. It supplies a dependable, platform-independent windowing toolkit that Python programmers reach through the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) package, plus its extension, the [`tkinter.ttk`](https://docs.python.org/3.14/library/tkinter.ttk.html#module-tkinter.ttk) module.

Sitting as a slim object-oriented layer over Tcl/Tk, the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) package means that to use `tkinter` you avoid writing Tcl code, though you'll still want to refer to the Tk documentation and, now and then, the Tcl documentation. `tkinter` is a collection of wrappers that expose the Tk widgets as Python classes.

The main strengths of [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) are its speed and the fact that it normally ships with Python. Its official documentation may be thin, yet plenty of solid material exists — references, tutorials, a book, and more. `tkinter` is likewise well known for a dated appearance, something greatly refined in Tk 8.5. Even so, plenty of other GUI libraries might appeal to you. Several alternative [GUI frameworks and tools](https://wiki.python.org/moin/GuiProgramming) are catalogued on the Python wiki.

- [`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3.14/library/tkinter.html)
  - [Architecture](https://docs.python.org/3.14/library/tkinter.html#architecture)
  - [Tkinter Modules](https://docs.python.org/3.14/library/tkinter.html#tkinter-modules)
  - [Tkinter Life Preserver](https://docs.python.org/3.14/library/tkinter.html#tkinter-life-preserver)
    - [A Hello World Program](https://docs.python.org/3.14/library/tkinter.html#a-hello-world-program)
    - [Important Tk Concepts](https://docs.python.org/3.14/library/tkinter.html#important-tk-concepts)
    - [Understanding How Tkinter Wraps Tcl/Tk](https://docs.python.org/3.14/library/tkinter.html#understanding-how-tkinter-wraps-tcl-tk)
    - [How do I…? What option does…?](https://docs.python.org/3.14/library/tkinter.html#how-do-i-what-option-does)
    - [Navigating the Tcl/Tk Reference Manual](https://docs.python.org/3.14/library/tkinter.html#navigating-the-tcl-tk-reference-manual)

  - [Threading model](https://docs.python.org/3.14/library/tkinter.html#threading-model)
  - [Handy Reference](https://docs.python.org/3.14/library/tkinter.html#handy-reference)
    - [Setting Options](https://docs.python.org/3.14/library/tkinter.html#setting-options)
    - [The Packer](https://docs.python.org/3.14/library/tkinter.html#the-packer)
    - [Packer Options](https://docs.python.org/3.14/library/tkinter.html#packer-options)
    - [Coupling Widget Variables](https://docs.python.org/3.14/library/tkinter.html#coupling-widget-variables)
    - [The Window Manager](https://docs.python.org/3.14/library/tkinter.html#the-window-manager)
    - [Tk Option Data Types](https://docs.python.org/3.14/library/tkinter.html#tk-option-data-types)
    - [Bindings and Events](https://docs.python.org/3.14/library/tkinter.html#bindings-and-events)
    - [The index Parameter](https://docs.python.org/3.14/library/tkinter.html#the-index-parameter)
    - [Images](https://docs.python.org/3.14/library/tkinter.html#images)

  - [File Handlers](https://docs.python.org/3.14/library/tkinter.html#file-handlers)

- [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3.14/library/tkinter.colorchooser.html)
- [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3.14/library/tkinter.font.html)
- [Tkinter Dialogs](https://docs.python.org/3.14/library/dialog.html)
  - [`tkinter.simpledialog` — Standard Tkinter input dialogs](https://docs.python.org/3.14/library/dialog.html#module-tkinter.simpledialog)
  - [`tkinter.filedialog` — File selection dialogs](https://docs.python.org/3.14/library/dialog.html#module-tkinter.filedialog)
    - [Native Load/Save Dialogs](https://docs.python.org/3.14/library/dialog.html#native-load-save-dialogs)

  - [`tkinter.commondialog` — Dialog window templates](https://docs.python.org/3.14/library/dialog.html#module-tkinter.commondialog)

- [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3.14/library/tkinter.messagebox.html)
- [`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3.14/library/tkinter.scrolledtext.html)
- [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3.14/library/tkinter.dnd.html)

[Subject index](INDEX.md) · [Previous](graphical-user-interfaces-with-tk.md) · [Continue](ttk-widget-routes.md)

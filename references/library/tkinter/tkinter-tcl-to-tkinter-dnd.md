# tkinter: `tkinter.Tcl()`, `tkinter.colorchooser`, `tkinter.commondialog`, `tkinter.filedialog`, `tkinter.font`, `tkinter.messagebox`, `tkinter.scrolledtext`, `tkinter.simpledialog`, `tkinter.ttk`, `tkinter.constants`, `tkinter.dnd`

tkinter.Tcl(*screenName=None*, *baseName=None*, *className='Tk'*, *useTk=False*)

A factory function, `Tcl()` produces an object quite similar to what the `Tk` class produces, with the difference that it leaves the Tk subsystem uninitialized. It comes in handy mainly when you want to drive the Tcl interpreter somewhere you’d rather not spawn extra toplevel windows, or somewhere you can’t (think Unix/Linux systems lacking an X server). An object made by the `Tcl()` object can later gain a Toplevel window (and initialize the Tk subsystem) through a call to its `loadtk()` method.

Among the modules that deliver Tk support are:

`tkinter`

The principal Tkinter module.

[`tkinter.colorchooser`](https://docs.python.org/3.14/library/tkinter.colorchooser.html#module-tkinter.colorchooser)

A dialog allowing the user to pick a color.

[`tkinter.commondialog`](https://docs.python.org/3.14/library/dialog.html#module-tkinter.commondialog)

The base class behind the dialogs declared in the remaining modules in this list.

[`tkinter.filedialog`](https://docs.python.org/3.14/library/dialog.html#module-tkinter.filedialog)

Standard dialogs that let the user nominate a file to open or to save.

[`tkinter.font`](https://docs.python.org/3.14/library/tkinter.font.html#module-tkinter.font)

Helpers for working with fonts.

[`tkinter.messagebox`](https://docs.python.org/3.14/library/tkinter.messagebox.html#module-tkinter.messagebox)

A gateway to the standard Tk dialog boxes.

[`tkinter.scrolledtext`](https://docs.python.org/3.14/library/tkinter.scrolledtext.html#module-tkinter.scrolledtext)

A Text widget that comes with a vertical scroll bar already attached.

[`tkinter.simpledialog`](https://docs.python.org/3.14/library/dialog.html#module-tkinter.simpledialog)

Elementary dialogs plus convenience functions.

[`tkinter.ttk`](https://docs.python.org/3.14/library/tkinter.ttk.html#module-tkinter.ttk)

The themed widget set that debuted in Tk 8.5, offering modern stand-ins for many of the classic widgets found in the main `tkinter` module.

Additional modules:

`_tkinter`

A binary module holding the low-level interface to Tcl/Tk. The main `tkinter` module imports it automatically, and application programmers should never touch it directly. It typically takes the form of a shared library (or DLL), though it can occasionally be linked statically into the Python interpreter.

[`idlelib`](https://docs.python.org/3.14/library/idle.html#module-idlelib)

Python’s Integrated Development and Learning Environment (IDLE), which is built on `tkinter`.

`tkinter.constants`

Symbolic constants you can supply in place of strings when feeding assorted parameters to Tkinter calls. The main `tkinter` module imports it automatically.

[`tkinter.dnd`](https://docs.python.org/3.14/library/tkinter.dnd.html#module-tkinter.dnd)

(experimental) Drag-and-drop support for `tkinter`. It will be deprecated once the Tk DND replacement lands.

[`turtle`](https://docs.python.org/3.14/library/turtle.html#module-turtle)

Turtle graphics rendered inside a Tk window.

[Subject index](INDEX.md) · [Previous](tkinter-modules.md) · [Continue](tkinter-life-preserver.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md) · [Owning module, declaration or section: Tkinter Modules](tkinter-modules.md)

# tkinter - Navigating the Tcl/Tk Reference Manual

### Navigating the Tcl/Tk Reference Manual

As mentioned, the official [Tk commands](https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm) reference manual (man pages) frequently gives the most accurate account of what particular widget operations do. Even once you know the name of the option or method you need, there may still be a couple of spots worth checking.

While every operation in Tkinter is realized as a method call on widget objects, you’ve seen that plenty of Tcl/Tk operations turn up as commands whose first parameter is a widget pathname, followed by optional parameters, e.g.

```python
destroy .
grid .frm.btn -column 0 -row 0

```

Others, though, look closer to methods invoked on a widget object (indeed, when you create a widget in Tcl/Tk, it sets up a Tcl command bearing the name of the widget pathname, and that command’s first parameter is the name of a method to call).

```python
.frm.btn invoke
.frm.lbl configure -text "Goodbye"

```

Within the official Tcl/Tk reference documentation, you’ll come across most method-call-style operations on the man page for a given widget (for example, the `invoke()` method shows up on the [ttk::button](https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_button.htm) man page), whereas functions that take a widget as a parameter frequently get a man page to themselves (for example, [grid](https://www.tcl.tk/man/tcl8.6/TkCmd/grid.htm)).

Many common options and methods turn up on the [options](https://www.tcl.tk/man/tcl8.6/TkCmd/options.htm) or [ttk::widget](https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_widget.htm) man pages, while others live in the man page for a particular widget class.

You’ll also notice that a lot of Tkinter methods carry compound names, e.g., `winfo_x()`, `winfo_height()`, `winfo_viewable()`. Documentation for all of these resides in the [winfo](https://www.tcl.tk/man/tcl8.6/TkCmd/winfo.htm) man page.

Note

A bit confusingly, every Tkinter widget also carries methods that don’t actually act on the widget at all but instead operate at a global scope, independent of any widget. Examples include the methods for reaching the clipboard or the system bell. (They just happen to be implemented as methods on the base `Widget` class from which all Tkinter widgets inherit.)

[Subject index](INDEX.md) · [Previous](how-do-i-what-option-does.md) · [Continue](threading-model.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)

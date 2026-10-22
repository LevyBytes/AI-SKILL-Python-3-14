# tkinter.colorchooser — `tkinter.colorchooser` — Color choosing dialog

## tkinter.colorchooser — Color choosing dialog

### `tkinter.colorchooser` — Color choosing dialog

**Source code:** [Lib/tkinter/colorchooser.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/colorchooser.py)

---

As a front end to the platform's native color picker dialog, the `tkinter.colorchooser` module supplies the `Chooser` class. `Chooser` puts up a modal color choosing dialog window. The `Chooser` class derives from the [`Dialog`](https://docs.python.org/3.14/library/dialog.html#tkinter.commondialog.Dialog) class.

 *class *tkinter.colorchooser.Chooser(*master=None*, ***options*)

 tkinter.colorchooser.askcolor(*color=None*, ***options*)

Open a color choosing dialog. Invoking this method displays the window, pauses until the user picks something, and hands the chosen color (or `None`) back to the caller.

See also

Module [`tkinter.commondialog`](https://docs.python.org/3.14/library/dialog.html#module-tkinter.commondialog)

Tkinter standard dialog module

[Subject index](INDEX.md) · [Continue](../tkinter-dnd/tkinter-dnd-dndhandler-class.md)

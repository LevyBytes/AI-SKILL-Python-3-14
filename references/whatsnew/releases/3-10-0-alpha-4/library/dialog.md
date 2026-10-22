# Python 3.10.0 alpha 4 / library / dialog

[bpo-42721](https://bugs.python.org/issue?@action=redirect&bpo=42721): Suppose simple query dialogs ([`tkinter.simpledialog`](https://docs.python.org/3.14/library/dialog.html#module-tkinter.simpledialog)), message boxes ([`tkinter.messagebox`](https://docs.python.org/3.14/library/tkinter.messagebox.html#module-tkinter.messagebox)) or the color choose dialog ([`tkinter.colorchooser`](https://docs.python.org/3.14/library/tkinter.colorchooser.html#module-tkinter.colorchooser)) get built with neither *master* nor *parent* supplied, while no default root window exists yet and `NoDefaultRoot()` was never invoked. In that situation a fresh temporal hidden root window is spun up on its own. That window is not registered as the default root and is torn down the moment the dialog window closes. This makes such simple dialog windows usable from programs that want no further GUI.

[bpo-42685](https://bugs.python.org/issue?@action=redirect&bpo=42685): Refined where simple query windows land in Tkinter (for example [`tkinter.simpledialog.askinteger()`](https://docs.python.org/3.14/library/dialog.html#tkinter.simpledialog.askinteger)). When a parent window is given and visible they sit at its center; otherwise they appear at the middle of the screen.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

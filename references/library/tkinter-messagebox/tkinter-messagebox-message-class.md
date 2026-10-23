# tkinter.messagebox: `tkinter.messagebox.Message`

### `tkinter.messagebox` - Tkinter message prompts

**Source code:** [Lib/tkinter/messagebox.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/messagebox.py)

---

A reusable base class plus an assortment of handy methods for the configurations people reach for most are what the `tkinter.messagebox` module gives you. These boxes are modal and, depending on what the user picks, hand back one of (`True`, `False`, `None`, `OK`, `CANCEL`, `YES`, `NO`). Typical message box styles and layouts run to (and are not capped at):

  (Figure: ../_images/tk_msg.png)

 *class *tkinter.messagebox.Message(*master=None*, ***options*)

Build a message window carrying a message your application supplies, an icon, and a group of buttons. Every button in that window goes by its own distinct symbolic name (check the *type* options).

These are the options you can set:

>

*command*

Names the function to call once the user dismisses the dialog. Whichever button the user clicked to close it has its name handed to that function as an argument. Only macOS offers this.

*default*

Supplies the symbolic name of this window's default button (`OK`, `CANCEL`, and the like). Leave this option out and the dialog's first button becomes the default.

*detail*

Adds a secondary note alongside the primary text set by the *message* option. This detail shows up below the primary text and, on operating systems that allow it, in a font with less emphasis than the primary text.

*icon*

Picks which icon appears. With this option left unset, the `INFO` icon shows instead.

*message*

Sets the text shown inside this message box. It defaults to an empty string.

*parent*

Designates the given window as the message box's logical parent. The box then appears layered above that parent window.

*title*

Sets a string to serve as the message box's title. macOS disregards this option, since its platform guidelines bar a title on a dialog of this sort.

*type*

Causes one of the built-in button groups to be shown.

[Subject index](INDEX.md) · [Previous](tkinter-message-prompts.md) · [Continue](tkinter-messagebox-message-show.md)

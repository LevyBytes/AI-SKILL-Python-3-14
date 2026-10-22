# tkinter.messagebox: Information, warning, error and confirmation dialogs

tkinter.messagebox.showinfo(*title=None*, *message=None*, ***options*)

Builds and pops up an information box carrying the title and message you provide.

**Warning message boxes**

 tkinter.messagebox.showwarning(*title=None*, *message=None*, ***options*)

Builds and pops up a warning box carrying the title and message you provide.

 tkinter.messagebox.showerror(*title=None*, *message=None*, ***options*)

Builds and pops up an error box carrying the title and message you provide.

**Question message boxes**

 tkinter.messagebox.askquestion(*title=None*, *message=None*, ***, *type=YESNO*, ***options*)

Pose a question. Its buttons are `YES` and `NO` by default. Hands back the symbolic name of the button that was chosen.

 tkinter.messagebox.askokcancel(*title=None*, *message=None*, ***options*)

Check whether the operation ought to go ahead. Presents `OK` and `CANCEL` buttons. Yields `True` when the reply is ok and `False` in every other case.

 tkinter.messagebox.askretrycancel(*title=None*, *message=None*, ***options*)

Check whether the operation ought to be attempted again. Presents `RETRY` and `CANCEL` buttons. Gives back `True` for a yes reply and `False` in every other case.

 tkinter.messagebox.askyesno(*title=None*, *message=None*, ***options*)

Pose a question. Presents `YES` and `NO` buttons. Gives back `True` for a yes reply and `False` in every other case.

[Subject index](INDEX.md) · [Previous](tkinter-messagebox-message-show.md) · [Continue](tkinter-messagebox-askyesnocancel.md) · [Owning module, declaration or section: tkinter.messagebox](tkinter-messagebox-message-class.md)

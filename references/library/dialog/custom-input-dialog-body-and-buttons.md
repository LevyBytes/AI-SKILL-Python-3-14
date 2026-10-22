# tkinter.simpledialog / Standard Tkinter input dialogs: `tkinter.simpledialog.Dialog`, `body()`, `buttonbox()`

*class *tkinter.simpledialog.Dialog(*parent*, *title=None*)

Serves as the parent class from which custom dialogs derive.

 body(*master*)

Override this to assemble the dialog’s interface and hand back whichever widget ought to hold focus at first.

 buttonbox()

By default this puts up OK and Cancel buttons. Override it when you want a different button arrangement.

[Subject index](INDEX.md) · [Previous](float-integer-and-string-input-dialogs.md) · [Continue](tkinter-filedialog-file-selection-dialogs.md)

# tkinter.filedialog: Native file and directory selection dialogs

### Native Load/Save Dialogs

The classes and functions below put up file dialog windows that pair a native look-and-feel with settings for tailoring how they behave. These keyword arguments apply to the classes and functions that follow:

>   *parent* - the window over which the dialog is laid   *title* - what the window’s title bar reads   *initialdir* - the folder the dialog opens into   *initialfile* - the file already chosen as the dialog appears   *filetypes* - a series of (label, pattern) tuples, with the ‘*’ wildcard permitted   *defaultextension* - the extension tacked on by default (for save dialogs)   *multiple* - when set true, picking several items at once is allowed

**Static factory functions**

When invoked, the functions below raise a modal dialog with a native look-and-feel, pause for the user to choose, and then pass the chosen value(s) — or `None` — back to the caller.

 tkinter.filedialog.askopenfile(*mode='r'*, ***options*)

 tkinter.filedialog.askopenfiles(*mode='r'*, ***options*)

Both functions above bring up an `Open` dialog and hand back the file object(s) opened in read-only mode.

 tkinter.filedialog.asksaveasfile(*mode='w'*, ***options*)

Brings up a `SaveAs` dialog and hands back a file object opened in write-only mode.

 tkinter.filedialog.askopenfilename(***options*)

 tkinter.filedialog.askopenfilenames(***options*)

Both functions above bring up an `Open` dialog and hand back the chosen filename(s) matching file(s) that already exist.

 tkinter.filedialog.asksaveasfilename(***options*)

Brings up a `SaveAs` dialog and hands back the chosen filename.

 tkinter.filedialog.askdirectory(***options*)

 Asks the user to pick a directory. One extra keyword option applies:  *mustexist* - sets whether the pick has to be a directory that already exists.

[Subject index](INDEX.md) · [Previous](tkinter-filedialog-file-selection-dialogs.md) · [Continue](native-open-and-save-dialog-classes.md)

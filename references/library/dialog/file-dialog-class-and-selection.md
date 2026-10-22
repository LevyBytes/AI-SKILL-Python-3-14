# tkinter.filedialog / Native Load/Save Dialogs: FileDialog selection, filtering and event methods

*class *tkinter.filedialog.FileDialog(*master*, *title=None*)

Builds a no-frills file selection dialog.

 cancel_command(*event=None*)

Kicks off the closing of the dialog window.

 dirs_double_event(*event*)

Handles the double-click event landing on a directory.

 dirs_select_event(*event*)

Handles the click event landing on a directory.

 files_double_event(*event*)

Handles the double-click event landing on a file.

 files_select_event(*event*)

Handles the single-click event landing on a file.

 filter_command(*event=None*)

Narrows the files down by directory.

 get_filter()

Fetches whichever file filter is active right now.

 get_selection()

Fetches the item that is currently picked.

 go(*dir_or_file=os.curdir*, *pattern='*'*, *default=''*, *key=None*)

Draws the dialog and kicks off the event loop.

 ok_event(*event*)

Leaves the dialog, handing back the current pick.

 quit(*how=None*)

Leaves the dialog, handing back a filename if there is one.

 set_filter(*dir*, *pat*)

Establishes the file filter.

 set_selection(*file*)

Switches the current file pick over to *file*.

[Subject index](INDEX.md) · [Previous](tkinter-filedialog-directory-class.md) · [Continue](load-file-dialog-validation.md) · [Owning module, declaration or section: Native Load/Save Dialogs](file-and-directory-selection-functions.md)

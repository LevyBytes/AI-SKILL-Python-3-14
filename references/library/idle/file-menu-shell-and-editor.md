# File menu (Shell and Editor)

### File menu (Shell and Editor)

New File

Create a new file editing window.

Open…

Open an existing file with an Open dialog.

Open Module…

Open an existing module (searches sys.path).

Recent Files

Open a list of recent files. Click one to open it.

Module Browser

Display the functions, classes, and methods of the current Editor file as a tree. From the shell, open a module beforehand.

Path Browser

Display sys.path directories, modules, functions, classes and methods as a tree.

Save

Write the current window back to its associated file, when one exists. A window altered since it was opened or last saved shows a * surrounding the window title. When no associated file exists, Save As is used instead.

Save As…

Write the current window through a Save As dialog. Whatever file you save to becomes that window’s new associated file. (When your file manager hides extensions, the present extension is dropped from the file name box. When the new filename contains no ‘.’, ‘.py’ and ‘.txt’ are appended for Python and text files respectively, though under macOS Aqua ’.py’ is appended to every file.)

Save Copy As…

Write the current window out to another file while leaving the associated file unchanged. (Refer to the Save As note above regarding filename extensions.)

Print Window

Print the current window to the default printer.

Close Window

Close the current window (when an editor has unsaved edits, prompt to save; when a Shell is unsaved, prompt to quit execution). Invoking `exit()` or `close()` within the Shell window likewise closes Shell. When this happens to be the lone window, IDLE exits as well.

Exit IDLE

Close all windows and quit IDLE (ask to save unsaved edit windows).

[Subject index](INDEX.md) · [Previous](menus.md) · [Continue](edit-menu-shell-and-editor.md)

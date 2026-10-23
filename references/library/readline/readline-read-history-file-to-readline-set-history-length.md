# readline - History file

### History file

The functions below act on a history file:

 readline.read_history_file([*filename*])

Read a readline history file and add its contents onto the history list. When no filename is given, the default is `~/.history`. This invokes `read_history()` in the underlying library and raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` carrying the file name when supplied and `"~/.history"` if not.

Changed in version 3.14: The auditing event was added.

 readline.write_history_file([*filename*])

Write the history list out to a readline history file, replacing whatever file may already be there. When no filename is given, the default is `~/.history`. This invokes `write_history()` in the underlying library and raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` carrying the file name when supplied and `"~/.history"` if not.

Changed in version 3.14: The auditing event was added.

 readline.append_history_file(*nelements*[, *filename*])

Add the most recent *nelements* history items onto a file. When no filename is given, the default is `~/.history`. That file has to exist beforehand. Underneath this invokes `append_history()` in the library. This function is present only when Python was built against a library version that provides it. It raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` carrying the file name when supplied and `"~/.history"` if not.

Added in version 3.5.

Changed in version 3.14: The auditing event was added.

 readline.get_history_length()

 readline.set_history_length(*length*)

Read or assign the number of lines you want kept in the history file. The `write_history_file()` function relies on this value when trimming the history file, by invoking `history_truncate_file()` in the underlying library. A negative value means the history file has no size cap.

[Subject index](INDEX.md) · [Previous](readline-get-line-buffer-to-readline-redisplay.md) · [Continue](readline-clear-history-to-readline-set-auto-history.md) · [Owning module, declaration or section: readline](readline-backend.md)

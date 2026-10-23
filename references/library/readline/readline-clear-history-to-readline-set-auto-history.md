# readline - History list

### History list

The functions below act on a global history list:

 readline.clear_history()

Wipe out the current history. Underneath this invokes `clear_history()` in the library. The Python function is present only when Python was built against a library version that provides it.

 readline.get_current_history_length()

Give back how many items the history holds right now. (Contrast with `get_history_length()`, which gives the upper bound on lines that a history file will receive.)

 readline.get_history_item(*index*)

Give back what history item at *index* currently holds. Item indexing starts from one. Underneath this invokes `history_get()` in the library.

 readline.remove_history_item(*pos*)

Delete the history item identified by its position out of the history. Position numbering starts from zero. Underneath this invokes `remove_history()` in the library.

 readline.replace_history_item(*pos*, *line*)

Swap the history item identified by its position for *line*. Position numbering starts from zero. Underneath this invokes `replace_history_entry()` in the library.

 readline.add_history(*line*)

Add *line* onto the history buffer, as though it were the most recent line typed. Underneath this invokes `add_history()` in the library.

 readline.set_auto_history(*enabled*)

Switch automatic invocations of `add_history()` on or off when input is read through readline. The *enabled* argument is expected to be a Boolean: a true value switches auto history on, and a false value switches it off.

Added in version 3.6.

**CPython implementation detail:** Auto history starts out enabled, and any change you make to it will not carry over between separate sessions.

[Subject index](INDEX.md) · [Previous](readline-read-history-file-to-readline-set-history-length.md) · [Continue](readline-set-startup-hook-to-readline-set-pre-input-hook.md) · [Owning module, declaration or section: readline](readline-backend.md)

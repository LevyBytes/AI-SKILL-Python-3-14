# readline - Line buffer

### Line buffer

The functions below act on the line buffer:

 readline.get_line_buffer()

Give back what the line buffer currently holds (`rl_line_buffer` in the underlying library).

 readline.insert_text(*string*)

Place text into the line buffer where the cursor sits. Underneath this invokes `rl_insert_text()` in the library, while disregarding the return value.

 readline.redisplay()

Update the screen contents so they match what the line buffer currently holds. Underneath this invokes `rl_redisplay()` in the library.

[Subject index](INDEX.md) · [Previous](readline-parse-and-bind-to-readline-read-init-file.md) · [Continue](readline-read-history-file-to-readline-set-history-length.md) · [Owning module, declaration or section: readline](readline-backend.md)

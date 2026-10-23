# code - Interactive Console Objects

### Interactive Console Objects

Being derived from `InteractiveInterpreter`, the `InteractiveConsole` class inherits every method the interpreter objects expose and tacks on the extras described below.

 InteractiveConsole.interact(*banner=None*, *exitmsg=None*)

Mimics the interactive Python console quite faithfully. The optional *banner* argument names the banner shown ahead of the very first interaction; left unset, it prints something resembling the standard Python interpreter's banner, then appends — inside parentheses — the console object's class name, so you won't mistake it for the actual interpreter (which it resembles closely!).

The optional *exitmsg* argument sets the exit message shown on the way out. Hand it the empty string and no exit message appears. Leave *exitmsg* off, or set it to `None`, and a default message is shown.

Changed in version 3.4: Hand in an empty string and no banner is printed at all.

Changed in version 3.6: Print an exit message when exiting.

 InteractiveConsole.push(*line*)

Feeds one line of source text into the interpreter. That line must not end with a trailing newline, though newlines within it are fine. It is tacked onto a buffer, after which the interpreter's `runsource()` method runs against the buffer's joined-together contents as the source. When that signals the command ran or was invalid, the buffer is cleared; otherwise the command is still unfinished and the buffer stays exactly as it stood once the line was added. A return of `True` means more input is needed, while `False` means the line was handled somehow — matching what `runsource()` reports.

 InteractiveConsole.resetbuffer()

Remove any unhandled source text from the input buffer.

 InteractiveConsole.raw_input(*prompt=''*)

Prints a prompt, then reads back a single line. What it returns leaves off the trailing newline. Entering the EOF key sequence at this point makes [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError) fire. By default the line comes from `sys.stdin`, but a subclass is free to swap in some other source.

[Subject index](INDEX.md) · [Previous](interactive-interpreter-execution-and-output.md) · [Owning module, declaration or section: code](code-interactiveinterpreter-class.md)

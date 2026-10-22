# code: `code.InteractiveConsole`

*class *code.InteractiveConsole(*locals=None*, *filename='&lt;console&gt;'*, *local_exit=False*)

Reproduces, down to fine detail, how the interactive Python interpreter acts. Layered on top of `InteractiveInterpreter`, this class throws in input buffering plus prompting driven by the well-known `sys.ps1` and `sys.ps2`. Should *local_exit* be true, invoking `exit()` and `quit()` at the console no longer triggers [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit); control simply returns to whatever called it.

Changed in version 3.13: Added *local_exit* parameter.

[Subject index](INDEX.md) · [Previous](code-interactiveinterpreter-class.md) · [Continue](code-interact-to-code-compile-command.md) · [Owning module, declaration or section: code](code-interactiveinterpreter-class.md)

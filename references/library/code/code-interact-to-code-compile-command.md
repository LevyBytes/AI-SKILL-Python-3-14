# code: `code.interact()`, `code.compile_command()`

code.interact(*banner=None*, *readfunc=None*, *local=None*, *exitmsg=None*, *local_exit=False*)

A shorthand helper for spinning up a read-eval-print loop. It instantiates a fresh `InteractiveConsole` and, when *readfunc* is supplied, wires that in as the `InteractiveConsole.raw_input()` method. A supplied *local* gets forwarded to the `InteractiveConsole` constructor to act as the default namespace for the loop, and a supplied *local_exit* is likewise handed to the `InteractiveConsole` constructor. After this, the instance's `interact()` method runs, with *banner* and *exitmsg* — when given — serving as the banner and the exit message. Once it finishes, the console object is thrown away.

Changed in version 3.6: Added *exitmsg* parameter.

Changed in version 3.13: Added *local_exit* parameter.

 code.compile_command(*source*, *filename='&lt;input&gt;'*, *symbol='single'*)

Programs aiming to mimic Python's interpreter main loop — otherwise known as the read-eval-print loop — will find this function handy. Its hard job is spotting when what the user typed is an unfinished command that further text could round out, versus a finished command or an outright syntax error. In practice it lands on the *almost* identical verdict that the genuine interpreter main loop would.

Here *source* holds the source string; *filename*, optional, names the file the source came from and falls back to `'<input>'`; and *symbol*, also optional, is the grammar start symbol, expected to be `'single'` (its default), `'eval'` or `'exec'`.

For a command that is both finished and valid, it yields a code object (identical to what `compile(source, filename, symbol)` gives); for one still unfinished, it yields `None`. A finished command bearing a syntax mistake makes it raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), whereas a command carrying an invalid literal makes it raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

[Subject index](INDEX.md) · [Previous](code-interactiveconsole-class.md) · [Continue](interactive-interpreter-execution-and-output.md) · [Owning module, declaration or section: code](code-interactiveinterpreter-class.md)

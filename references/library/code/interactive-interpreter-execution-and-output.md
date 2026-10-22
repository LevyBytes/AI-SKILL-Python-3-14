# code — Interactive Interpreter Objects

### Interactive Interpreter Objects

 InteractiveInterpreter.runsource(*source*, *filename='&lt;input&gt;'*, *symbol='single'*)

Compiles a chunk of source and executes it inside the interpreter. It takes the same arguments `compile_command()` does; *filename* defaults to `'<input>'` and *symbol* to `'single'`. From here, any of a few outcomes may follow:

- The supplied input was faulty, so `compile_command()` threw an exception ([`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) or [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError)). A syntax traceback then gets printed via the `showsyntaxerror()` method, and `runsource()` hands back `False`.

- The input remains unfinished and additional text is needed, so `compile_command()` gave back `None`; in turn `runsource()` returns `True`.

- The input is finished, so `compile_command()` produced a code object. That code then runs through a call to `runcode()` — which also copes with run-time exceptions, [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) aside — and `runsource()` returns `False`.

You can read the return value to choose between `sys.ps1` and `sys.ps2` when prompting for the following line.

 InteractiveInterpreter.runcode(*code*)

Runs a code object. Should an exception arise, `showtraceback()` fires to show a traceback. Every exception is trapped apart from [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), which is permitted to bubble up.

One caveat regarding [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt): it can fire somewhere else within this code and might slip past unhandled, so whoever calls this should be ready to handle it themselves.

 InteractiveInterpreter.showsyntaxerror(*filename=None*)

Shows the syntax error that has just happened. No stack trace appears, since syntax errors don't carry one. When *filename* is supplied, it gets pushed into the exception in place of the default name Python's parser would use — that parser always reports `'<string>'` while reading from a string. Emitting the output is handled by the `write()` method.

 InteractiveInterpreter.showtraceback()

Shows the exception that has just happened. The leading stack item is dropped, since it sits inside the interpreter object's own implementation. Emitting the output is the job of the `write()` method.

Changed in version 3.5: Rather than only the primary traceback, the complete chained traceback now appears.

 InteractiveInterpreter.write(*data*)

Sends a string to the standard error stream (`sys.stderr`). Subclasses are expected to override it so they can supply whatever output handling suits their needs.

[Subject index](INDEX.md) · [Previous](code-interact-to-code-compile-command.md) · [Continue](interactiveconsole-interact-to-interactiveconsole-raw-input.md) · [Owning module, declaration or section: code](code-interactiveinterpreter-class.md)

# pdb / Command-line interface: `pdb.Pdb`, `run()`, `runeval()`, `runcall()`, `set_trace()`

*class *pdb.Pdb(*completekey='tab'*, *stdin=None*, *stdout=None*, *skip=None*, *nosigint=False*, *readrc=True*, *mode=None*, *backend=None*, *colorize=False*)

`Pdb` is the debugger class.

The *completekey*, *stdin* and *stdout* arguments get handed down to the underlying [`cmd.Cmd`](https://docs.python.org/3.14/library/cmd.html#cmd.Cmd) class, which is documented there.

When supplied, the *skip* argument has to be an iterable of glob-style module-name patterns. Frames originating in any module that matches one of those patterns are skipped over by the debugger. [1]

Out of the box, Pdb installs a handler for the SIGINT signal (delivered when the user presses Ctrl-C at the console) whenever you issue a `continue` command. That lets you re-enter the debugger by hitting Ctrl-C. To keep Pdb from altering the SIGINT handler, set *nosigint* to true.

Defaulting to true, the *readrc* argument decides whether Pdb reads .pdbrc files off the filesystem.

How the debugger was launched is conveyed by the *mode* argument, which influences how certain commands behave. The permitted values are `'inline'` (what the breakpoint() builtin passes), `'cli'` (what the command-line launch passes), or `None` (giving the backwards-compatible behaviour that existed prior to the addition of the *mode* argument).

Which backend the debugger uses is set by the *backend* argument. Passing `None` selects the default backend; see `set_default_backend()`. Otherwise the available backends are `'settrace'` and `'monitoring'`.

When *colorize* is `True`, the debugger emits colorized output where color is supported. Source code shown in pdb is highlighted as a result.

Example call to enable tracing with *skip*:

```python
import pdb; pdb.Pdb(skip=['django.*']).set_trace()

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `pdb.Pdb` with no arguments.

Changed in version 3.1: Added the *skip* parameter.

Changed in version 3.2: Added the *nosigint* parameter. Before this, Pdb never installed a SIGINT handler.

Changed in version 3.6: The *readrc* argument.

Added in version 3.14: Added the *mode* argument.

Added in version 3.14: Added the *backend* argument.

Added in version 3.14: Added the *colorize* argument.

Changed in version 3.14: Inline breakpoints such as [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) or `pdb.set_trace()` now always halt the program at the calling frame and disregard the *skip* pattern (when one is present).

 run(*statement*, *globals=None*, *locals=None*)

 runeval(*expression*, *globals=None*, *locals=None*)

 runcall(*function*, **args*, ***kwds*)

 set_trace()

See the documentation for the functions explained above.

[Subject index](INDEX.md) · [Previous](pdb-runeval-to-pdb-get-default-backend.md) · [Continue](debugger-commands-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Command-line interface](pdb-run.md)

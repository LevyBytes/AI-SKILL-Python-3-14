# pdb / Debugger commands: Debugger statement execution, restart and quit commands

unalias name

Remove the alias identified by *name*.

 ! statement

Run the single-line *statement* within the current stack frame's context. You may leave off the exclamation point, unless the statement's opening word looks like it could be a debugger command, for instance:

```none
(Pdb) ! n=42
(Pdb)

```

If you want to assign a global variable, put a [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) statement ahead of the assignment on that same line, for example:

```none
(Pdb) global list_options; list_options = ['-l']
(Pdb)

```

 run [args ...]

 restart [args ...]

Begin the Python program under debug again from the start. When *args* is given, it gets tokenized via [`shlex`](https://docs.python.org/3.14/library/shlex.html#module-shlex), and the outcome becomes the fresh [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv). Your history, breakpoints, actions, and debugger settings all carry over. The name `restart` is simply an alias for `run`.

Changed in version 3.14: the `run` and `restart` commands no longer function whenever the debugger has been started in `'inline'` mode.

 q(uit)

Leave the debugger. Whatever program was running gets aborted. Feeding it an end-of-file does the same thing as `quit`.

Should the debugger have started in `'inline'` mode, you'll be asked to confirm first. Any of `y`, `Y`, `<Enter>` or `EOF` counts as confirmation to quit.

Changed in version 3.14: When the debugger was launched in `'inline'` mode, a confirmation prompt now appears. Once you confirm, the debugger calls [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) right away rather than raising [`bdb.BdbQuit`](https://docs.python.org/3.14/library/bdb.html#bdb.BdbQuit) on the following trace event.

 debug code

Drop into a nested debugger that walks through *code* — any expression or statement you want evaluated within the present environment.

[Subject index](INDEX.md) · [Previous](pdb-alias-command.md) · [Continue](debugger-commands.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Debugger commands](debugger-commands-section-introduction-and-initial-examples.md)

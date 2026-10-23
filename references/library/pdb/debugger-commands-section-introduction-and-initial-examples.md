# pdb - Debugger commands - Section introduction and initial examples

### Debugger commands

What follows is the set of commands the debugger understands. Most of them have a one- or two-letter shorthand, shown in the notation below; for instance, `h(elp)` indicates that `h` or `help` both invoke the help command (whereas `he` or `hel` do not, and neither do `H`, `Help`, or `HELP`). Whitespace (spaces or tabs) must separate a command from its arguments. Optional arguments sit inside square brackets (`[]`) in the syntax; you do not type the brackets themselves. A vertical bar (`|`) separates alternatives in the syntax.

Submitting an empty line re-runs the previous command. The exception: when the prior command was `list`, the following 11 lines get listed.

Input the debugger does not recognize as a command is treated as Python statements and run in the scope of the program under debug. You may also place an exclamation point (`!`) in front of Python statements. This gives you a strong way to probe the program being debugged; you can even reassign a variable or invoke a function. Should a statement like that raise, the exception's name is shown, but the debugger's state stays the same.

Changed in version 3.13: Expressions and statements that begin with a pdb command prefix are now recognized and run correctly.

Aliases are supported by the debugger. Because aliases can take parameters, they give you some flexibility to suit whatever context you are inspecting.

You can put several commands on one line, separating them with `;;`. (A lone `;` is avoided because it serves as the separator between multiple commands on a line handed to the Python parser.) The splitting is naive: the input breaks at the first `;;` pair, even when that pair sits inside a quoted string. For strings that contain double semicolons, a workaround is implicit string concatenation: `';'';'` or `";"";"`.

To define a throwaway global variable, reach for a *convenience variable*. A *convenience variable* is one whose name begins with `$`. As an example, `$foo = 1` defines a global `$foo` usable throughout the debugger session. Because *convenience variables* are wiped when the program resumes, they are less prone to clash with your program than ordinary variables such as `foo = 1`.

The four built-in *convenience variables* are:

- `$_frame`: the current frame you are debugging

- `$_retval`: the return value if the frame is returning

- `$_exception`: the exception if the frame is raising an exception

- `$_asynctask`: the asyncio task if pdb stops in an async function

Added in version 3.12: Added the *convenience variable* feature.

Added in version 3.14: Added the `$_asynctask` convenience variable.

When a `.pdbrc` file is present in the user's home directory or the working directory, it is read using `'utf-8'` encoding and run as though entered at the debugger prompt, except that blank lines and lines beginning with `#` are skipped. That makes it especially handy for aliases. When both files are present, the home-directory one is read first, and aliases set there can be replaced by the local file.

Changed in version 3.2: `.pdbrc` may now hold commands that resume debugging, like `continue` or `next`. Earlier, such commands did nothing.

Changed in version 3.11: `.pdbrc` is now read using `'utf-8'` encoding. Earlier it was read with the encoding of the system locale.

 h(elp) [command]

With no argument, show the list of commands available. Given a *command* as the argument, show help for that command. `help pdb` brings up the complete documentation (the `pdb` module's docstring). Because the *command* argument has to be an identifier, you enter `help exec` to get help on the `!` command.

 w(here) [count]

Show a stack trace, the newest frame appearing at the bottom. When *count* is 0, show the current frame entry. When *count* is negative, show the oldest - *count* frames. When *count* is positive, show the newest *count* frames. The current frame, which sets the context for most commands, is marked by an arrow (`>`).

Changed in version 3.14: *count* argument is added.

 d(own) [count]

Shift the current frame *count* (one by default) levels down the stack trace (toward a newer frame).

 u(p) [count]

Shift the current frame *count* (one by default) levels up the stack trace (toward an older frame).

 b(reak) [([filename:]lineno | function) [, condition]]

Given a *lineno* argument, place a break at line *lineno* of the current file. You can prefix the line number with a *filename* and a colon to set a breakpoint in a different file (perhaps one not yet loaded). That file is looked up on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). Allowed forms of *filename* are `/abspath/to/file.py`, `relpath/file.py`, `module` and `package.module`.

Given a *function* argument, place a break at the first executable statement inside that function. *function* may be any expression that yields a function within the current namespace.

When a second argument appears, it is an expression that must evaluate to true for the breakpoint to take effect.

With no argument, list every break, and for each breakpoint, the number of hits it has had, its current ignore count, and any condition attached to it.

Every breakpoint gets a number that all the other breakpoint commands use to refer to it.

 tbreak [([filename:]lineno | function) [, condition]]

A temporary breakpoint that gets deleted on its own the first time it is hit. Its arguments match those of `break`.

 cl(ear) [filename:lineno | bpnumber ...]

Given a *filename:lineno* argument, clear every breakpoint on that line. Given a space-separated list of breakpoint numbers, clear those breakpoints. With no argument, clear all breaks (after first asking for confirmation).

 disable bpnumber [bpnumber ...]

[Subject index](INDEX.md) · [Previous](pdb-pdb-class-to-pdb-pdb-set-trace.md) · [Continue](disabling-debugger-breakpoints.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md)

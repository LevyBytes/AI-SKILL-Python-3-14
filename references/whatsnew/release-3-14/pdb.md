# What's new in Python 3.14 / pdb — bdb, pdb, sys

### pdb

- A new [`-p PID`](https://docs.python.org/3.14/library/pdb.html#cmdoption-pdb-p) command-line option now lets the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module attach remotely to an already-running Python process:

```sh
python -m pdb -p 1234

```

Doing so connects to the Python process bearing that PID and lets you debug it interactively. Be aware that, owing to the way the Python interpreter operates, attaching to a remote process that sits blocked inside a system call or waiting on I/O takes effect only once the next bytecode instruction runs or the process is delivered a signal.

The capability builds on PEP 768 along with the new [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec) function to attach to the far process and forward the PDB commands to it.

(Contributed by Matt Wozniski and Pablo Galindo in [gh-131591](https://github.com/python/cpython/issues/131591).)

- Hardcoded breakpoints ([`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) and [`set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace)) now re-use the latest [`Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb) instance that invokes [`set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb.set_trace), rather than building a fresh one on every occasion. Because of that, all instance-specific state such as [`display`](https://docs.python.org/3.14/library/pdb.html#pdbcommand-display) and [`commands`](https://docs.python.org/3.14/library/pdb.html#pdbcommand-commands) carries over between hardcoded breakpoints. (Contributed by Tian Gao in [gh-121450](https://github.com/python/cpython/issues/121450).)

- A fresh *mode* argument is introduced on [`pdb.Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb). The `restart` command becomes unavailable once [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) runs in `inline` mode. (Work by Tian Gao in [gh-123757](https://github.com/python/cpython/issues/123757).)

- When a user attempts to leave [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) while in `inline` mode, a confirmation prompt now appears. Pressing `y`, `Y`, `<Enter>` or `EOF` confirms the exit and triggers [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit), rather than raising [`bdb.BdbQuit`](https://docs.python.org/3.14/library/bdb.html#bdb.BdbQuit). (Contributed by Tian Gao in [gh-124704](https://github.com/python/cpython/issues/124704).)

- Inline breakpoints like [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) or [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) will always halt the program at the calling frame, disregarding the `skip` pattern (when one is set). (Contributed by Tian Gao in [gh-130493](https://github.com/python/cpython/issues/130493).)

- A `<tab>` placed at the start of a line during [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) multi-line input now produces a 4-space indentation rather than emitting a `\t` character. (Contributed by Tian Gao in [gh-130471](https://github.com/python/cpython/issues/130471).)

- Auto-indent is introduced in [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) multi-line input. It will either retain the previous line's indentation or add a 4-space indentation whenever it spots a new code block. (Contributed by Tian Gao in [gh-133350](https://github.com/python/cpython/issues/133350).)

- `$_asynctask` has been added so that, where relevant, the running asyncio task can be reached. (Work by Tian Gao in [gh-124367](https://github.com/python/cpython/issues/124367).)

- [`pdb.set_trace_async()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace_async) has been introduced for debugging asyncio coroutines, and [`await`](https://docs.python.org/3.14/reference/expressions.html#await) statements work within this function. (Work by Tian Gao in [gh-132576](https://github.com/python/cpython/issues/132576).)

- Source code shown within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) is now syntax-highlighted. The same controls used for the default [interactive](https://docs.python.org/3.14/glossary.html#term-interactive) shell govern this behavior, plus the newly added `colorize` argument on [`pdb.Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb). (Contributed by Tian Gao and Łukasz Langa in [gh-133355](https://github.com/python/cpython/issues/133355).)

### pdb

- [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) now offers two backends, resting on either [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) or [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring). Working through the [pdb CLI](https://docs.python.org/3.14/library/pdb.html#pdb-cli) or [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) will always rely on the `sys.monitoring` backend. Directly creating [`pdb.Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb) and the classes derived from it will rely on the `sys.settrace()` backend by default, and that is configurable. (Contributed by Tian Gao in [gh-124533](https://github.com/python/cpython/issues/124533).)

[Subject index](INDEX.md) · [Previous source section](pathlib.md) · [Next source section](pickle.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](textwrap.md)

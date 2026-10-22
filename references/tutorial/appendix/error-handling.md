# 16.1.1. Error Handling

### 16.1.1. Error Handling

Whenever something goes wrong, the interpreter emits a diagnostic message together with a stack trace. Running interactively, it drops you back at the primary prompt afterward; if the input was a file, it quits with a nonzero exit status once the trace has been shown. (An exception caught by an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause inside a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement does not count as an error here.) A handful of conditions are fatal no matter what and end the process with a nonzero exit status, namely internal inconsistencies and certain out-of-memory situations. Every diagnostic goes to the standard error stream, whereas the ordinary output of the commands you ran lands on standard output.

Hitting the interrupt key (typically Control-C or Delete) at either the primary or secondary prompt throws away what you typed and brings back the primary prompt. [1] Should you trigger an interrupt mid-command, the [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception is raised, and a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement can catch it.

[Subject index](INDEX.md) · [Previous source section](interactive-mode.md) · [Following source section](executable-python-scripts.md)

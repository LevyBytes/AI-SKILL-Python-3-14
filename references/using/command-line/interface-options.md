# 1.1.1. Interface options

### 1.1.1. Interface options

While the interpreter's interface looks much like a UNIX shell, it offers several extra ways to be launched:

- If standard input is attached to a tty device, the interpreter shows a prompt, running each command you enter until it encounters an EOF (an end-of-file character; on UNIX you generate it with Ctrl-D, and on Windows with Ctrl-Z followed by Enter). See [Interactive Mode](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac) for additional detail on the interactive session.

- Given a file name as an argument, or a file supplied through standard input, the interpreter loads and runs the script found there.

- Given a directory name as an argument, it locates and runs a suitably named script inside that directory.

- Given `-c command`, the interpreter runs the Python statement(s) passed as *command*. Note that *command* may hold several statements split across newline boundaries. Be aware that leading whitespace carries meaning in Python statements!

- Given `-m module-name`, the named module is resolved through the ordinary import machinery and then run as though it were a script.

When not running interactively, the whole input is parsed up front and only afterward executed.

Encountering an interface option ends the option list that the interpreter itself consumes; every argument that follows is forwarded into [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) — and observe that its initial entry at index zero (`sys.argv[0]`) holds a string identifying where the program came from.

[Subject index](INDEX.md) · [Previous source section](command-line.md) · [Following source section](c-command.md)

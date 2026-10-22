# Interactive defaults without an interface option

With no interface option supplied, `-i` becomes implied, `sys.argv[0]` is set to an empty string (`""`), and the current directory is inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). On top of that, tab-completion and history editing turn on automatically when your platform supports them (see [Readline configuration](https://docs.python.org/3.14/library/site.html#rlcompleter-config)).

See also

[Invoking the Interpreter](https://docs.python.org/3.14/tutorial/interpreter.html#tut-invoking)

Changed in version 3.4: tab-completion plus history editing now switch on by themselves.

[Subject index](INDEX.md) · [Previous source section](run-a-python-file-directory-or-zip-archive.md) · [Following source section](h-help.md)

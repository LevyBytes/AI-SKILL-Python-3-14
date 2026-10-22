# cmd: `Cmd.doc_header`, `Cmd.misc_header`, `Cmd.undoc_header`, `Cmd.ruler`, `Cmd.use_rawinput`

Cmd.doc_header

The header put out when the help output contains a section for documented commands.

 Cmd.misc_header

The header put out when the help output contains a section for miscellaneous help topics (namely, `help_*()` methods that lack matching `do_*()` methods).

 Cmd.undoc_header

The header put out when the help output contains a section for undocumented commands (namely, `do_*()` methods that lack matching `help_*()` methods).

 Cmd.ruler

The character drawn to form the separator lines beneath the help-message headers. When empty, no ruler line appears. Its default is `'='`.

 Cmd.use_rawinput

A flag whose default is true. When true, `cmdloop()` calls [`input()`](https://docs.python.org/3.14/library/functions.html#input) to show a prompt and read the next command; when false, [`sys.stdout.write()`](https://docs.python.org/3.14/library/sys.html#sys.stdout) and [`sys.stdin.readline()`](https://docs.python.org/3.14/library/sys.html#sys.stdin) handle that work. (As a result, importing [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) on systems that support it lets the interpreter automatically support **Emacs**-like line editing and command-history keystrokes.)

[Subject index](INDEX.md) · [Previous](cmd-cmdloop-to-cmd-intro.md) · [Continue](cmd-example-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: cmd](cmd-cmd-class.md) · [Owning module, declaration or section: Cmd Objects](cmd-cmdloop-to-cmd-intro.md)

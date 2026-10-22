# What's New In Python 3.13 / A better interactive interpreter

### New Features

### A better interactive interpreter

By default Python now runs a new [interactive](https://docs.python.org/3.14/glossary.html#term-interactive) shell, derived from code in the [PyPy project](https://pypy.org/). Whenever someone launches the [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) from an interactive terminal, these new capabilities are available:

- Multiline editing with history preservation.

- REPL-specific commands such as help, exit, and quit are usable straight away, with no requirement to invoke them as function calls.

- Prompts and tracebacks with [color enabled by default](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

- Interactive help browsing using F1 with a separate command history.

- Browsing past entries with F2, which jumps over output along with the [>>>](https://docs.python.org/3.14/glossary.html#term-0) and [?](https://docs.python.org/3.14/glossary.html#term-...) prompts.

- A ?Paste mode? bound to F3 eases pasting of bigger code chunks (hit F3 once more to come back to the ordinary prompt).

If you want to turn the new interactive shell off, set the [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable. Further detail about interactive mode lives in [Interactive Mode](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac).

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](improved-error-messages.md) · [Release/subject declaration](summary-release-highlights.md)

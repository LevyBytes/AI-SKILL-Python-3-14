# sys.__interactivehook__

sys.__interactivehook__

Whenever this attribute is present, its value is invoked automatically (with no arguments) as the interpreter starts up in [interactive mode](https://docs.python.org/3.14/tutorial/interpreter.html#tut-interactive). This happens once the [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) file has been read, so the hook can be set up in there. The [`site`](https://docs.python.org/3.14/library/site.html#module-site) module [sets this](https://docs.python.org/3.14/library/site.html#rlcompleter-config).

When the hook fires at startup, an auditing event `cpython.run_interactivehook` is raised, passing the hook object as its argument.

Added in version 3.4.

[API family](INDEX.md) · [sys context index](../INDEX.md).

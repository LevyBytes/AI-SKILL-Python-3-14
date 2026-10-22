# site — Readline configuration

### Readline configuration

Where [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) is available, this module additionally imports and sets up the [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) module, provided Python launches in [interactive mode](https://docs.python.org/3.14/tutorial/interpreter.html#tut-interactive) and without the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) option. By default this switches on tab completion and adopts `~/.python_history` for saving history. You can switch it off by removing (or replacing) the [`sys.__interactivehook__`](https://docs.python.org/3.14/library/sys.html#sys.__interactivehook__) attribute from your `sitecustomize` or `usercustomize` module, or from your [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) file.

Changed in version 3.4: Turning on rlcompleter and history became automatic.

[Subject index](INDEX.md) · [Previous](usercustomize.md) · [Continue](site-prefixes-to-site-getusersitepackages.md) · [Owning module, declaration or section: site](site-site-specific-configuration-hook.md)

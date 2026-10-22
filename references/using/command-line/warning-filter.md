# -W arg

-W arg

Warning control. By default, Python's warning machinery sends warning messages to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

In their simplest form, the settings apply one specific action across the board to every warning a process raises (including ones that would otherwise be ignored by default):

```sh
-Wdefault  # Warn once per call location
-Werror    # Convert to exceptions
-Walways   # Warn every time
-Wall      # Same as -Walways
-Wmodule   # Warn once per calling module
-Wonce     # Warn once per Python process
-Wignore   # Never warn

```

You can shorten the action names however you like, and the interpreter will expand them into the matching action name. As an illustration, `-Wi` means the same thing as `-Wignore`.

Here is the argument's complete form:

```sh
action:message:category:module:lineno

```

Fields left empty match every value, and trailing empty fields can be left off. For instance, `-W ignore::DeprecationWarning` ignores all DeprecationWarning warnings.

The *action* field works as described above, yet it only governs warnings matching the remaining fields.

The *message* field has to match the entire warning message, and this comparison ignores case.

The *category* field corresponds to the warning category (for example, `DeprecationWarning`). It has to be a class name; the test checks whether the message's actual warning category is a subclass of the category you specified.

The *module* field matches the module name in full (fully qualified), and this comparison is case-sensitive.

The *lineno* field matches the line number; here zero matches every line number and so amounts to leaving the line number out.

You can supply several `-W` options; should a warning match more than one, the action belonging to the last matching option takes effect. Any invalid `-W` options are ignored (although a warning about invalid options is printed once the first warning fires).

Warnings may likewise be steered through the `PYTHONWARNINGS` environment variable and from inside a Python program by way of the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module. As an example, the [`warnings.filterwarnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.filterwarnings) function lets you apply a regular expression to the warning message.

Consult [The Warnings Filter](https://docs.python.org/3.14/library/warnings.html#warning-filter) and [Describing Warning Filters](https://docs.python.org/3.14/library/warnings.html#describing-warning-filters) for further specifics.

[Subject index](INDEX.md) · [Previous source section](verbose-imports.md) · [Following source section](skip-script-first-line.md)

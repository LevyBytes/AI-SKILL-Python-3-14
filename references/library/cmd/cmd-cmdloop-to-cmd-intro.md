# cmd: Command-interpreter loop, hooks and help configuration

### Cmd Objects

A `Cmd` instance offers the methods below:

 Cmd.cmdloop(*intro=None*)

Repeatedly present a prompt, take input, strip an opening prefix from what was received, and route it to action methods, handing them the rest of the line as the argument.

The optional argument supplies a banner or intro string to print ahead of the first prompt (this takes precedence over the `intro` class attribute).

When the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module is loaded, input picks up **bash**-style history-list editing on its own (for instance, Control-P scrolls back to the previous command, Control-N moves forward to the next, Control-F shifts the cursor rightward without erasing, Control-B shifts it leftward without erasing, and so forth).

End-of-file on input comes back as the string `'EOF'`.

An interpreter instance recognizes a command named `foo` exactly when it owns a method `do_foo()`. In a special case, a line that opens with the character `'?'` routes to the method `do_help()`. In another special case, a line that opens with the character `'!'` routes to the method `do_shell()` (provided such a method exists).

This method returns once the `postcmd()` method yields a true value. The *stop* argument handed to `postcmd()` is the value returned from the matching `do_*()` method for that command.

With completion turned on, completing commands proceeds automatically, and completing a command's args happens by invoking `complete_foo()` with the arguments *text*, *line*, *begidx*, and *endidx*. *text* is the prefix string we are trying to match — every returned match has to start with it. *line* holds the current input line with leading whitespace stripped, while *begidx* and *endidx* mark the start and end indexes of the prefix text, which you can use to vary completion based on the argument's position.

 Cmd.do_help(*arg*)

Every subclass of `Cmd` inherits a built-in `do_help()`. Called with an argument `'bar'`, this method calls the matching method `help_bar()`, and when that one is absent, prints the docstring of `do_bar()` if one exists. Given no argument, `do_help()` enumerates all available help topics (namely every command paired with a `help_*()` method, plus commands carrying docstrings) and likewise enumerates any undocumented commands.

 Cmd.onecmd(*str*)

Treat the argument as if it had been typed in reply to the prompt. You may override this, though there is usually no need; consult the `precmd()` and `postcmd()` methods for handy execution hooks. The return value flags whether the interpreter ought to halt its interpretation of commands. When a `do_*()` method exists for the command *str*, that method's return value is returned; otherwise the value returned by the `default()` method is returned.

 Cmd.emptyline()

The method invoked when a blank line is entered in reply to the prompt. Unless overridden, this method re-runs the last nonempty command that was entered.

 Cmd.default(*line*)

The method invoked on an input line whose command prefix goes unrecognized. Unless overridden, this method prints an error message and returns.

 Cmd.completedefault(*text*, *line*, *begidx*, *endidx*)

The method invoked to complete an input line whenever no command-specific `complete_*()` method exists. By default it returns an empty list.

 Cmd.columnize(*list*, *displaywidth=80*)

The method invoked to render a list of strings as a tidy block of columns. No column is wider than it has to be. A gap of two spaces separates columns for legibility.

 Cmd.precmd(*line*)

A hook method run right before the command line *line* is interpreted, yet after the input prompt has been built and shown. In `Cmd` this method is a stub, present so subclasses can override it. Its return value becomes the command the `onecmd()` method will run; a `precmd()` implementation may rewrite the command or hand back *line* untouched.

 Cmd.postcmd(*stop*, *line*)

A hook method run right after a command dispatch wraps up. In `Cmd` this method is a stub, present so subclasses can override it. *line* is the command line that was run, and *stop* flags whether execution will end once `postcmd()` returns; this will be the return value of the `onecmd()` method. Whatever this method returns becomes the new value for the internal flag tied to *stop*; returning false keeps interpretation going.

 Cmd.preloop()

A hook method run once when `cmdloop()` is invoked. In `Cmd` this method is a stub, present so subclasses can override it.

 Cmd.postloop()

A hook method run once as `cmdloop()` is about to return. In `Cmd` this method is a stub, present so subclasses can override it.

Instances of `Cmd` subclasses expose a few public instance variables:

 Cmd.prompt

The prompt put out to ask for input.

 Cmd.identchars

The string of characters allowed within the command prefix.

 Cmd.lastcmd

The most recent nonempty command prefix observed.

 Cmd.cmdqueue

A list of queued input lines. `cmdloop()` consults the cmdqueue list whenever fresh input is required; when it holds entries, those are handled in order, just as though typed at the prompt.

 Cmd.intro

A string to put out as an intro or banner. It can be overridden by passing the `cmdloop()` method an argument.

[Subject index](INDEX.md) · [Previous](cmd-cmd-class.md) · [Continue](cmd-doc-header-to-cmd-use-rawinput.md) · [Owning module, declaration or section: cmd](cmd-cmd-class.md)

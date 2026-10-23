# cmd - Cmd Example - Section introduction and initial examples

### Cmd Example

The `cmd` module proves most useful for assembling custom shells that let a user drive a program interactively.

What follows is a brief example of constructing a shell around a handful of the commands in the [`turtle`](https://docs.python.org/3.14/library/turtle.html#module-turtle) module.

Elementary turtle commands such as [`forward()`](https://docs.python.org/3.14/library/turtle.html#turtle.forward) get added to a `Cmd` subclass via a method called `do_forward()`. The argument is turned into a number and routed to the turtle module. The shell's built-in help utility draws on the docstring.

The example further provides a simple record-and-playback feature built on the `precmd()` method, which handles lowercasing the input and writing the commands out to a file. The `do_playback()` method reads that file back and pushes the saved commands onto the `cmdqueue` for instant playback:

[Subject index](INDEX.md) · [Previous](cmd-doc-header-to-cmd-use-rawinput.md) · [Continue](cmd-example-code-example-import-cmd-sys.md) · [Owning module, declaration or section: cmd](cmd-cmd-class.md)

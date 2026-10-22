# 9.1. Complete Python programs

### 9.1. Complete Python programs

A language spec doesn't have to dictate the way its interpreter gets launched, yet it still helps to define what a complete Python program is. Such a program runs inside an environment that has barely been set up: every built-in and standard module is present, though none has been initialized, with the exception of [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) (assorted system services), [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) (the built-in functions, exceptions, and `None`), and [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__). That last one supplies both the local and the global namespace in which the whole program runs.

A complete Python program follows the same syntax as file input, which the upcoming section covers.

You can likewise start the interpreter in interactive mode; here it doesn't ingest and run a whole program but instead takes and runs a single statement (which may be compound) at a time. The starting environment matches that of a complete program, and every statement runs within the namespace of [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__).

There are three ways to deliver a complete program to the interpreter: through the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) *string* command line option, as the file named in the first command line argument, or by way of standard input. Should that file or standard input turn out to be a tty device, the interpreter switches into interactive mode; if not, it runs the file as a complete program.

[Subject index](INDEX.md) · [Owning language section](top-level-components.md) · [Previous source section](top-level-components.md) · [Following source section](file-input.md)

# 2.1. Invoking the Interpreter

## 2. Using the Python Interpreter

### 2. Using the Python Interpreter

### 2.1. Invoking the Interpreter

On machines that carry it, the Python interpreter typically lands at `/usr/local/bin/python3.14`; once `/usr/local/bin` is on your Unix shell's search path, you can launch it just by entering the command:

```text
python3.14

```

into the shell. [1] Because which directory holds the interpreter is decided at install time, it may sit elsewhere; ask your local Python expert or your system administrator. (For instance, `/usr/local/python` is a widely used alternative spot.)

When you've installed Python on Windows from the [Microsoft Store](https://docs.python.org/3.14/using/windows.html#windows-store), the `python3.14` command becomes available. Should the [py.exe launcher](https://docs.python.org/3.14/using/windows.html#launcher) be installed, the `py` command works too. Consult [Python install manager](https://docs.python.org/3.14/using/windows.html#setting-envvars) for further ways to start Python.

Entering an end-of-file character at the primary prompt (Control-D on Unix, Control-Z on Windows) makes the interpreter quit with a zero exit status. Where that fails, you can leave the interpreter by entering this command instead: `quit()`.

On the majority of systems the interpreter's line-editing capabilities cover interactive editing, history substitution, and code completion. The fastest way to tell whether command line editing is present is probably to type a word at the Python prompt and then hit the Left arrow (or Control-b). A cursor that moves means you have command line editing; turn to Appendix [Interactive Input Editing and History Substitution](https://docs.python.org/3.14/tutorial/interactive.html#tut-interacting) for a primer on the keys. Should nothing seem to occur, or should a sequence such as `^[[D` or `^B` show up, command line editing is absent; backspace will be your only means of deleting characters from the line you're on.

In broad terms the interpreter behaves much like the Unix shell: invoke it with standard input wired to a tty device and it reads and runs commands interactively; invoke it with a file name argument or with a file as standard input and it reads and runs a *script* drawn from that file.

Another route into the interpreter is `python -c command [arg] ...`, which runs the statement(s) held in *command*, paralleling the shell's [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) option. Because Python statements regularly include spaces or other characters the shell treats specially, the usual advice is to wrap *command* in quotes from end to end.

A number of Python modules double as handy scripts. You can call them with `python -m module [arg] ...`, which runs the source file belonging to *module* exactly as though you had written out its full name on the command line.

With a script file in play, there are times when you'd like to run the script and then drop into interactive mode. Passing [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) ahead of the script achieves that.

Every command line option is documented in [Command line and environment](https://docs.python.org/3.14/using/cmdline.html#using-on-general).

[Subject index](INDEX.md) · [Previous source section](../interactive-input-editing-and-history-substitution/alternatives-to-the-interactive-interpreter.md) · [Following source section](argument-passing.md)

# 2.1.1. Argument Passing

### 2.1.1. Argument Passing

Once the interpreter has them, the script name together with any arguments that follow become a list of strings stored in the `argv` variable inside the `sys` module. Run `import sys` to reach this list. Its length is never below one; with neither a script nor any arguments supplied, `sys.argv[0]` holds an empty string. Give the script name as `'-'` (which stands for standard input) and `sys.argv[0]` becomes `'-'`. Use [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) *command* and `sys.argv[0]` becomes `'-c'`. Use [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) *module* and `sys.argv[0]` becomes the full name of the module that was found. Any options sitting after `-c` *command* or `-m` *module* bypass the Python interpreter's own option handling and stay in `sys.argv` for the command or module to deal with.

[Subject index](INDEX.md) · [Previous source section](invoking-the-interpreter.md) · [Following source section](interactive-mode.md)

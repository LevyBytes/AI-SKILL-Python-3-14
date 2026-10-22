# 4.1. Structure of a program

### 4. Execution model

### 4.1. Structure of a program

Code blocks are the building units out of which a Python program is assembled. The term *block* names a stretch of Python program text that runs as a single unit. These count as blocks: a module, the body of a function, and a class definition. Every command you enter interactively counts as a block too. A script file — that is, a file handed to the interpreter on standard input or named as an argument on its command line — counts as a code block. A script command (one supplied on the interpreter command line via the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) option) is itself a code block. So is a module launched as a top level script (under the name `__main__`) from the command line through a [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) argument. The string handed to the built-in functions [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) and [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) likewise forms a code block.

Every code block runs inside an *execution frame*. A frame holds certain administrative data (handy for debugging) and dictates the location and manner in which execution proceeds once the code block has finished running.

[Subject index](INDEX.md) · [Following source section](binding-of-names.md)

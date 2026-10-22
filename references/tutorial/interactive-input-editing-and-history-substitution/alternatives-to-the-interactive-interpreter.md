# 14.2. Alternatives to the Interactive Interpreter

### 14.2. Alternatives to the Interactive Interpreter

Set against the interpreter's older releases, this capability marks a huge leap ahead; even so, a few wishes remain unmet. One would be having the right indentation offered on continuation lines (the parser already knows whether an [`INDENT`](https://docs.python.org/3.14/library/token.html#token.INDENT) token comes next). The completion machinery could draw on the interpreter's symbol table. And a command that verified — or even proposed — matching parentheses, quotes, and the like would help too.

A long-standing alternative among enhanced interactive interpreters is [IPython](https://ipython.org/), bringing tab completion, object exploration, and sophisticated history management. It lends itself to deep customization and to being embedded inside other applications as well. A comparable enhanced interactive environment is [bpython](https://bpython-interpreter.org/).

[Subject index](INDEX.md) · [Previous source section](tab-completion-and-history-editing.md) · [Following source section](../using-the-python-interpreter/invoking-the-interpreter.md)

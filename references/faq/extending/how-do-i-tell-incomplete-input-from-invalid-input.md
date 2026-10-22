# How do I tell “incomplete input” from “invalid input”?

### How do I tell “incomplete input” from “invalid input”?

There are times you'd like to mimic how the Python interactive interpreter acts — it shows a continuation prompt whenever the input is unfinished (you've typed the opening of an “if” statement, say, or left parentheses or triple string quotes unclosed), yet it surfaces a syntax error right away the moment the input is invalid.

From Python, the [`codeop`](https://docs.python.org/3.14/library/codeop.html#module-codeop) module fits the bill, coming close enough to how the parser behaves. IDLE relies on it, as one instance.

Over in C, the path of least resistance is to invoke [`PyRun_InteractiveLoop()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_InteractiveLoop) — perhaps on its own thread — and leave the input to the Python interpreter. Another option is pointing [`PyOS_ReadlineFunctionPointer()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) at an input function of your own. Look to `Modules/readline.c` and `Parser/myreadline.c` for additional pointers.

[Subject index](INDEX.md)

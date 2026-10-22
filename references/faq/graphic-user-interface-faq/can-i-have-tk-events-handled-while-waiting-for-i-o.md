# Can I have Tk events handled while waiting for I/O?

### Can I have Tk events handled while waiting for I/O?

Off Windows, yes — and threads aren't even needed! You will, though, have to reshape your I/O code somewhat. Tk provides the counterpart of Xt's `XtAddInput()` call, letting you register a callback function that the Tk mainloop invokes whenever I/O becomes possible on a file descriptor. Refer to [File Handlers](https://docs.python.org/3.14/library/tkinter.html#tkinter-file-handlers).

[Subject index](INDEX.md)

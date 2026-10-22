# subinterpreters C API: Subinterpreters and main-interpreter relationships

# Subinterpreters

### Multiple interpreters in a Python process

Most of the time you embed just one Python interpreter, yet situations arise that call for spinning up multiple self-contained interpreters within a single process — possibly within a single thread as well. Sub-interpreters make that achievable.

What is termed the “main” interpreter is whichever one the runtime brings up first during initialization. Typically it stands as the lone Python interpreter inside a process. Setting it apart from sub-interpreters, the main interpreter shoulders process-wide duties of its own such as handling signals. On top of that it drives execution while the runtime starts up and is normally the interpreter still active as the runtime shuts down. A pointer to its state comes back from the `PyInterpreterState_Main()` function.

Moving from one sub-interpreter to another is done through the [`PyThreadState_Swap()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Swap) function. To bring them into being and tear them down, rely on the functions listed below:

[Subject index](INDEX.md) · [Following source contract](pyinterpreterconfig-to-pyinterpreterconfig-own-gil.md)

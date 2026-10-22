# the very high level layer C API: Python file execution and interactive-loop entrypoints

## The Very High Level Layer??

### The Very High Level Layer

With the functions in this chapter you can run Python source code supplied through a file or a buffer, though they offer no finer-grained way to communicate with the interpreter.

A number of these functions take a grammar start symbol as one of their parameters. The start symbols you can choose from are `Py_eval_input`, `Py_file_input`, `Py_single_input`, and `Py_func_type_input`. They are documented after the functions that receive them as parameters.

Be aware as well that some of these functions expect FILE* parameters. A subtlety worth handling with care is that the `FILE` structure may differ and be incompatible between C libraries. On Windows at the very least, dynamically linked extensions can wind up using separate libraries, so make sure FILE* parameters reach these functions only when you know they came from the very same library the Python runtime relies on.

 int PyRun_AnyFile(FILE *fp, const char *filename)

A pared-down wrapper over `PyRun_AnyFileExFlags()` further down, with *closeit* fixed at `0` and *flags* fixed at `NULL`.

 int PyRun_AnyFileFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

A pared-down wrapper over `PyRun_AnyFileExFlags()` further down, with the *closeit* argument pinned to `0`.

 int PyRun_AnyFileEx(FILE *fp, const char *filename, int closeit)

A pared-down wrapper over `PyRun_AnyFileExFlags()` further down, with the *flags* argument pinned to `NULL`.

 int PyRun_AnyFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

When *fp* points at a file tied to an interactive device (a console, terminal input, or Unix pseudo-terminal), the call returns whatever `PyRun_InteractiveLoop()` yields; otherwise it hands back the outcome of `PyRun_SimpleFile()`. *filename* is decoded from the filesystem encoding ([`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding)). Should *filename* be `NULL`, the function falls back on `"???"` for the filename. When *closeit* is true, the file gets closed prior to `PyRun_SimpleFileExFlags()` returning.

 int PyRun_SimpleString(const char *command)

A pared-down wrapper over `PyRun_SimpleStringFlags()` further down, with the `PyCompilerFlags`* argument pinned to `NULL`.

 int PyRun_SimpleStringFlags(const char *command, PyCompilerFlags *flags)

Runs the Python source code held in *command* inside the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module, honoring the *flags* argument. When `__main__` is not yet present, it gets created. The return is `0` for success or `-1` when an exception was raised. Should an error occur, no mechanism exists to retrieve the exception details. The meaning of *flags* is covered below.

Keep in mind that when an otherwise unhandled [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) is raised, the function does not give back `-1`; instead it exits the process, provided [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) is zero.

 int PyRun_SimpleFile(FILE *fp, const char *filename)

A streamlined front end for `PyRun_SimpleFileExFlags()` shown later, where *closeit* defaults to `0` while *flags* defaults to `NULL`.

 int PyRun_SimpleFileEx(FILE *fp, const char *filename, int closeit)

A streamlined front end for `PyRun_SimpleFileExFlags()` shown later, where *flags* defaults to `NULL`.

 int PyRun_SimpleFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

Behaves like `PyRun_SimpleStringFlags()`, except the Python source code arrives from *fp* rather than from a string held in memory. *filename* ought to be the file's name, and it is decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). When *closeit* is true, the file gets closed prior to `PyRun_SimpleFileExFlags()` returning.

Note

On Windows, open *fp* in binary mode (e.g. `fopen(filename, "rb")`). Failing that, Python might mishandle a script file using LF line endings.

 int PyRun_InteractiveOneObject(FILE *fp, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, PyCompilerFlags *flags)

Reads one statement from a file tied to an interactive device and runs it, following the *flags* argument. The prompt shown to the user comes from `sys.ps1` and `sys.ps2`. *filename* has to be a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object.

The return is `0` when the input ran successfully, `-1` when an exception occurred, or an error code drawn from the `errcode.h` include file shipped with Python when a parse error happened. (Bear in mind that `errcode.h` is not pulled in by `Python.h`, so you must include it explicitly when you need it.)

 int PyRun_InteractiveOne(FILE *fp, const char *filename)

A thin shortcut to `PyRun_InteractiveOneFlags()` documented below, in which *flags* takes the value `NULL`.

 int PyRun_InteractiveOneFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

Behaves like `PyRun_InteractiveOneObject()`, except *filename* is a const char*, decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

 int PyRun_InteractiveLoop(FILE *fp, const char *filename)

A convenience entry point onto `PyRun_InteractiveLoopFlags()` covered below, holding *flags* at `NULL`.

 int PyRun_InteractiveLoopFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

Reads and runs statements from a file tied to an interactive device, continuing until EOF arrives. The prompt presented to the user uses `sys.ps1` and `sys.ps2`. *filename* is decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). The return is `0` at EOF, or a negative number on failure.

 int (*PyOS_InputHook)(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

May be pointed at a function whose prototype is `int func(void)`. Python invokes that function as the interpreter prompt is about to go idle and wait for terminal input from the user. Its return value gets discarded. Replacing this hook is a way to weave the interpreter's prompt together with other event loops, as `Modules/_tkinter.c` does within the Python source code.

Changed in version 3.12: Invocation of this function is now restricted to the [main interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support).

[Subject index](INDEX.md) · [Previous source contract](../utilities/utilities.md) · [Following source contract](pyrun-string-to-pyeval-evalcode.md)

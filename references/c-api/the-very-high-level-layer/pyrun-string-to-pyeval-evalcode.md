# the very high level layer C API: Interactive input hooks and code compilation/execution

char *(*PyOS_ReadlineFunctionPointer)(FILE*, FILE*, const char*)

May be pointed at a function whose prototype is `char *func(FILE *stdin, FILE *stdout, char *prompt)`, which supplants the default routine that reads one line of input at the interpreter's prompt. That function should emit the string *prompt* when it is not `NULL`, then read one line of input from the supplied standard input file and return the resulting string. As an example, the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module installs this hook to deliver line-editing and tab-completion capabilities.

The outcome has to be a string allocated through [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc) or [`PyMem_RawRealloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawRealloc), or `NULL` should an error arise.

Changed in version 3.4: The result now has to come from [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc) or [`PyMem_RawRealloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawRealloc), rather than from [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) or [`PyMem_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Realloc).

Changed in version 3.12: Only the [main interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support) ever triggers a call to this function.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_String(const char *str, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals)

*Return value: New reference.*

A reduced form of `PyRun_StringFlags()` given below, where the *flags* parameter stays `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_StringFlags(const char *str, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, PyCompilerFlags *flags)

*Return value: New reference.*

Runs the Python source code from *str* within the context defined by the objects *globals* and *locals*, using the compiler flags given by *flags*. *globals* has to be a dictionary; *locals* may be any object that supports the mapping protocol. The parameter *start* picks the start symbol and has to be one of the available start symbols.

Hands back the object that results from running the code as a Python object, or `NULL` if an exception was raised.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_File(FILE *fp, const char *filename, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals)

*Return value: New reference.*

A condensed gateway to `PyRun_FileExFlags()` appearing below, holding *closeit* at `0` together with *flags* at `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_FileEx(FILE *fp, const char *filename, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, int closeit)

*Return value: New reference.*

A condensed gateway to `PyRun_FileExFlags()` appearing below, holding *flags* at `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_FileFlags(FILE *fp, const char *filename, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, PyCompilerFlags *flags)

*Return value: New reference.*

A condensed gateway to `PyRun_FileExFlags()` appearing below, holding *closeit* at `0`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyRun_FileExFlags(FILE *fp, const char *filename, int start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals, int closeit, PyCompilerFlags *flags)

*Return value: New reference.*

Behaves like `PyRun_StringFlags()`, except the Python source code is read from *fp* rather than from a string in memory. *filename* ought to be the file's name, and it is decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). When *closeit* is true, the file gets closed prior to `PyRun_FileExFlags()` returning.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_CompileString(const char *str, const char *filename, int start)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A trimmed handle on `Py_CompileStringFlags()` listed below, with *flags* kept as `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_CompileStringFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags)

*Return value: New reference.*

A trimmed handle on `Py_CompileStringExFlags()` listed below, with *optimize* assigned `-1`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_CompileStringObject(const char *str, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, int start, PyCompilerFlags *flags, int optimize)

*Return value: New reference.*

Parses and compiles the Python source code held in *str*, giving back the code object that results. The start symbol comes from *start*; this lets you restrict which code may be compiled and should be one of the available start symbols. The filename supplied in *filename* goes into building the code object and can show up in tracebacks or [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exception messages. The return is `NULL` when the code cannot be parsed or compiled.

The integer *optimize* sets the compiler's optimization level; a value of `-1` adopts the interpreter's optimization level as set by the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) options. Stated outright, the levels run `0` (where nothing is optimized and `__debug__` stays true), `1` (which strips out asserts and turns `__debug__` false), and `2` (which additionally drops docstrings).

Added in version 3.4.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_CompileStringExFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags, int optimize)

*Return value: New reference.*

Behaves like `Py_CompileStringObject()`, except *filename* is a byte string decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

Added in version 3.2.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_EvalCode([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a simplified interface to `PyEval_EvalCodeEx()`, supplying only the code object together with the global and local variables. Every other argument is set to `NULL`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyrun-anyfile-to-pyrun-interactiveloopflags.md) · [Following source contract](pyeval-evalcodeex-to-pyeval-mergecompilerflags.md)

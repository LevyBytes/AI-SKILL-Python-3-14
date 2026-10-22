# File objects

## File objects

### File objects

This set of APIs offers a bare-bones imitation of the Python 2 C API for built-in file objects, which once depended on the buffered I/O (FILE*) facilities of the C standard library. Under Python 3, files and streams go through the new [`io`](https://docs.python.org/3.14/library/io.html#module-io) module, which layers several abstractions over the operating system's low-level unbuffered I/O. The functions listed below act as convenience C wrappers around those newer APIs and exist chiefly for the interpreter's own internal error reporting; third-party code should reach for the `io` APIs directly.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFile_FromFd(int fd, const char *name, const char *mode, int buffering, const char *encoding, const char *errors, const char *newline, int closefd)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a Python file object out of the file descriptor of an already-opened file *fd*. You may pass `NULL` for the arguments *name*, *encoding*, *errors* and *newline* to fall back on the defaults; passing *-1* for *buffering* selects the default there. The *name* value is disregarded and retained only for backward compatibility. On failure the call returns `NULL`. For a fuller account of the arguments, consult the documentation for the [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) function.

Warning

Because Python streams maintain a buffering layer of their own, combining them with OS-level file descriptors can give rise to assorted problems — data turning up in an unexpected order, for one.

Changed in version 3.2: Ignore *name* attribute.

 int PyObject_AsFileDescriptor([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields, as an int, the file descriptor tied to *p*. When the object happens to be an integer, that value is what comes back. Otherwise, the object's [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method gets invoked if it is present; that method has to give back an integer, which then serves as the file descriptor value. On failure it raises an exception and returns `-1`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFile_GetLine([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, int n)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Acting as the counterpart of `p.readline([n])`, this function pulls a single line from the object *p*. That *p* can be a file object or any object furnishing a [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) method. Passing `0` for *n* reads precisely one line, no matter how long the line happens to be. A value of *n* above `0` caps the read at *n* bytes from the file, so the returned line may be only partial. Either way, hitting end-of-file straightaway yields an empty string. When *n* is below `0`, a full line is read regardless of its length, but reaching end-of-file at once triggers an [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError).

 int PyFile_SetOpenCodeHook(Py_OpenCodeHookFunction handler)

Supplants the usual behavior of [`io.open_code()`](https://docs.python.org/3.14/library/io.html#io.open_code) so that its argument flows through the handler you supply.

Here *handler* is a function whose type is:

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*Py_OpenCodeHookFunction)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, void*)

The counterpart of [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*)(PyObject *path, void *userData), in which *path* is assured to be a [`PyUnicodeObject`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeObject).

The *userData* pointer gets handed to the hook function. Given that hook functions can be invoked out of separate runtimes, this pointer ought not to point straight at Python state.

Because this hook is by design exercised while importing, steer clear of importing fresh modules during its run unless you know them to be frozen or already present in `sys.modules`.

After a hook is in place, it can be neither removed nor swapped out, and any subsequent calls to `PyFile_SetOpenCodeHook()` will not succeed. When it fails, the function returns -1 and, provided the interpreter has already been initialized, raises an exception.

It is safe to invoke this function ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) named `setopencodehook` carrying no arguments.

Added in version 3.8.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFile_OpenCodeObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path)

Opens *path* using the mode `'rb'`. The *path* argument has to be a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object. You can override how this function behaves through `PyFile_SetOpenCodeHook()` so as to run some preprocessing over the text.

This parallels [`io.open_code()`](https://docs.python.org/3.14/library/io.html#io.open_code) on the Python side.

When it succeeds, the function gives back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to a Python file object. When it fails, it gives back `NULL` and leaves an exception set.

Added in version 3.8.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFile_OpenCode(const char *path)

Similar to `PyFile_OpenCodeObject()`, but *path* is a UTF-8 encoded const char*.

Added in version 3.8.

 int PyFile_WriteObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Writes the object *obj* out to the file object *p*. For *flags*, the sole accepted value is [`Py_PRINT_RAW`](https://docs.python.org/3.14/c-api/object.html#c.Py_PRINT_RAW); when supplied, the object's [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) form is what gets written rather than its [`repr()`](https://docs.python.org/3.14/library/functions.html#repr).

Should *obj* be `NULL`, the string `"<NULL>"` is written.

Gives back `0` when it succeeds or `-1` when it fails, with the relevant exception being set.

 int PyFile_WriteString(const char *s, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Writes the string *s* out to the file object *p*. Gives back `0` on success or `-1` on failure, with the relevant exception being set.

[Subject index](INDEX.md) · [Previous source contract](../defining-extension-modules/legacy-single-phase-initialization.md) · [Following source contract](pyfile-newstdprinter-to-pystdprinter-type.md)

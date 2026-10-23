# What’s New in Python 2.2 / Interpreter Changes and Fixes - sys

### Interpreter Changes and Fixes

A portion of these changes matter solely to those working with the Python interpreter down at the C level — authors of Python extension modules, people embedding the interpreter, or anyone tinkering with the interpreter's own internals. Stick to writing Python code and almost nothing covered here will touch you.

- You can now write profiling and tracing functions in C, where they run far faster than their Python counterparts and ought to trim the cost of profiling and tracing. Authors of Python development environments will find this useful. Python's API gained two new C functions, [`PyEval_SetProfile()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfile) and [`PyEval_SetTrace()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTrace). The [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) and [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) functions remain in place; they have merely been reworked to sit on top of the new C-level interface. (Contributed by Fred L. Drake, Jr.)

- A further low-level API arrived, aimed mostly at those building Python debuggers and development tooling. With [`PyInterpreterState_Head()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Head) and [`PyInterpreterState_Next()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Next) a caller can step across every interpreter object that exists; [`PyInterpreterState_ThreadHead()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_ThreadHead) together with [`PyThreadState_Next()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyThreadState_Next) make it possible to iterate over all the thread states under a given interpreter. (Contributed by David Beazley.)

- The garbage collector's C-level interface has been reworked so that writing extension types which cooperate with garbage collection, and debugging mistaken uses of these functions, both become easier. Because several functions now carry slightly altered semantics, a number of them had to be renamed. An extension built against the old API will still compile, yet it will *not* take part in garbage collection, so bringing it up to date for 2.2 deserves reasonably high priority.

Follow these steps to move an extension module onto the new API:

- Change the name `Py_TPFLAGS_GC` over to [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC).

- Allocate objects with [`PyObject_GC_New()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) or [`PyObject_GC_NewVar()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar),

and free them with [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del).

- Change `PyObject_GC_Init()` to [`PyObject_GC_Track()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Track), and `PyObject_GC_Fini()` to [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack).

- Remove `PyGC_HEAD_SIZE` from object size calculations.

- Remove calls to `PyObject_AS_GC()` and `PyObject_FROM_GC()`.

- [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) gained a new `et` format sequence; `et` accepts both a parameter and an encoding name, then converts the parameter into that encoding when the parameter proves to be a Unicode string, or leaves it untouched if it's an 8-bit string, presuming it already sits in the wanted encoding. That sets it apart from the `es` format character, which treats 8-bit strings as being in Python's default ASCII encoding and converts them into the named new encoding. (Contributed by M.-A. Lemburg; it underpins the Windows MBCS support covered in the section just below.)

- Another argument-parsing function, [`PyArg_UnpackTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_UnpackTuple), has joined the API — simpler, and likely quicker. Rather than handing over a format string, the caller merely states the smallest and largest argument counts it expects, along with a collection of pointers to [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* variables that get populated with the argument values.

- Method definition tables can now use two new flags, [`METH_NOARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_NOARGS) and [`METH_O`](https://docs.python.org/3.14/c-api/structures.html#c.METH_O), which ease implementing methods that take no arguments or just one untyped argument. Invoking methods like these runs more efficiently than invoking an equivalent method built on [`METH_VARARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_VARARGS). Furthermore, the older `METH_OLDARGS` way of authoring C methods is from now on officially deprecated.

- A pair of new wrapper functions, [`PyOS_snprintf()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_snprintf) and [`PyOS_vsnprintf()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_vsnprintf), were introduced to supply cross-platform implementations of the fairly recent `snprintf()` and `vsnprintf()` C lib APIs. Unlike the ordinary `sprintf()` and `vsprintf()` functions, the Python flavours verify the buffer's bounds as a guard against buffer overruns. (Contributed by M.-A. Lemburg.)

- An unused parameter has been stripped from the [`_PyTuple_Resize()`](https://docs.python.org/3.14/c-api/tuple.html#c._PyTuple_Resize) function, leaving it with 2 parameters where it had 3. Since that third argument never served any purpose, you can just drop it while porting code from older releases up to Python 2.2.

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules.md) · [Next source section](other-changes-and-fixes.md) · [Release/subject declaration](introduction.md)

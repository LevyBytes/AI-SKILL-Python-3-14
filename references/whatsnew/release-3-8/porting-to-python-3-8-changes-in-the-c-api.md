# What’s New In Python 3.8 / Porting to Python 3.8 / Changes in the C API

### Changes in the C API

- A fresh *cf_feature_version* field has landed in the [`PyCompilerFlags`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyCompilerFlags) structure. You should set it to `PY_MINOR_VERSION`. By default the field gets disregarded; it matters only when the `PyCF_ONLY_AST` flag appears in *cf_flags*. (Contributed by Guido van Rossum in [bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766).)

- Gone from the C API is the `PyEval_ReInitThreads()` function. There is no need to invoke it on purpose: turn to [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) instead. (Contributed by Victor Stinner in [bpo-36728](https://bugs.python.org/issue?@action=redirect&bpo=36728).)

- Under Unix, save for Android and Cygwin, C extensions no longer link against libpython. With Python embedded, `libpython` has to be loaded using `RTLD_GLOBAL` rather than `RTLD_LOCAL`. Previously under `RTLD_LOCAL`, you already could not load C extensions that weren't linked to `libpython`, such as the standard library's C extensions assembled by the `*shared*` section of `Modules/Setup`. (Contributed by Victor Stinner in [bpo-21536](https://bugs.python.org/issue?@action=redirect&bpo=21536).)

- Employing `#` variants of formats while parsing or building value (for example [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple), [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue), [`PyObject_CallFunction()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallFunction), and so on) when `PY_SSIZE_T_CLEAN` is not defined now triggers `DeprecationWarning`. Removal is slated for 3.10 or 4.0. Consult [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) for the specifics. (Contributed by Inada Naoki in [bpo-36381](https://bugs.python.org/issue?@action=redirect&bpo=36381).)

- An instance of a heap-allocated type (such as one produced via [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec)) keeps a reference back to its type object. The bump to such type objects' reference count has shifted out of [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) and down into the lower-level [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) and `PyObject_INIT` functions. This brings types built through `PyType_FromSpec()` into line with other classes in managed code.

[Statically allocated types](https://docs.python.org/3.14/c-api/typeobj.html#static-types) remain unaffected.

In nearly every case nothing should change. Even so, any type that bumps the reference count by hand after allocating an instance (perhaps as a workaround for the bug) could become immortal as a result. To prevent that, such classes must call Py_DECREF on the type object while deallocating the instance.

For a correct port of these types over to 3.8, apply the changes below:

  - Strip the [`Py_INCREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) on the type object that follows allocating an instance - where present. That can come after a call to [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New), [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar), [`PyObject_GC_New()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New), [`PyObject_GC_NewVar()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar), or whatever custom allocator draws on [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) or `PyObject_INIT`.

Example:

```c
static foo_struct *
foo_new(PyObject *type) {
    foo_struct *foo = PyObject_GC_New(foo_struct, (PyTypeObject *) type);
    if (foo == NULL)
        return NULL;
#if PY_VERSION_HEX < 0x03080000
    // Workaround for Python issue 35810; no longer necessary in Python 3.8
    PY_INCREF(type)
#endif
    return foo;
}

```

  - See to it that each custom `tp_dealloc` function on a heap-allocated type drops the type's reference count.

Example:

```c
static void
foo_dealloc(foo_struct *instance) {
    PyObject *type = Py_TYPE(instance);
    PyObject_GC_Del(instance);
#if PY_VERSION_HEX >= 0x03080000
    // This was not needed before Python 3.8 (Python issue 35810)
    Py_DECREF(type);
#endif
}

```

(Contributed by Eddie Elizondo in [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810).)

- MSVC now has an implementation of the [`Py_DEPRECATED()`](https://docs.python.org/3.14/c-api/intro.html#c.Py_DEPRECATED) macro. The macro is now required to sit ahead of the symbol name.

Example:

```c
Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void);

```

(Contributed by Zackery Spytz in [bpo-33407](https://bugs.python.org/issue?@action=redirect&bpo=33407).)

- The interpreter has stopped claiming binary compatibility for extension types from one feature release to the next. Whatever [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) a third-party extension module exports is expected to carry every slot the current Python version anticipates, [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) among them ([`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE) is no longer consulted ahead of reading `tp_finalize`).

(Contributed by Antoine Pitrou in [bpo-32388](https://bugs.python.org/issue?@action=redirect&bpo=32388).)

- Two more `int` arguments, *end_lineno* and *end_col_offset*, are now taken by the functions `PyNode_AddChild()` and `PyParser_AddToken()`.

- The standard Windows distribution no longer ships the `libpython38.a` file that lets MinGW tools link straight against `python38.dll`. Should you need that file, it can be produced with the `gendef` and `dlltool` tools out of the MinGW binutils package:

```shell
gendef - python38.dll > tmp.def
dlltool --dllname python38.dll --def tmp.def --output-lib libpython38.a

```

Where an installed `pythonXY.dll` ends up hinges on the chosen installation options together with the Windows version and language. Look at [Using Python on Windows](https://docs.python.org/3.14/using/windows.html#using-on-windows) for further detail. Drop the resulting library into the very directory that holds `pythonXY.lib`, which usually is the `libs` directory beneath your Python installation.

(Contributed by Steve Dower in [bpo-37351](https://bugs.python.org/issue?@action=redirect&bpo=37351).)

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Release/subject declaration](assignment-expressions.md) · [Release/subject declaration](porting-to-python-3-8.md) · [Next source section](bytecode-migration-changes.md)

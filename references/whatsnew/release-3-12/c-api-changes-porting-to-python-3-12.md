# What’s New In Python 3.12 / C API Changes / Porting to Python 3.12

### Porting to Python 3.12

- Older Unicode interfaces built on the `Py_UNICODE*` representation are now gone. Switch over to interfaces that work through UTF-8 or `wchar_t*`.

- Routines that parse arguments, [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) among them, no longer accept any `Py_UNICODE*` based format (for instance `u` or `Z`). Shift your Unicode handling to alternatives such as `s`, `z`, `es`, and `U`.

- Across every static builtin type, `tp_weaklist` now always holds `NULL`. Even though this is purely an internal field on `PyTypeObject`, we flag the shift in case any code reaches into the field directly regardless. Sidestep trouble by relying on the published public C-API, or, where that won't do, the internal-only `_PyObject_GET_WEAKREFS_LISTPTR()` macro.

- The internal-only [`PyTypeObject.tp_subclasses`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_subclasses) is no longer guaranteed to hold a usable object pointer. Its declared type became void* to signal that fact. We flag it here should any code be reaching straight into the internal-only field.

When you want the roster of subclasses, invoke the Python method [`__subclasses__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__subclasses__) (perhaps via [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod)).

- Extra formatting capabilities (left aligning, octals, uppercase hexadecimals, `intmax_t`, `ptrdiff_t`, `wchar_t` C strings, variable width and precision) were added to [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) plus [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV). (Contributed by Serhiy Storchaka in [gh-98836](https://github.com/python/cpython/issues/98836).)

- When [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) and [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV) meet a format character they cannot parse, they now raise a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Earlier releases instead copied every remaining piece of the format string verbatim into the output and threw away whatever extra arguments remained. (Contributed by Serhiy Storchaka in [gh-95781](https://github.com/python/cpython/issues/95781).)

- Corrected a misplaced sign inside [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) plus [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV). (Contributed by Philip Georgi in [gh-95504](https://github.com/python/cpython/issues/95504).)

- Any extension class that wants a [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) slot or a weak reference slot ought to reach for [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) and [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF) rather than `tp_dictoffset` and `tp_weaklistoffset`. You can still rely on `tp_dictoffset` and `tp_weaklistoffset`, yet they handle multiple inheritance only partially ([gh-95589](https://github.com/python/cpython/issues/95589)) and can run slower. A class that sets `Py_TPFLAGS_MANAGED_DICT` is obligated to invoke `_PyObject_VisitManagedDict()` and `_PyObject_ClearManagedDict()` so its instance dictionaries get traversed and cleared. For weakrefs, keep calling [`PyObject_ClearWeakRefs()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyObject_ClearWeakRefs) just like before.

- The [`PyUnicode_FSDecoder()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSDecoder) routine has stopped taking bytes-like paths such as the [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) types; for byte strings, solely the exact [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type passes. (Contributed by Victor Stinner in [gh-98393](https://github.com/python/cpython/issues/98393).)

- Each of the [`Py_CLEAR`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR), [`Py_SETREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_SETREF) and [`Py_XSETREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XSETREF) macros evaluates whatever you pass it a single time now. Should an argument carry side effects, those effects will no longer occur twice. (Contributed by Victor Stinner in [gh-98724](https://github.com/python/cpython/issues/98724).)

- From now on the interpreter keeps its error indicator normalized at all times. As a result [`PyErr_SetObject()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetObject), [`PyErr_SetString()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetString) plus every sibling that assigns the error indicator will normalize the exception ahead of stashing it. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

- `_Py_RefTotal` no longer carries authority and survives purely for ABI compatibility. Bear in mind it is an internal global surfaced only within debug builds. Should you happen to depend on it, switch over to `_Py_GetGlobalRefTotal()`.

- These functions will now pick a fitting metaclass for whatever type is freshly created:

  - [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec)

  - [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases)

  - [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec)

Building classes whose metaclass replaces [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) is now deprecated and will be forbidden once Python 3.14+ arrives. Be aware that these functions skip the metaclass's `tp_new`, which can leave initialization incomplete.

Keep in mind that [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass) (introduced with Python 3.12) already refuses to build classes whose metaclass replaces `tp_new` ([`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) over in Python).

Because `tp_new` supersedes nearly all of what the `PyType_From*` functions accomplish, the pair simply cannot coexist. The old behavior — sidestepping the metaclass through several stages of building a type — is broadly unsafe, given that (meta)classes presume `tp_new` ran. No tidy universal fix exists. Any one of the approaches below might suit you:

  - When the metaclass is yours to govern, steer clear of `tp_new` within it:

    - Where setup is optional, shift it into [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) instead.

    -

Where Python never has to instantiate the metaclass, blank its `tp_new` to `NULL` through the [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION) flag. That renders it fine for the `PyType_From*` functions.

  - Skip the `PyType_From*` functions altogether: when you can do without C-specific extras (slots or fixing the instance size), build types by [calling](https://docs.python.org/3.14/c-api/call.html#call) the metaclass.

  - Once you *know* dropping the `tp_new` is harmless, silence the deprecation warning through [`warnings.catch_warnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) over in Python.

- Neither [`PyOS_InputHook`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_InputHook) nor [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) fires inside [subinterpreters](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support) any longer. The reason is that callers tend to lean on process-wide global state (these callbacks own no means of restoring extension module state).

It also keeps extensions out of the bind where they end up executing in a subinterpreter they don't support (or that they haven't been loaded into yet). Browse [gh-104668](https://github.com/python/cpython/issues/104668) for the details.

- [`PyLongObject`](https://docs.python.org/3.14/c-api/long.html#c.PyLongObject) received reworked internals aimed at stronger performance. Even though the guts of `PyLongObject` count as private, certain extension modules lean on them. Stop touching the internal fields directly; reach for the API functions whose names start with `PyLong_...` in their place. A pair of fresh *unstable* API functions now exist so you can quickly read the value of any `PyLongObject` that lands inside one machine word:

  - [`PyUnstable_Long_IsCompact()`](https://docs.python.org/3.14/c-api/long.html#c.PyUnstable_Long_IsCompact)

  - [`PyUnstable_Long_CompactValue()`](https://docs.python.org/3.14/c-api/long.html#c.PyUnstable_Long_CompactValue)

- Whatever custom allocators you register through [`PyMem_SetAllocator()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetAllocator) must henceforth be thread-safe, no matter which memory domain applies. Allocators carrying no state of their own, the "hooks" included, escape this rule. Where your custom allocator isn't thread-safe yet and you want a hand, kindly open a fresh GitHub issue and CC `@ericsnowcurrently`.

[Subject index](INDEX.md) · [Previous source section](opaque-reference-counting-calls.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Next source section](c-api-changes-deprecated-deprecated.md)

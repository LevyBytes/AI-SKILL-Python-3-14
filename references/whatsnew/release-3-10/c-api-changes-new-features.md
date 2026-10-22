# What's New In Python 3.10 / C API Changes / New Features — datetime, gc

### New Features

- What [`PyNumber_Index()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Index) returns now is guaranteed to have the exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). In earlier releases the return value could be an instance of an `int` subclass. (Contributed by Serhiy Storchaka in [bpo-40792](https://bugs.python.org/issue?@action=redirect&bpo=40792).)

- Add a new [`orig_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.orig_argv) member to the [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) structure, holding the list of the original command line arguments handed to the Python executable. (Contributed by Victor Stinner in [bpo-23427](https://bugs.python.org/issue?@action=redirect&bpo=23427).)

- The [`PyDateTime_DATE_GET_TZINFO()`](https://docs.python.org/3.14/c-api/datetime.html#c.PyDateTime_DATE_GET_TZINFO) and [`PyDateTime_TIME_GET_TZINFO()`](https://docs.python.org/3.14/c-api/datetime.html#c.PyDateTime_TIME_GET_TZINFO) macros are now available for reading the `tzinfo` attributes that belong to [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) and [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) objects. (Contributed by Zackery Spytz in [bpo-30155](https://bugs.python.org/issue?@action=redirect&bpo=30155).)

- Add a [`PyCodec_Unregister()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Unregister) function whose job is removing a previously registered codec search function. (Contributed by Hai Shi in [bpo-41842](https://bugs.python.org/issue?@action=redirect&bpo=41842).)

- The [`PyIter_Send()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Send) function arrived so that a value can be sent into an iterator while avoiding any `StopIteration` exception. (Contributed by Vladimir Matveev in [bpo-41756](https://bugs.python.org/issue?@action=redirect&bpo=41756).)

- Add [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize) to the limited C API. (Contributed by Alex Gaynor in [bpo-41784](https://bugs.python.org/issue?@action=redirect&bpo=41784).)

- Add [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef) function: comparable to [`PyModule_AddObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObject) except it does not steal a reference to the value when it succeeds. (Contributed by Victor Stinner in [bpo-1635741](https://bugs.python.org/issue?@action=redirect&bpo=1635741).)

- Add [`Py_NewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef) and [`Py_XNewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XNewRef) functions which bump an object's reference count and hand the object back. (Contributed by Victor Stinner in [bpo-42262](https://bugs.python.org/issue?@action=redirect&bpo=42262).)

- The [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) and [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) functions will now take a single class for the *bases* argument. (Contributed by Serhiy Storchaka in [bpo-42423](https://bugs.python.org/issue?@action=redirect&bpo=42423).)

- The [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) function will now tolerate a NULL `tp_doc` slot. (Contributed by Hai Shi in [bpo-41832](https://bugs.python.org/issue?@action=redirect&bpo=41832).)

- The [`PyType_GetSlot()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetSlot) function is now able to take [static types](https://docs.python.org/3.14/c-api/typeobj.html#static-types). (Contributed by Hai Shi and Petr Viktorin in [bpo-41073](https://bugs.python.org/issue?@action=redirect&bpo=41073).)

- Add a new [`PySet_CheckExact()`](https://docs.python.org/3.14/c-api/set.html#c.PySet_CheckExact) function to the C-API for verifying whether an object is an instance of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) yet not an instance of a subtype. (Contributed by Pablo Galindo in [bpo-43277](https://bugs.python.org/issue?@action=redirect&bpo=43277).)

- Add [`PyErr_SetInterruptEx()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetInterruptEx) which lets you hand over a signal number to simulate. (Contributed by Antoine Pitrou in [bpo-43356](https://bugs.python.org/issue?@action=redirect&bpo=43356).)

- The limited C API now works even when [Python is built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) (whenever the `Py_DEBUG` macro is defined). Within the limited C API, the [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) and [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) functions are now realized as opaque function calls instead of touching the [`PyObject.ob_refcnt`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_refcnt) member directly, provided Python is compiled in debug mode and the `Py_LIMITED_API` macro is aimed at Python 3.10 or a later version. Supporting the limited C API in debug mode turned out to be feasible because the [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) structure stays identical across release and debug mode going back to Python 3.8 (see [bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465)).

The limited C API remains unsupported within the [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) special build (`Py_TRACE_REFS` macro). (Contributed by Victor Stinner in [bpo-43688](https://bugs.python.org/issue?@action=redirect&bpo=43688).)

- Add the [`Py_Is(x, y)`](https://docs.python.org/3.14/c-api/structures.html#c.Py_Is) function for checking whether the *x* object is the *y* object, equivalent to `x is y` in Python. Also added are the [`Py_IsNone()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsNone), [`Py_IsTrue()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsTrue), [`Py_IsFalse()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsFalse) functions for checking whether an object is, in turn, the `None` singleton, the `True` singleton or the `False` singleton. (Contributed by Victor Stinner in [bpo-43753](https://bugs.python.org/issue?@action=redirect&bpo=43753).)

- Add new functions for steering the garbage collector from C code: [`PyGC_Enable()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Enable), [`PyGC_Disable()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Disable), [`PyGC_IsEnabled()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_IsEnabled). With these functions you can turn on, turn off and inspect the garbage collector's state straight from C code, sparing you the need to import the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module.

- Add a new [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION) type flag that blocks the creation of type instances. (Contributed by Victor Stinner in [bpo-43916](https://bugs.python.org/issue?@action=redirect&bpo=43916).)

- Add a new [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) type flag used to build immutable type objects: no setting or deleting of their type attributes is permitted. (Contributed by Victor Stinner and Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-pep-652-maintaining-the-stable-abi.md) · [Next source section](c-api-changes-porting-to-python-3-10.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md)

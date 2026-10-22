# What's New In Python 3.9 / C API Changes / New Features

### C API Changes

### New Features

- [**PEP 573**](https://peps.python.org/pep-0573/): Introduced [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) for tying a module to a class; [`PyType_GetModule()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModule) along with [`PyType_GetModuleState()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleState) for fetching that module plus its state; and both [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod) and [`METH_METHOD`](https://docs.python.org/3.14/c-api/structures.html#c.METH_METHOD) so a method can get at the class where it was defined. (Contributed by Marcel Plch and Petr Viktorin in [bpo-38787](https://bugs.python.org/issue?@action=redirect&bpo=38787).)

- Introduced the [`PyFrame_GetCode()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetCode) function for obtaining a frame’s code, and the [`PyFrame_GetBack()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBack) function for obtaining the frame just outside the current one. (Contributed by Victor Stinner in [bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421).)

- Brought [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber) into the limited C API. (Contributed by Victor Stinner in [bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421).)

- Introduced the [`PyThreadState_GetInterpreter()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetInterpreter) and [`PyInterpreterState_Get()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Get) functions for reaching the interpreter. Introduced the [`PyThreadState_GetFrame()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetFrame) function for grabbing the current frame belonging to a Python thread state. Introduced the [`PyThreadState_GetID()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetID) function for reading a Python thread state’s one-of-a-kind identifier. (Contributed by Victor Stinner in [bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947).)

- Brought a fresh public [`PyObject_CallNoArgs()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallNoArgs) function into the C API; it invokes a callable Python object passing nothing at all. For invoking such an object with no argument, this is the fastest route available. (Contributed by Victor Stinner in [bpo-37194](https://bugs.python.org/issue?@action=redirect&bpo=37194).)

- Changes in the limited C API (if `Py_LIMITED_API` macro is defined):

  - Offer [`Py_EnterRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_EnterRecursiveCall) together with [`Py_LeaveRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_LeaveRecursiveCall) as ordinary functions under the limited API. Up to now they came as macros, yet those macros failed to compile against the limited C API, which has no way to touch the `PyThreadState.recursion_depth` field — that structure stays opaque in the limited C API.

  - `PyObject_INIT()` and `PyObject_INIT_VAR()` turn into ordinary “opaque” functions that tuck the implementation details out of sight.

(Contributed by Victor Stinner in [bpo-38644](https://bugs.python.org/issue?@action=redirect&bpo=38644) and [bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542).)

- The [`PyModule_AddType()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddType) function arrives to ease registering a type onto a module. (Contributed by Donghee Na in [bpo-40024](https://bugs.python.org/issue?@action=redirect&bpo=40024).)

- Brought the [`PyObject_GC_IsTracked()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_IsTracked) and [`PyObject_GC_IsFinalized()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_IsFinalized) functions into the public API so you can ask whether the garbage collector is presently tracking Python objects or has already finalized them, respectively. (Contributed by Pablo Galindo Salgado in [bpo-40241](https://bugs.python.org/issue?@action=redirect&bpo=40241).)

- Brought in `_PyObject_FunctionStr()`, which yields a reader-friendly string form of a function-like object. (Patch by Jeroen Demeyer in [bpo-37645](https://bugs.python.org/issue?@action=redirect&bpo=37645).)

- Brought in [`PyObject_CallOneArg()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallOneArg) for invoking an object with a single positional argument (Patch by Jeroen Demeyer in [bpo-37483](https://bugs.python.org/issue?@action=redirect&bpo=37483).)

[Subject index](INDEX.md) · [Previous source section](build-changes.md) · [Next source section](c-api-changes-porting-to-python-3-9.md) · [Release/subject declaration](summary-release-highlights.md)

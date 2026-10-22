# What's New In Python 3.9 / C API Changes / Removed

### Removed

- Kept the `PyFPE_START_PROTECT()` and `PyFPE_END_PROTECT()` macros from `pyfpe.h` out of the limited C API. (Contributed by Victor Stinner in [bpo-38835](https://bugs.python.org/issue?@action=redirect&bpo=38835).)

- The `tp_print` slot on [PyTypeObject](https://docs.python.org/3.14/c-api/typeobj.html#type-structs) is gone. Back in Python 2.7 and earlier it served to print objects out to files. From Python 3.0 onward it sat idle and untouched. (Contributed by Jeroen Demeyer in [bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974).)

- Changes in the limited C API (if `Py_LIMITED_API` macro is defined):

  - Excluded the following functions from the limited C API:

    - `PyThreadState_DeleteCurrent()` (Contributed by Joannah Nanjekye in [bpo-37878](https://bugs.python.org/issue?@action=redirect&bpo=37878).)

    - `_Py_CheckRecursionLimit`

    - `_Py_NewReference()`

    - `_Py_ForgetReference()`

    - `_PyTraceMalloc_NewReference()`

    - `_Py_GetRefTotal()`

    - The trashcan mechanism which never worked in the limited C API.

    - `PyTrash_UNWIND_LEVEL`

    - `Py_TRASHCAN_BEGIN_CONDITION`

    - `Py_TRASHCAN_BEGIN`

    - `Py_TRASHCAN_END`

    - `Py_TRASHCAN_SAFE_BEGIN`

    - `Py_TRASHCAN_SAFE_END`

  - Moved following functions and definitions to the internal C API:

    - `_PyDebug_PrintTotalRefs()`

    - `_Py_PrintReferences()`

    -

`_Py_PrintReferenceAddresses()`

    - `_Py_tracemalloc_config`

    - `_Py_AddToAllObjects()` (specific to `Py_TRACE_REFS` build)

(Contributed by Victor Stinner in [bpo-38644](https://bugs.python.org/issue?@action=redirect&bpo=38644) and [bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542).)

- Dropped the `_PyRuntime.getframe` hook plus the `_PyThreadState_GetFrame` macro that aliased `_PyRuntime.getframe`. Only the internal C API ever surfaced them. The `PyThreadFrameGetter` type went away as well. (Contributed by Victor Stinner in [bpo-39946](https://bugs.python.org/issue?@action=redirect&bpo=39946).)

- Took the functions below out of the C API. To wipe every free list, invoke [`PyGC_Collect()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Collect) yourself. (Contributed by Inada Naoki and Victor Stinner in [bpo-37340](https://bugs.python.org/issue?@action=redirect&bpo=37340), [bpo-38896](https://bugs.python.org/issue?@action=redirect&bpo=38896) and [bpo-40428](https://bugs.python.org/issue?@action=redirect&bpo=40428).)

  - `PyAsyncGen_ClearFreeLists()`

  - `PyContext_ClearFreeList()`

  - `PyDict_ClearFreeList()`

  - `PyFloat_ClearFreeList()`

  - `PyFrame_ClearFreeList()`

  - `PyList_ClearFreeList()`

  - `PyMethod_ClearFreeList()` and `PyCFunction_ClearFreeList()`: the free lists that held bound method objects are gone.

  - `PySet_ClearFreeList()`: Python 3.4 already did away with the set free list.

  - `PyTuple_ClearFreeList()`

  - `PyUnicode_ClearFreeList()`: Python 3.3 already did away with the Unicode free list.

- Removed `_PyUnicode_ClearStaticStrings()` function. (Contributed by Victor Stinner in [bpo-39465](https://bugs.python.org/issue?@action=redirect&bpo=39465).)

- Dropped `Py_UNICODE_MATCH`. [**PEP 393**](https://peps.python.org/pep-0393/) had deprecated it, and it had stayed broken from Python 3.3 onward. Reach for the [`PyUnicode_Tailmatch()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Tailmatch) function in its stead. (Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- Scrubbed the header files of interfaces that were declared yet never implemented. The public API symbols on the way out are: `_PyBytes_InsertThousandsGroupingLocale`, `_PyBytes_InsertThousandsGrouping`, `_Py_InitializeFromArgs`, `_Py_InitializeFromWideArgs`, `_PyFloat_Repr`, `_PyFloat_Digits`, `_PyFloat_DigitsInit`, `PyFrame_ExtendStack`, `_PyAIterWrapper_Type`, `PyNullImporter_Type`, `PyCmpWrapper_Type`, `PySortWrapper_Type`, `PyNoArgsFunction`. (Contributed by Pablo Galindo Salgado in [bpo-39372](https://bugs.python.org/issue?@action=redirect&bpo=39372).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-porting-to-python-3-9.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Next source section](typing.md)

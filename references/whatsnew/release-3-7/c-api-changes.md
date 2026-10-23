# What's New In Python 3.7 / C API Changes - tracemalloc

### C API Changes

Thread-local storage now has a new API. Consult PEP 539: New C API for Thread-Local Storage for the overview, and [Thread-specific storage API](https://docs.python.org/3.14/c-api/tls.html#thread-specific-storage-api) for the full reference. (Contributed by Masayuki Yamamoto in [bpo-25658](https://bugs.python.org/issue?@action=redirect&bpo=25658).)

A set of [new C APIs](https://docs.python.org/3.14/c-api/contextvars.html#contextvarsobjects) is surfaced by the freshly added context variables functionality.

Given a name, the freshly added [`PyImport_GetModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_GetModule) function returns the module that was imported earlier. (Contributed by Eric Snow in [bpo-28411](https://bugs.python.org/issue?@action=redirect&bpo=28411).)

Writing rich comparison functions is made simpler by the freshly added [`Py_RETURN_RICHCOMPARE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_RETURN_RICHCOMPARE) macro. (Contributed by Petr Victorin in [bpo-23699](https://bugs.python.org/issue?@action=redirect&bpo=23699).)

To flag code paths that can never be reached, the freshly added [`Py_UNREACHABLE`](https://docs.python.org/3.14/c-api/intro.html#c.Py_UNREACHABLE) macro is available. (Contributed by Barry Warsaw in [bpo-31338](https://bugs.python.org/issue?@action=redirect&bpo=31338).)

By way of the freshly added [`PyTraceMalloc_Track()`](https://docs.python.org/3.14/c-api/memory.html#c.PyTraceMalloc_Track) and [`PyTraceMalloc_Untrack()`](https://docs.python.org/3.14/c-api/memory.html#c.PyTraceMalloc_Untrack) functions, [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) now offers a C API. (Contributed by Victor Stinner in [bpo-30054](https://bugs.python.org/issue?@action=redirect&bpo=30054).)

To trace module imports, the freshly added [import__find__load__start](https://docs.python.org/3.14/howto/instrumentation.html#static-markers) and [import__find__load__done](https://docs.python.org/3.14/howto/instrumentation.html#static-markers) static markers are available. (Contributed by Christian Heimes in [bpo-31574](https://bugs.python.org/issue?@action=redirect&bpo=31574).)

Across the structures [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef), [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef), [`PyStructSequence_Field`](https://docs.python.org/3.14/c-api/tuple.html#c.PyStructSequence_Field), [`PyStructSequence_Desc`](https://docs.python.org/3.14/c-api/tuple.html#c.PyStructSequence_Desc), and `wrapperbase`, the `name` and `doc` fields are now typed `const char *` instead of `char *`. (Contributed by Serhiy Storchaka in [bpo-28761](https://bugs.python.org/issue?@action=redirect&bpo=28761).)

What [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize) and [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8) return is now typed `const char *` instead of `char *`. (Contributed by Serhiy Storchaka in [bpo-28769](https://bugs.python.org/issue?@action=redirect&bpo=28769).)

What [`PyMapping_Keys()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Keys), [`PyMapping_Values()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Values) and [`PyMapping_Items()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Items) return is now invariably a list, no longer a list or a tuple. (Contributed by Oren Milman in [bpo-28280](https://bugs.python.org/issue?@action=redirect&bpo=28280).)

The functions [`PySlice_Unpack()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_Unpack) and [`PySlice_AdjustIndices()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_AdjustIndices) were added. (Contributed by Serhiy Storchaka in [bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).)

In favour of the freshly added [`PyOS_BeforeFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_BeforeFork), [`PyOS_AfterFork_Parent()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Parent) and [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) functions, [`PyOS_AfterFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork) is deprecated. (Contributed by Antoine Pitrou in [bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

Formerly part of the public API, the `PyExc_RecursionErrorInst` singleton has been dropped, since its members never being cleared could trigger a segfault as the interpreter finalizes. Contributed by Xavier de Gaye in [bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898) and [bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697).

C API coverage for timezones was added via the timezone constructors [`PyTimeZone_FromOffset()`](https://docs.python.org/3.14/c-api/datetime.html#c.PyTimeZone_FromOffset) and [`PyTimeZone_FromOffsetAndName()`](https://docs.python.org/3.14/c-api/datetime.html#c.PyTimeZone_FromOffsetAndName), plus reach to the UTC singleton through [`PyDateTime_TimeZone_UTC`](https://docs.python.org/3.14/c-api/datetime.html#c.PyDateTime_TimeZone_UTC). Contributed by Paul Ganssle in [bpo-10381](https://bugs.python.org/issue?@action=redirect&bpo=10381).

For `PyThread_start_new_thread()` and `PyThread_get_thread_ident()`, the result type, together with the *id* parameter of [`PyThreadState_SetAsyncExc()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_SetAsyncExc), shifted from long to unsigned long. (Contributed by Serhiy Storchaka in [bpo-6532](https://bugs.python.org/issue?@action=redirect&bpo=6532).)

Should its second argument be `NULL` while the wchar_t* string holds null characters, [`PyUnicode_AsWideCharString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideCharString) now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Serhiy Storchaka in [bpo-30708](https://bugs.python.org/issue?@action=redirect&bpo=30708).)

Because the startup sequence and the handling of dynamic memory allocators have changed, the long-documented rule that [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) must run before most C API functions is now leaned on more heavily, and ignoring it can cause segfaults in embedding applications. For further detail, see the Porting to Python 3.7 section in this document together with the [Before Python initialization](https://docs.python.org/3.14/c-api/interp-lifecycle.html#pre-init-safe) section of the C API documentation.

For any given interpreter, the freshly added [`PyInterpreterState_GetID()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_GetID) returns its unique ID. (Contributed by Eric Snow in [bpo-29102](https://bugs.python.org/issue?@action=redirect&bpo=29102).)

Whenever UTF-8 mode is turned on, [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale), [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale) now apply the UTF-8 encoding. (Contributed by Victor Stinner in [bpo-29240](https://bugs.python.org/issue?@action=redirect&bpo=29240).)

For the `surrogateescape` error handler, [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize) and [`PyUnicode_EncodeLocale()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeLocale) now apply the current locale encoding. (Contributed by Victor Stinner in [bpo-29240](https://bugs.python.org/issue?@action=redirect&bpo=29240).)

So that they act like string slices, the *start* and *end* parameters of [`PyUnicode_FindChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FindChar) are now adjusted. (Contributed by Xiang Zhang in [bpo-28822](https://bugs.python.org/issue?@action=redirect&bpo=28822).)

[Subject index](INDEX.md) · [Previous source section](zipfile.md) · [Next source section](build-changes.md) · [Release/subject declaration](summary-release-highlights.md)

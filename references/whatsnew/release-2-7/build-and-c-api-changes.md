# What’s New in Python 2.7 / Build and C API Changes

### Build and C API Changes

The changes affecting Python’s build process and its C API are as follows:

- GDB 7, the newest release of the GNU Debugger, can be [scripted using Python](https://web.archive.org/web/20110715084810/http://sourceware.org/gdb/current/onlinedocs/gdb/Python.html). As you start debugging an executable program P, GDB hunts for a file named `P-gdb.py` and reads it automatically. Dave Malcolm provided a `python-gdb.py` that supplies several commands handy when you’re debugging Python itself. For instance, `py-up` and `py-down` move you up or down by one Python stack frame, which generally maps to several C stack frames. `py-print` displays the value held by a Python variable, while `py-bt` prints out the Python stack trace. (Added as a result of [bpo-8032](https://bugs.python.org/issue?@action=redirect&bpo=8032).)

- When you rely on the `.gdbinit` file shipped with Python, the “pyo” macro in the 2.7 version now behaves correctly when the thread under debugging is not holding the GIL; the macro now acquires it ahead of printing. (Contributed by Victor Stinner; [bpo-3632](https://bugs.python.org/issue?@action=redirect&bpo=3632).)

- [`Py_AddPendingCall()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_AddPendingCall) is now thread-safe, so any worker thread can hand notifications off to the main Python thread. That comes in especially handy for asynchronous IO work. (Contributed by Kristján Valur Jónsson; [bpo-4293](https://bugs.python.org/issue?@action=redirect&bpo=4293).)

- New function: [`PyCode_NewEmpty()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_NewEmpty) builds an empty code object, requiring only the filename, the function name, and the first line number. This helps extension modules that are trying to assemble a more informative traceback stack. Formerly such extensions had to call `PyCode_New()`, which demanded a far longer list of arguments. (Added by Jeffrey Yasskin.)

- New function: [`PyErr_NewExceptionWithDoc()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewExceptionWithDoc) builds a new exception class in the same way the existing [`PyErr_NewException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewException) does, but accepts an extra `char *` argument that carries the new class’s docstring. (Added by ‘lekma’ on the Python bug tracker; [bpo-7033](https://bugs.python.org/issue?@action=redirect&bpo=7033).)

- New function: [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber) accepts a frame object and gives back the line number the frame is currently running. Previously code had to fetch the index of the bytecode instruction in progress and then look up the line number that the address corresponds to. (Added by Jeffrey Yasskin.)

- New functions: [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongAndOverflow) and [`PyLong_AsLongLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongLongAndOverflow) render a Python long integer roughly as a C long or long long. When the number is too big for the destination type, an *overflow* flag gets set and passed back to the caller. (Contributed by Case Van Horsen; [bpo-7528](https://bugs.python.org/issue?@action=redirect&bpo=7528) and [bpo-7767](https://bugs.python.org/issue?@action=redirect&bpo=7767).)

- New function: as an outgrowth of the rewritten string-to-float conversion, a new [`PyOS_string_to_double()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_string_to_double) function was added. The former `PyOS_ascii_strtod()` and `PyOS_ascii_atof()` functions are now deprecated.

- New function: `PySys_SetArgvEx()` assigns the value of `sys.argv` and may optionally amend `sys.path` to add the directory holding the script named by `sys.argv[0]`, depending on what an *updatepath* parameter is set to.

The addition of this function closed a security gap affecting programs that embed Python. Its predecessor, `PySys_SetArgv()`, always refreshed `sys.path` and on occasion appended the working directory. Consequently, launching a Python-embedding program from a directory under another party's control let an attacker drop a Trojan-horse module there (for instance, a file called `os.py`) that the program would import and execute.

Maintainers of a C/C++ program that embeds Python should look at whether `PySys_SetArgv()` is being invoked and weigh carefully whether `PySys_SetArgvEx()` with *updatepath* set to false would be the better choice.

The vulnerability was filed as [**CVE 2008-5983**](https://www.cve.org/CVERecord?id=CVE-2008-5983); the conversation lives in [bpo-5753](https://bugs.python.org/issue?@action=redirect&bpo=5753), with the repair credited to Antoine Pitrou.

- New macros: these macros are now declared by the Python header files: [`Py_ISALNUM`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISALNUM), [`Py_ISALPHA`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISALPHA), [`Py_ISDIGIT`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISDIGIT), [`Py_ISLOWER`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISLOWER), [`Py_ISSPACE`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISSPACE), [`Py_ISUPPER`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISUPPER), [`Py_ISXDIGIT`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_ISXDIGIT), [`Py_TOLOWER`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_TOLOWER), and [`Py_TOUPPER`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_TOUPPER). Each parallels the C standard character-classification macros while disregarding the active locale, since Python in various spots has to examine characters without depending on locale. (Added by Eric Smith; [bpo-5793](https://bugs.python.org/issue?@action=redirect&bpo=5793).)

- Removed function: `PyEval_CallObject()` survives only as a macro now. The function form had been retained for ABI linking compatibility, but that dated back to 1997; deleting it at this stage is surely safe. (Removed by Antoine Pitrou; [bpo-8276](https://bugs.python.org/issue?@action=redirect&bpo=8276).)

- New format codes: the trio `PyString_FromFormat()`, `PyString_FromFormatV()`, and [`PyErr_Format()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Format) will now take the `%lld` and `%llu` format codes that render C's long long types. (Contributed by Mark Dickinson; [bpo-7228](https://bugs.python.org/issue?@action=redirect&bpo=7228).)

- The tangled relationship between threads and process forking has been reworked. Formerly a child process spawned by [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) could break, because that child begins with just one thread active, namely the thread that ran the `os.fork()`. Should any other thread have been holding a lock at fork time, for example Python's import lock, that lock would remain flagged as "held" inside the fresh process. Yet nothing in the child would ever free it, because the remaining threads weren't duplicated, leaving the child unable to carry out imports anymore.

Before it calls [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork), Python 2.7 takes the import lock, and it also tidies up whatever locks were made via the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module. This cleanup won't help C extension modules carrying their own internal locks, nor those that invoke `fork()` directly.

(Fixed by Thomas Wouters; [bpo-1590864](https://bugs.python.org/issue?@action=redirect&bpo=1590864).)

- The [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) function will now invoke the internal `threading._shutdown()` function, which stops certain exceptions from surfacing as an interpreter winds down. (Patch by Adam Olsen; [bpo-1722344](https://bugs.python.org/issue?@action=redirect&bpo=1722344).)

- If you rely on the [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) structure to declare a type's attributes, Python will from now on refuse any attempt to delete or assign a `T_STRING_INPLACE` attribute.

- Global symbols exported by the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module now carry a `Py` prefix, or else a `_ctypes` one. (Implemented by Thomas Heller; [bpo-3102](https://bugs.python.org/issue?@action=redirect&bpo=3102).)

- New configure option: the `--with-system-expat` switch makes it possible to compile the [`pyexpat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) module against the system's Expat library. (Contributed by Arfrever Frehtes Taifersar Arahesis; [bpo-7609](https://bugs.python.org/issue?@action=redirect&bpo=7609).)

- New configure option: passing `--with-valgrind` turns off the pymalloc allocator, which the Valgrind memory-error detector struggles to parse properly. As a result Valgrind gains accuracy at spotting memory leaks and overruns. (Contributed by James Henstridge; [bpo-2422](https://bugs.python.org/issue?@action=redirect&bpo=2422).)

- New configure option: supplying an empty string to `--with-dbmliborder=` is now allowed so that every one of the various DBM modules can be switched off. (Added by Arfrever Frehtes Taifersar Arahesis; [bpo-6491](https://bugs.python.org/issue?@action=redirect&bpo=6491).)

- The **configure** script now probes for floating-point rounding defects on some 32-bit Intel chips and, when found, sets a `X87_DOUBLE_ROUNDING` preprocessor definition. Nothing in the codebase relies on it yet, though it stands ready for whoever wants it. (Added by Mark Dickinson; [bpo-2937](https://bugs.python.org/issue?@action=redirect&bpo=2937).)

**configure** additionally defines a `LDCXXSHARED` Makefile variable now, to back C++ linking. (Contributed by Arfrever Frehtes Taifersar Arahesis; [bpo-1222585](https://bugs.python.org/issue?@action=redirect&bpo=1222585).)

- The build now produces the files required for pkg-config support. (Contributed by Clinton Roy; [bpo-3585](https://bugs.python.org/issue?@action=redirect&bpo=3585).)

- Subversion 1.7 is supported by the build now. (Contributed by Arfrever Frehtes Taifersar Arahesis; [bpo-6094](https://bugs.python.org/issue?@action=redirect&bpo=6094).)

[Subject index](INDEX.md) · [Previous source section](updated-module-elementtree-1-3.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Next source section](capsules.md)

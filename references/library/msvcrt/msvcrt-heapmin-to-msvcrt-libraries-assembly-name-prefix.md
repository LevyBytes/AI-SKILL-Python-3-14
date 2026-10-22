# msvcrt — Other Functions

### Other Functions

 msvcrt.heapmin()

Compel the `malloc()` heap to tidy itself and give idle blocks back to the operating system. Any failure here comes through as [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 msvcrt.set_error_mode(*mode*)

Redirect where the C runtime emits the error text for a fault that could terminate the program. Supply *mode* as one of the `OUT_*` constants below, or as `REPORT_ERRMODE`. The previous setting comes back, or -1 should something go wrong. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.OUT_TO_DEFAULT

Where errors land depends on what kind of application is running. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.OUT_TO_STDERR

Errors are routed to standard error. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.OUT_TO_MSGBOX

Errors are shown in a message box. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.REPORT_ERRMODE

Hand back whatever the error mode is set to right now. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.CrtSetReportMode(*type*, *mode*)

Names where output goes — one target or several — for a given report category that `_CrtDbgReport()` produces inside the MS VC++ runtime. Give *type* as one of the `CRT_*` constants below, and *mode* as one of the `CRTDBG_*` constants below. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.CrtSetReportFile(*type*, *file*)

Once `CrtSetReportMode()` has selected `CRTDBG_MODE_FILE`, this lets you point at the file handle that should collect the message text. Give *type* as one of the `CRT_*` constants below, and set *file* to the file handle you intend to use. Present only in a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build).

 msvcrt.CRT_WARN

Cautions, notices, and details that can wait rather than needing a response right away.

 msvcrt.CRT_ERROR

Faults, problems with no recovery path, and matters that have to be dealt with at once.

 msvcrt.CRT_ASSERT

Assertion failures.

 msvcrt.CRTDBG_MODE_DEBUG

Sends the message into the output window of the debugger.

 msvcrt.CRTDBG_MODE_FILE

Sends the message to a file handle that you provide. Call `CrtSetReportFile()` beforehand to nominate the exact file or stream that serves as the target.

 msvcrt.CRTDBG_MODE_WNDW

Pops up a message box that presents the message together with the `Abort`, `Retry`, and `Ignore` buttons.

 msvcrt.CRTDBG_REPORT_MODE

Hands back the *mode* presently in effect for the given *type*.

 msvcrt.CRT_ASSEMBLY_VERSION

The version of the CRT Assembly, as taken from the `crtassem.h` header file.

 msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN

The public key token for the VC Assembly, as taken from the `crtassem.h` header file.

 msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX

The name prefix for the Libraries Assembly, as taken from the `crtassem.h` header file.

[Subject index](INDEX.md) · [Previous](msvcrt-kbhit-to-msvcrt-ungetwch.md) · [Owning module, declaration or section: msvcrt](msvcrt-useful-routines-from-the-ms-vc-runtime.md)

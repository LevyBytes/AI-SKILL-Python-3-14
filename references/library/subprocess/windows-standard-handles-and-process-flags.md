# subprocess: Windows standard handles and process-creation constants

### Windows Constants

The `subprocess` module makes the following constants available.

 subprocess.STD_INPUT_HANDLE

The standard input device. At the outset this is the console input buffer, `CONIN$`.

 subprocess.STD_OUTPUT_HANDLE

The standard output device. At the outset this is the active console screen buffer, `CONOUT$`.

 subprocess.STD_ERROR_HANDLE

The standard error device. At the outset this is the active console screen buffer, `CONOUT$`.

 subprocess.SW_HIDE

Conceals the window. Some other window will then be activated.

 subprocess.STARTF_USESTDHANDLES

Marks that the `STARTUPINFO.hStdInput`, `STARTUPINFO.hStdOutput`, and `STARTUPINFO.hStdError` attributes hold extra information.

 subprocess.STARTF_USESHOWWINDOW

Marks that the `STARTUPINFO.wShowWindow` attribute holds extra information.

 subprocess.STARTF_FORCEONFEEDBACK

A `STARTUPINFO.dwFlags` parameter signaling that the *Working in Background* mouse cursor should appear while a process starts up. For GUI processes this is how things behave by default.

Added in version 3.13.

 subprocess.STARTF_FORCEOFFFEEDBACK

A `STARTUPINFO.dwFlags` parameter signaling that launching a process should leave the mouse cursor untouched.

Added in version 3.13.

 subprocess.CREATE_NEW_CONSOLE

Rather than inheriting the console of its parent (the default), the new process receives a console of its own.

 subprocess.CREATE_NEW_PROCESS_GROUP

A `Popen` `creationflags` parameter signaling that a fresh process group should be created. Using [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill) on the subprocess depends on this flag.

When `CREATE_NEW_CONSOLE` is given, this flag has no effect.

 subprocess.ABOVE_NORMAL_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at above-average priority.

Added in version 3.7.

 subprocess.BELOW_NORMAL_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at below-average priority.

Added in version 3.7.

 subprocess.HIGH_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at high priority.

Added in version 3.7.

 subprocess.IDLE_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at idle (the lowest) priority.

Added in version 3.7.

 subprocess.NORMAL_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at normal priority. (default)

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](windows-popen-helpers.md) · [Continue](windows-process-priority-and-job-flags.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

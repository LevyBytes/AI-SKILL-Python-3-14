# sys.remote_exec

sys.remote_exec(*pid*, *script*)

Runs *script* — a file holding Python code — inside the remote process identified by the supplied *pid*.

The call comes back right away, while the code itself runs on the target process’s main thread at its next free moment, much the way signals get serviced. No interface tells you when that code has actually run. It falls to the caller to guarantee the file is still present, and not overwritten, by the time the remote process goes to read it.

The remote process has to be running a CPython interpreter whose major and minor version match the local one. Should either the local or the remote interpreter be a pre-release (alpha, beta, or release candidate), the two interpreters must match down to the exact version.

Consult [Remote debugging attachment protocol](https://docs.python.org/3.14/howto/remote_debugging.html#remote-debugging) for fuller detail on how the remote debugging mechanism works.

As the code runs inside the remote process, an auditing event `sys.remote_exec` fires carrying the *pid* and the path to the script file. That event fires within the process that invoked `sys.remote_exec()`.

As the script runs inside the remote process, an auditing event `cpython.remote_debugger_script` fires carrying the path as seen in the remote process. That event fires inside the remote process rather than the one that invoked `sys.remote_exec()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Added in version 3.14: See [**PEP 768**](https://peps.python.org/pep-0768/) for more details.

[API family](INDEX.md) · [sys context index](../INDEX.md).

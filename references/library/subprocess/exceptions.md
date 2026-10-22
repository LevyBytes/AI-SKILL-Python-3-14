# subprocess — Exceptions

### Exceptions

Should the child process raise exceptions before the fresh program begins running, those exceptions get re-raised back in the parent.

By far the most frequent exception is [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). It shows up, for instance, on an attempt to run a file that does not exist. Code should be ready to handle `OSError` exceptions. Keep in mind that with `shell=True`, the child raises `OSError` only when the chosen shell itself could not be located. Figuring out whether the shell could not locate the requested application means inspecting the return code or the subprocess output.

If `Popen` is invoked with invalid arguments, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

When the invoked process exits with a non-zero return code, `check_call()` and `check_output()` raise `CalledProcessError`.

Every function and method that takes a *timeout* parameter, including `run()` and `Popen.communicate()`, raises `TimeoutExpired` should the timeout elapse before the process finishes.

The exceptions this module defines all derive from `SubprocessError`.

Added in version 3.3: The `SubprocessError` base class was added.

[Subject index](INDEX.md) · [Previous](popen-creation-flags-and-stream-buffers.md) · [Continue](security-considerations.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

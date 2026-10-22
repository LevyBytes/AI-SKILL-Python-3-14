# Python 3.9.0 alpha 2 / library / exceptions

[bpo-39033](https://bugs.python.org/issue?@action=redirect&bpo=39033): Resolve a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) within [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport). Karthikeyan Singaravelan authored the patch.

[bpo-38982](https://bugs.python.org/issue?@action=redirect&bpo=38982): Repair asyncio `PidfdChildWatcher` so it copes with a `waitpid()` error. Should `waitpid()` run elsewhere, the `waitpid()` invocation fails with [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError): the code then uses return code 255 and emits a warning. This guarantees the pidfd file descriptor gets closed whenever the error shows up.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

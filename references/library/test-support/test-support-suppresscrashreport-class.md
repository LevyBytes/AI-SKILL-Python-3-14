# test.support`test.support` - Utilities for the Python test suite

*class *test.support.SuppressCrashReport

A context manager that attempts to keep crash dialog popups from appearing during tests expected to crash a subprocess.

Under Windows, it turns off Windows Error Reporting dialogs through [SetErrorMode](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680621.aspx).

Under UNIX, [`resource.setrlimit()`](https://docs.python.org/3.14/library/resource.html#resource.setrlimit) serves to lower [`resource.RLIMIT_CORE`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_CORE)'s soft limit to 0 so that no coredump file is written.

On either platform, [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) puts the previous value back.

[Subject index](INDEX.md) · [Previous](instantiation-checks-and-integer-digit-limit-helpers.md) · [Continue](test-signal-state-preservation.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

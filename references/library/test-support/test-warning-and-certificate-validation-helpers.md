# test.support`test.support` - Utilities for the Python test suite

test.support.print_warning(*msg*)

Emit a warning to [`sys.__stderr__`](https://docs.python.org/3.14/library/sys.html#sys.__stderr__). Shape the message as: `f"Warning -- {msg}"`. When *msg* spans several lines, prepend the `"Warning -- "` prefix to every line.

Added in version 3.9.

 test.support.wait_process(*pid*, ***, *exitcode*, *timeout=None*)

Block until process *pid* finishes, then verify that its exit code equals *exitcode*.

Raise an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) when the process exit code differs from *exitcode*.

Should the process keep running past *timeout* seconds (`SHORT_TIMEOUT` by default), terminate it and raise an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError). This timeout capability is unavailable on Windows.

Added in version 3.9.

 test.support.calcobjsize(*fmt*)

Return the size of the [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) whose structure members *fmt* defines. The value returned counts the Python object header's size together with alignment.

 test.support.calcvobjsize(*fmt*)

Return the size of the [`PyVarObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) whose structure members *fmt* defines. The value returned counts the Python object header's size together with alignment.

 test.support.checksizeof(*test*, *o*, *size*)

For testcase *test*, assert that the `sys.getsizeof` of *o* added to the GC header size comes to *size*.

 @test.support.anticipate_failure(*condition*)

A decorator that conditionally tags tests with [`unittest.expectedFailure()`](https://docs.python.org/3.14/library/unittest.html#unittest.expectedFailure). Each application of this decorator ought to carry an accompanying comment naming the relevant tracker issue.

 test.support.system_must_validate_cert(*f*)

A decorator that skips the decorated test on TLS certification validation failures.

 @test.support.run_with_locale(*catstr*, **locales*)

A decorator that runs a function under a different locale, then restores it properly once the function returns. *catstr* names the locale category as a string (for instance `"LC_ALL"`). The supplied *locales* are attempted one after another, and the first one that is valid gets used.

 @test.support.run_with_tz(*tz*)

A decorator that runs a function under a particular timezone, then restores it properly once the function returns.

 @test.support.requires_freebsd_version(**min_version*)

Decorator for the minimum version when running test on FreeBSD. Where the FreeBSD version falls below the minimum, the test gets skipped.

 @test.support.requires_linux_version(**min_version*)

Decorator for the minimum version when running test on Linux. Where the Linux version falls below the minimum, the test gets skipped.

 @test.support.requires_mac_version(**min_version*)

Decorator for the minimum version when running test on macOS. Where the macOS version falls below the minimum, the test gets skipped.

 @test.support.requires_gil_enabled

Decorator that skips tests on the free-threaded build. Where the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) is turned off, the test gets skipped.

 @test.support.requires_IEEE_754

Decorator for skipping tests on non-IEEE 754 platforms.

 @test.support.requires_zlib

Decorator that skips tests when [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) is absent.

 @test.support.requires_gzip

Decorator that skips tests when [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) is absent.

 @test.support.requires_bz2

Decorator that skips tests when [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) is absent.

[Subject index](INDEX.md) · [Previous](test-support-captured-stdin-to-test-support-flush-std-streams.md) · [Continue](test-support-utilities-for-the-python-test-suite.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

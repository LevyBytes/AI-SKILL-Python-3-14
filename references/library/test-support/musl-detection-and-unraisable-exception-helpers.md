# test.support — `test.support` — Utilities for the Python test suite

A decorator that executes the test only when the [Limited C API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) can be used.

 @test.support.cpython_only

A decorator restricting a test so that it applies to CPython alone.

 @test.support.impl_detail(*msg=None*, ***guards*)

A decorator that calls `check_impl_detail()` with *guards*. When that call yields `False`, the *msg* text becomes the explanation given for skipping the test.

 @test.support.thread_unsafe(*reason=None*)

A decorator that flags a test as thread-unsafe. Such a test is confined to a single thread, even under `--parallel-threads`.

 @test.support.no_tracing

A decorator that disables tracing briefly while the test executes.

 @test.support.refcount_test

A decorator meant for tests that exercise reference counting. When the test is not executed under CPython, the decorator skips it. Throughout the test, any trace function is cleared so that the trace function does not produce surprising refcounts.

 @test.support.bigmemtest(*size*, *memuse*, *dry_run=True*)

A decorator intended for bigmem tests.

*size* gives the size the test asks for (expressed in arbitrary units that the test itself interprets.) *memuse* is the byte count consumed per unit by the test, or a reasonable estimate thereof. As an illustration, a test requiring a pair of byte buffers at 4 GiB apiece might use `@bigmemtest(size=_4G, memuse=2)`.

Typically the *size* argument arrives at the decorated test method as one more argument. When *dry_run* is `True`, the figure handed to the test method can be smaller than what was asked for. When *dry_run* is `False`, the test cannot perform dummy runs unless `-M` is given.

 @test.support.bigaddrspacetest

A decorator for tests that consume the entire address space.

 test.support.linked_to_musl()

Yields `False` when nothing indicates the interpreter was built against `musl`; otherwise it yields a version triple — `(0, 0, 0)` when the version cannot be determined, or the real version when it is. Meant for use within `skip` decorators. Both `emscripten` and `wasi` are presumed to be built with `musl`; in other cases `platform.libc_ver` is consulted.

 test.support.check_syntax_error(*testcase*, *statement*, *errtext=''*, ***, *lineno=None*, *offset=None*)

Checks for syntax errors in *statement* by trying to compile *statement*. Here *testcase* is the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) instance for the test. *errtext* is the regular expression expected to match the textual form of the raised [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). When *lineno* is not `None`, it is checked against the exception's line. When *offset* is not `None`, it is checked against the exception's offset.

 test.support.open_urlresource(*url*, **args*, ***kw*)

Opens *url*. Should opening fail, it raises `TestFailed`.

 test.support.reap_children()

Call this once any sub-processes have been launched, at the close of `test_main`. Doing so helps guarantee that no leftover children (zombies) linger to consume resources and cause trouble during refleak hunts.

 test.support.get_attribute(*obj*, *name*)

Fetches an attribute, and raises [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) whenever [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) occurs.

 test.support.catch_unraisable_exception()

A context manager that traps an unraisable exception by way of [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook).

Holding onto the exception value (`cm.unraisable.exc_value`) produces a reference cycle. That reference cycle is severed deliberately as the context manager exits.

Holding onto the object (`cm.unraisable.object`) may revive it when it points to an object that is in the middle of finalization. As the context manager exits, it clears that stored object.

Usage:

```python
with support.catch_unraisable_exception() as cm:
    # code creating an "unraisable exception"
    ...

    # check the unraisable exception: use cm.unraisable
    ...

# cm.unraisable attribute no longer exists at this point
# (to break a reference cycle)

```

Added in version 3.8.

[Subject index](INDEX.md) · [Continue](package-test-loading-and-process-skip-helpers.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md) · [Owning module, declaration or section: @test.support.requires_limited_api](test-support-utilities-for-the-python-test-suite.md) · [Preceding source contract and version conditions](test-support-utilities-for-the-python-test-suite.md)

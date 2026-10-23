# test.support.threading_helper`test.support.threading_helper` - Utilities for threading tests

### `test.support.threading_helper` - Utilities for threading tests

The `test.support.threading_helper` module offers support for threading tests.

Added in version 3.10.

 test.support.threading_helper.join_thread(*thread*, *timeout=None*)

Joins a *thread* inside *timeout*. Raises an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) when the thread remains alive past *timeout* seconds.

 @test.support.threading_helper.reap_threads

A decorator that makes sure threads are tidied up even when the test fails.

 test.support.threading_helper.start_threads(*threads*, *unlock=None*)

A context manager that starts *threads*, a sequence of threads. *unlock* is a function invoked once the threads have started, even where an exception was raised; one example would be [`threading.Event.set()`](https://docs.python.org/3.14/library/threading.html#threading.Event.set). On exit, `start_threads` will try to join the threads it started.

 test.support.threading_helper.threading_cleanup(**original_values*)

Tidies up threads absent from *original_values*. Built to issue a warning whenever a test leaves threads still running in the background.

 test.support.threading_helper.threading_setup()

Returns the present thread count along with a copy of the dangling threads.

 test.support.threading_helper.wait_threads_exit(*timeout=None*)

A context manager that holds until every thread created within the `with` statement has exited.

 test.support.threading_helper.catch_threading_exception()

A context manager that traps a [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) exception by way of [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook).

Attributes assigned when an exception is trapped:

- `exc_type`

- `exc_value`

- `exc_traceback`

- `thread`

Consult the [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) documentation.

These attributes get removed when the context manager exits.

Usage:

```python
with threading_helper.catch_threading_exception() as cm:
    # code spawning a thread which raises an exception
    ...

    # check the thread exception, use cm attributes:
    # exc_type, exc_value, exc_traceback, thread
    ...

# exc_type, exc_value, exc_traceback, thread attributes of cm no longer
# exists at this point
# (to avoid reference cycles)

```

Added in version 3.8.

 test.support.threading_helper.run_concurrently(*worker_func*, *nthreads*, *args=()*, *kwargs={}*)

Runs the worker function side by side across several threads. Should any thread raise an exception, it is re-raised once every thread has finished.

[Subject index](INDEX.md) · [Previous](../test-support-bytecode-helper/bytecode-disassembly-and-instruction-assertions.md) · [Continue](../test-support-os-helper/filesystem-encoding-test-names.md)

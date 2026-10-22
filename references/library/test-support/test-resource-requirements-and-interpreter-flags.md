# test.support — `test.support` — Utilities for the Python test suite

test.support.requires(*resource*, *msg=None*)

Raise `ResourceDenied` when *resource* cannot be reached. *msg* becomes the argument passed to `ResourceDenied` should it be raised. Always returns `True` when invoked from a function whose `__name__` equals `'__main__'`. Used when `test.regrtest` runs the tests.

 test.support.sortdict(*dict*)

Return a repr of *dict* with keys sorted.

 test.support.findfile(*filename*, *subdir=None*)

Return the path leading to the file called *filename*. When nothing matches, *filename* itself is returned. That is not necessarily a failure, since it might already be the file's path.

Supplying *subdir* gives a relative path to search through to locate the file, rather than looking straight in the path directories.

 test.support.get_pagesize()

Get size of a page in bytes.

Added in version 3.12.

 test.support.setswitchinterval(*interval*)

Set [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval) to the supplied *interval*. Establishes a floor on the interval for Android systems, keeping the system from hanging.

 test.support.check_impl_detail(***guards*)

Apply this check to fence off CPython's implementation-specific tests, or to limit them to only the implementations the arguments fence in. The function returns `True` or `False` according to the host platform. Example usage:

```python
check_impl_detail()               # Only on CPython (default).
check_impl_detail(jython=True)    # Only on Jython.
check_impl_detail(cpython=False)  # Everywhere except CPython.

```

 test.support.set_memlimit(*limit*)

Set the values for `max_memuse` and `real_max_memuse` for big memory tests.

 test.support.record_original_stdout(*stdout*)

Save the *stdout* value. It is intended to retain the stdout as it stood when regrtest started.

 test.support.get_original_stdout()

Return the original stdout that `record_original_stdout()` recorded, or `sys.stdout` when none was recorded.

 test.support.args_from_interpreter_flags()

Return a list of command line arguments that recreate the present settings held in `sys.flags` and `sys.warnoptions`.

 test.support.optim_args_from_interpreter_flags()

Return a list of command line arguments that recreate the present optimization settings held in `sys.flags`.

[Subject index](INDEX.md) · [Previous](test-support-never-eq-to-test-support-with-pymalloc.md) · [Continue](test-support-captured-stdin-to-test-support-flush-std-streams.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

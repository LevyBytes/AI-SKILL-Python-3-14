# test.support`test.support` - Utilities for the Python test suite

test.support.NEVER_EQ

Object that equals nothing at all (not even `ALWAYS_EQ`). Used to test mixed type comparison.

 test.support.LARGEST

Object that exceeds everything (apart from itself). Used to test mixed type comparison.

 test.support.SMALLEST

Object that falls below everything (apart from itself). Used to test mixed type comparison.

The `test.support` module declares the functions below:

 test.support.busy_retry(*timeout*, *err_msg=None*, */*, ***, *error=True*)

Keep running the loop body until a `break` ends the loop.

Once *timeout* seconds elapse, raise an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) when *error* is true, or simply end the loop when *error* is false.

Example:

```python
for _ in support.busy_retry(support.SHORT_TIMEOUT):
    if check():
        break

```

Example of error=False usage:

```python
for _ in support.busy_retry(support.SHORT_TIMEOUT, error=False):
    if check():
        break
else:
    raise RuntimeError('my custom error')

```

 test.support.sleeping_retry(*timeout*, *err_msg=None*, */*, ***, *init_delay=0.010*, *max_delay=1.0*, *error=True*)

Wait strategy that applies exponential backoff.

Keep running the loop body until a `break` ends the loop. Sleep on every loop iteration except the first. Each iteration doubles the sleep delay (capped at *max_delay* seconds).

Consult the `busy_retry()` documentation for how the parameters are used.

Example raising an exception after SHORT_TIMEOUT seconds:

```python
for _ in support.sleeping_retry(support.SHORT_TIMEOUT):
    if check():
        break

```

Example of error=False usage:

```python
for _ in support.sleeping_retry(support.SHORT_TIMEOUT, error=False):
    if check():
        break
else:
    raise RuntimeError('my custom error')

```

 test.support.is_resource_enabled(*resource*)

Return `True` when *resource* is enabled and reachable. The roster of reachable resources is populated only while `test.regrtest` is running the tests.

 test.support.get_resource_value(*resource*)

Return the value given for *resource* (as `-u *resource*=*value*`). Return `None` when *resource* is disabled or carries no specified value.

 test.support.python_is_optimized()

Return `True` when Python was compiled without `-O0` or `-Og`.

 test.support.with_pymalloc()

Return `_testcapi.WITH_PYMALLOC`.

[Subject index](INDEX.md) · [Previous](test-support-short-timeout-to-test-support-always-eq.md) · [Continue](test-resource-requirements-and-interpreter-flags.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

# test.support`test.support` - Utilities for the Python test suite

test.support.captured_stdin()

 test.support.captured_stdout()

 test.support.captured_stderr()

A context managers that temporarily replaces the named stream with [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) object.

Example use with output streams:

```python
with captured_stdout() as stdout, captured_stderr() as stderr:
    print("hello")
    print("error", file=sys.stderr)
assert stdout.getvalue() == "hello\n"
assert stderr.getvalue() == "error\n"

```

Example use with input stream:

```python
with captured_stdin() as stdin:
    stdin.write('hello\n')
    stdin.seek(0)
    # call test code that consumes from sys.stdin
    captured = input()
self.assertEqual(captured, "hello")

```

 test.support.disable_faulthandler()

A context manager that temporary disables [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler).

 test.support.gc_collect()

Push the collector to reclaim as many objects as it can. This matters because the garbage collector makes no promise of prompt deallocation. As a result, `__del__` methods can fire later than you would expect, and weakrefs can stay alive longer than you would expect.

 test.support.disable_gc()

A context manager that turns off the garbage collector when entered. When it exits, the garbage collector returns to whatever state it held before.

 test.support.swap_attr(*obj*, *attr*, *new_val*)

Context manager to swap out an attribute with a new object.

Usage:

```python
with swap_attr(obj, "attr", 5):
    ...

```

For the span of the `with` block this assigns `obj.attr` the value 5, then puts the former value back once the block ends. Should `attr` be missing from `obj`, it gets created and then removed when the block finishes.

The former value (or `None` when there was none) is bound to whatever the “as” clause targets, when one is present.

 test.support.swap_item(*obj*, *attr*, *new_val*)

Context manager to swap out an item with a new object.

Usage:

```python
with swap_item(obj, "item", 5):
    ...

```

For the span of the `with` block this assigns `obj["item"]` the value 5, then puts the former value back once the block ends. Should `item` be missing from `obj`, it gets created and then removed when the block finishes.

The former value (or `None` when there was none) is bound to whatever the “as” clause targets, when one is present.

 test.support.flush_std_streams()

Invoke the `flush()` method on [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) first and then on [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). It serves to keep the ordering of the logs consistent ahead of writing into stderr.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](test-resource-requirements-and-interpreter-flags.md) · [Continue](test-warning-and-certificate-validation-helpers.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)

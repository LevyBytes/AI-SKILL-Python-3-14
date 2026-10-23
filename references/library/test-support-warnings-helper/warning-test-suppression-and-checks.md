# test.support.warnings_helper: `test.support.warnings_helper.ignore_warnings()`, `test.support.warnings_helper.check_no_resource_warning()`, `test.support.warnings_helper.check_syntax_warning()`, `test.support.warnings_helper.check_warnings()`

### `test.support.warnings_helper` - Utilities for warnings tests

Support aimed at warnings tests is delivered by the `test.support.warnings_helper` module.

Added in version 3.10.

 test.support.warnings_helper.ignore_warnings(***, *category*)

Mute warnings that are instances of *category*, where *category* has to be [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) or one of its subclasses. This is broadly the same as pairing [`warnings.catch_warnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) with [`warnings.simplefilter('ignore', category=category)`](https://docs.python.org/3.14/library/warnings.html#warnings.simplefilter). For example:

```python
@warning_helper.ignore_warnings(category=DeprecationWarning)
def test_suppress_warning():
    # do something

```

Added in version 3.8.

 test.support.warnings_helper.check_no_resource_warning(*testcase*)

A context manager that verifies no [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) was produced. Be sure to dispose of whatever object might emit `ResourceWarning` ahead of the context manager closing.

 test.support.warnings_helper.check_syntax_warning(*testcase*, *statement*, *errtext=''*, ***, *lineno=1*, *offset=None*)

Check for a syntax warning in *statement* by trying to compile *statement*. It additionally checks that the [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) surfaces just a single time and that, once promoted to an error, it becomes a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). *testcase* is the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) instance driving the test. *errtext* is the regular expression expected to match the string form of both the emitted `SyntaxWarning` and the raised `SyntaxError`. When *lineno* is not `None`, it is compared against the line of the warning and the exception. When *offset* is not `None`, it is compared against the exception's offset.

Added in version 3.8.

 test.support.warnings_helper.check_warnings(**filters*, *quiet=True*)

A handy wrapper around [`warnings.catch_warnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) that smooths the job of testing whether a warning was raised as intended. It comes close to invoking `warnings.catch_warnings(record=True)` together with [`warnings.simplefilter()`](https://docs.python.org/3.14/library/warnings.html#warnings.simplefilter) tuned to `always`, plus the ability to automatically vet whatever results get recorded.

As positional arguments, `check_warnings` takes 2-tuples shaped like `("message regexp", WarningCategory)`. Whenever one or more *filters* are supplied, or whenever the optional keyword argument *quiet* is `False`, it confirms the warnings line up with expectations: every named filter has to match at least one warning thrown by the wrapped code or the test fails, and the test also fails if any warning surfaces that matches none of the named filters. Set *quiet* to `True` to switch off the first of those checks.

Given no arguments at all, its fallback behavior is:

```python
check_warnings(("", Warning), quiet=True)

```

Here every warning gets captured while nothing is raised as an error.

Stepping into the context manager yields a `WarningRecorder` instance. You can reach the warnings list that backs [`catch_warnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) through the recorder object's [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) attribute. For convenience, the attributes belonging to the object for the latest warning are likewise reachable straight off the recorder object (see the example further down). Where nothing has been raised, every attribute you would normally find on a warning-representing object instead comes back as `None`.

The recorder object additionally carries a `reset()` method that empties the warnings list.

Here is the intended pattern for using the context manager:

```python
with check_warnings(("assertion is always true", SyntaxWarning),
                    ("", UserWarning)):
    exec('assert(False, "Hey!")')
    warnings.warn(UserWarning("Hide me!"))

```

Here, should either warning fail to fire or some unexpected warning fire instead, `check_warnings()` would raise an error.

When a test has to inspect the warnings more closely, going beyond merely confirming that they happened, a snippet along these lines works:

```python
with check_warnings(quiet=True) as w:
    warnings.warn("foo")
    assert str(w.args[0]) == "foo"
    warnings.warn("bar")
    assert str(w.args[0]) == "bar"
    assert str(w.warnings[0].args[0]) == "foo"
    assert str(w.warnings[1].args[0]) == "bar"
    w.reset()
    assert len(w.warnings) == 0

```

In this scenario all warnings are intercepted, and the test code examines those captured warnings firsthand.

Changed in version 3.2: New optional arguments *filters* and *quiet*.

[Subject index](INDEX.md) · [Previous](../test-support-import-helper/test-support-import-helper-dirsonsyspath-class.md) · [Continue](test-support-warnings-helper-warningsrecorder-class.md)

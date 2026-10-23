# warnings - Testing Warnings

### Testing Warnings

When you want to test the warnings that code raises, reach for the `catch_warnings` context manager. It lets you temporarily adjust the warnings filter to suit your test. As an example, the following captures every warning that is raised so you can inspect them:

```python
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings(record=True) as w:
    # Cause all warnings to always be triggered.
    warnings.simplefilter("always")
    # Trigger a warning.
    fxn()
    # Verify some things
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert "deprecated" in str(w[-1].message)

```

You can also turn every warning into an exception by writing `error` in place of `always`. Keep one thing in mind: once a warning has already been raised under a `once`/`default` rule, then regardless of which filters you set, that warning won't surface a second time unless the warnings registry tied to it has been cleared.

When the context manager exits, the warnings filter goes back to whatever state it held on entry. That keeps tests from altering the warnings filter in surprising ways from one test to the next and producing nondeterministic test outcomes.

>

Note

For how the `catch_warnings` context manager behaves with respect to concurrency-safety inside programs that rely on several threads or on async functions, consult Concurrent safety of Context Managers.

If you are exercising several operations that all raise the same kind of warning, take care to test them in a way that proves each operation really does raise a fresh warning (for example, set warnings to be raised as exceptions and verify the operations raise exceptions, confirm the warning list keeps growing after each operation, or delete the earlier entries from the warnings list before each new operation).

[Subject index](INDEX.md) · [Previous](temporarily-suppressing-warnings.md) · [Continue](updating-code-for-new-versions-of-dependencies.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)

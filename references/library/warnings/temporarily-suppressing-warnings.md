# warnings — Temporarily Suppressing Warnings

### Temporarily Suppressing Warnings

Suppose you are calling code you already know triggers a warning — say, a deprecated function — but you would rather not see the warning (even when warnings were explicitly turned on from the command line). The warning can then be muted with the `catch_warnings` context manager:

```python
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

```

Every warning is simply discarded for as long as you stay inside the context manager. That lets you run code you know to be deprecated without seeing the warning, all the while leaving the warning intact for other code that might not realize it is relying on deprecated code.

>

Note

For how the `catch_warnings` context manager behaves with respect to concurrency-safety inside programs that rely on several threads or on async functions, consult Concurrent safety of Context Managers.

[Subject index](INDEX.md) · [Previous](overriding-the-default-filter.md) · [Continue](testing-warnings.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)

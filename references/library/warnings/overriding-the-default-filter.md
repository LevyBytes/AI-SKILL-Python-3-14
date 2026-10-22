# warnings — Overriding the default filter

### Overriding the default filter

Anyone building an application in Python might prefer to keep *all* Python-level warnings out of sight for their users by default, surfacing them only while running tests or otherwise working on the application. The [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) attribute, which carries filter configurations to the interpreter, doubles as a flag for whether warnings ought to be turned off:

```python
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

```

For anyone writing test runners that exercise Python code, the recommendation instead is to make certain *all* warnings show up by default for the code under test, with something like:

```python
import sys

if not sys.warnoptions:
    import os, warnings
    warnings.simplefilter("default") # Change the filter in this process
    os.environ["PYTHONWARNINGS"] = "default" # Also affect subprocesses

```

Lastly, anyone writing interactive shells that execute user code under a namespace that isn't `__main__` is encouraged to make sure [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) messages stay visible by default, with code along these lines (where `user_ns` is the module that runs the code entered interactively):

```python
import warnings
warnings.filterwarnings("default", category=DeprecationWarning,
                                   module=user_ns.get("__name__"))

```

[Subject index](INDEX.md) · [Previous](default-warning-filter.md) · [Continue](temporarily-suppressing-warnings.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)

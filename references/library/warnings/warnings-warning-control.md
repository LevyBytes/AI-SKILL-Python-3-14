# warnings`warnings` - Warning control

### `warnings` - Warning control

**Source code:** [Lib/warnings.py](https://github.com/python/cpython/tree/3.14/Lib/warnings.py)

---

A warning message is the usual way to flag some condition in a program to the user when that condition (ordinarily) is not severe enough to justify raising an exception and stopping the program outright. A typical case is signalling that the program relies on a module that is now obsolete.

In Python source, a warning is raised by invoking the `warn()` function provided here. (From C, the equivalent is [`PyErr_WarnEx()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WarnEx); refer to [Exception Handling](https://docs.python.org/3.14/c-api/exceptions.html#exceptionhandling) for the specifics).

By default these messages go to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr), yet how they are treated is highly configurable — ranging from suppressing every warning to promoting them into exceptions. That treatment may depend on the warning category, on the wording of the message itself, and on where in the source the warning originates. As a rule, repeated instances of the same warning from the same source location are not shown again.

Controlling warnings happens across two stages: first, whenever a warning is raised, the system decides whether the message should actually be emitted; second, when a message is to be emitted, it is formatted and printed by way of a hook the user can configure.

Deciding whether a given warning message gets emitted falls to the warning filter — an ordered series of matching rules paired with actions. You add rules to that filter with `filterwarnings()`, and you return it to its initial state with `resetwarnings()`.

Emitting the warning text is the job of `showwarning()`, which can be replaced; by default that function builds the message through `formatwarning()`, a routine that custom replacements may likewise call.

See also

[`logging.captureWarnings()`](https://docs.python.org/3.14/library/logging.html#logging.captureWarnings) lets you route every warning through the standard logging infrastructure.

[Subject index](INDEX.md) · [Continue](warning-categories.md)

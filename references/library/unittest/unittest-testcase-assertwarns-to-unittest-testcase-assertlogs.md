# unittest: `assertWarns()`, `assertWarnsRegex()`, `assertLogs()`

assertWarns(*warning*, *callable*, **args*, ***kwds*)

 assertWarns(*warning*, ***, *msg=None*)

Verify that calling *callable* with whatever positional or keyword arguments you additionally feed to `assertWarns()` triggers a warning. The test succeeds when *warning* fires and fails when it does not. Any exception counts as an error. You can trap any one of several warnings by supplying a tuple of warning classes for *warnings*.

When you provide nothing beyond *warning* and perhaps *msg*, a context manager is returned, letting the code under test sit inline instead of inside a function:

```python
with self.assertWarns(SomeWarning):
    do_something()

```

In its context-manager role, `assertWarns()` will also take the extra keyword argument *msg*.

The context manager keeps the trapped warning object in its `warning` attribute, along with the source line that set off the warnings in the `filename` and `lineno` attributes. That comes in handy when you want to run further checks against the trapped warning:

```python
with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)
self.assertEqual(320, cm.lineno)

```

This method behaves the same no matter which warning filters happen to be active at call time.

Added in version 3.2.

Changed in version 3.3: the *msg* keyword argument was added for the context-manager usage.

 assertWarnsRegex(*warning*, *regex*, *callable*, **args*, ***kwds*)

 assertWarnsRegex(*warning*, *regex*, ***, *msg=None*)

Behaves like `assertWarns()` while additionally confirming that *regex* matches against the message of the warning that fired. *regex* can be a compiled regular expression object or a string holding a regular expression fit for use with [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search). Example:

```python
self.assertWarnsRegex(DeprecationWarning,
                      r'legacy_function\(\) is deprecated',
                      legacy_function, 'XYZ')

```

or:

```python
with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
    frobnicate('/etc/passwd')

```

Added in version 3.2.

Changed in version 3.3: a *msg* keyword argument was added for use in context-manager form.

 assertLogs(*logger=None*, *level=None*)

A context manager that confirms a minimum of one message is logged on the *logger* (or one of its descendants), at no less than the supplied *level*.

When supplied, *logger* ought to be a [`logging.Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) object or a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) naming a logger. By default it is the root logger, which catches every message that a non-propagating descendent logger did not block.

When supplied, *level* ought to be either a numeric logging level or the equivalent string (for example either `"ERROR"` or [`logging.ERROR`](https://docs.python.org/3.14/library/logging.html#logging.ERROR)). By default it is [`logging.INFO`](https://docs.python.org/3.14/library/logging.html#logging.INFO).

The test succeeds when no fewer than one message produced inside the `with` block satisfies the *logger* and *level* criteria; otherwise it fails.

What the context manager hands back is a recording helper that tracks the log messages that matched. It carries two attributes:

 records

A list of [`logging.LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) objects of the matching log messages.

[Subject index](INDEX.md) · [Previous](subclass-and-exception-assertions.md) · [Continue](log-absence-and-ordering-assertions.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)

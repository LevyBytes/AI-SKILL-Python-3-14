# unittest: `assertIsSubclass()`, `assertNotIsSubclass()`, `assertRaises()`, `assertRaisesRegex()`

assertIsSubclass(*cls*, *superclass*, *msg=None*)

 assertNotIsSubclass(*cls*, *superclass*, *msg=None*)

Verify that *cls* is (or is not) a subclass of *superclass* (where *superclass* may be a single class or a tuple of classes, just as [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) permits). For a precise type match, reach for `assertIs(cls, superclass)`.

Added in version 3.14.

You may also confirm that exceptions, warnings, and log messages get produced, by means of these methods:

| Method | Checks that | New in |
| --- | --- | --- |
| `assertRaises(exc, fun, *args, **kwds)` | `fun(*args, **kwds)` raises *exc* |  |
| `assertRaisesRegex(exc, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises *exc* and the message matches regex *r* | 3.1 |
| `assertWarns(warn, fun, *args, **kwds)` | `fun(*args, **kwds)` raises *warn* | 3.2 |
| `assertWarnsRegex(warn, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises *warn* and the message matches regex *r* | 3.2 |
| `assertLogs(logger, level)` | The `with` block logs on *logger* with minimum *level* | 3.4 |
| `assertNoLogs(logger, level)` | The `with` block does not log on*logger* with minimum *level* | 3.10 |

 assertRaises(*exception*, *callable*, **args*, ***kwds*)

 assertRaises(*exception*, ***, *msg=None*)

Verify that calling *callable* with whatever positional or keyword arguments you additionally feed to `assertRaises()` raises an exception. The test succeeds when *exception* is raised, becomes an error if a different exception surfaces, and fails when nothing is raised at all. You can trap any one of several exceptions by supplying a tuple of exception classes for *exception*.

When you provide nothing beyond *exception* and perhaps *msg*, a context manager is returned, letting the code under test sit inline instead of inside a function:

```python
with self.assertRaises(SomeException):
    do_something()

```

In its context-manager role, `assertRaises()` will also take the extra keyword argument *msg*.

The context manager keeps the trapped exception object in its `exception` attribute. That comes in handy when you want to run further checks against the raised exception:

```python
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)

```

Changed in version 3.1: the option to employ `assertRaises()` in context-manager form was introduced.

Changed in version 3.2: Added the `exception` attribute.

Changed in version 3.3: in context-manager form, the *msg* keyword argument was introduced.

 assertRaisesRegex(*exception*, *regex*, *callable*, **args*, ***kwds*)

 assertRaisesRegex(*exception*, *regex*, ***, *msg=None*)

Behaves like `assertRaises()` while additionally confirming that *regex* matches against the string form of the exception that was raised. *regex* can be a compiled regular expression object or a string holding a regular expression fit for use with [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search). Examples:

```python
self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
                       int, 'XYZ')

```

or:

```python
with self.assertRaisesRegex(ValueError, 'literal'):
   int('XYZ')

```

Added in version 3.1: Added under the name `assertRaisesRegexp`.

Changed in version 3.2: Renamed to `assertRaisesRegex()`.

Changed in version 3.3: when used as a context manager, the *msg* keyword argument was added.

[Subject index](INDEX.md) · [Previous](test-debugging-equality-and-instance-assertions.md) · [Continue](unittest-testcase-assertwarns-to-unittest-testcase-assertlogs.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)

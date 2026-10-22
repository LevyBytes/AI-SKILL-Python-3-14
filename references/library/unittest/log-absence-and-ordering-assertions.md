# unittest: `assertNoLogs()`, `assertAlmostEqual()`, `assertNotAlmostEqual()`, `assertGreater()`, `assertGreaterEqual()`, `assertLess()`, `assertLessEqual()`

output

A list of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects with the formatted output of matching messages.

Example:

```python
with self.assertLogs('foo', level='INFO') as cm:
    logging.getLogger('foo').info('first message')
    logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])

```

Added in version 3.4.

 assertNoLogs(*logger=None*, *level=None*)

A context manager that confirms zero messages are logged on the *logger* (or one of its descendants), at no less than the supplied *level*.

When supplied, *logger* ought to be a [`logging.Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) object or a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) naming a logger. By default it is the root logger, which catches every message.

When supplied, *level* ought to be either a numeric logging level or the equivalent string (for example either `"ERROR"` or [`logging.ERROR`](https://docs.python.org/3.14/library/logging.html#logging.ERROR)). By default it is [`logging.INFO`](https://docs.python.org/3.14/library/logging.html#logging.INFO).

In contrast to `assertLogs()`, the context manager hands back nothing.

Added in version 3.10.

Several further methods exist for carrying out checks of a more specific nature, for instance:

| Method | Checks that | New in |
| --- | --- | --- |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |  |
| `assertNotAlmostEqual(a, b)` | `round(a-b, 7) != 0` |  |
| `assertGreater(a, b)` | `a > b` | 3.1 |
| `assertGreaterEqual(a, b)` | `a >= b` | 3.1 |
| `assertLess(a, b)` | `a < b` | 3.1 |
| `assertLessEqual(a, b)` | `a <= b` | 3.1 |
| `assertRegex(s, r)` | `r.search(s)` | 3.1 |
| `assertNotRegex(s, r)` | `not r.search(s)` | 3.2 |
| `assertCountEqual(a, b)` | *a* contains the same elements as *b*, regardless of their order. | 3.2 |
| `assertStartsWith(a, b)` | `a.startswith(b)` | 3.14 |
| `assertNotStartsWith(a, b)` | `not a.startswith(b)` | 3.14 |
| `assertEndsWith(a, b)` | `a.endswith(b)` | 3.14 |
| `assertNotEndsWith(a, b)` | `not a.endswith(b)` | 3.14 |
| `assertHasAttr(a, b)` | `hasattr(a, b)` | 3.14 |
| `assertNotHasAttr(a, b)` | `not hasattr(a, b)` | 3.14 |

 assertAlmostEqual(*first*, *second*, *places=7*, *msg=None*, *delta=None*)

 assertNotAlmostEqual(*first*, *second*, *places=7*, *msg=None*, *delta=None*)

Verify that *first* and *second* are roughly (or not roughly) equal: subtract one from the other, round the difference to the stated count of decimal *places* (7 by default), then check it against zero. Be aware these methods round the values to the stated count of *decimal places* (that is, in the manner of the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function) and not to *significant digits*.

Should you pass *delta* in place of *places*, the gap between *first* and *second* has to be no greater than (or greater than) *delta*.

Passing *delta* together with *places* raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.2: objects that compare equal are now treated by `assertAlmostEqual()` as almost equal on their own. Likewise, `assertNotAlmostEqual()` now fails by itself whenever the objects compare equal. The *delta* keyword argument was also added.

 assertGreater(*first*, *second*, *msg=None*)

 assertGreaterEqual(*first*, *second*, *msg=None*)

 assertLess(*first*, *second*, *msg=None*)

 assertLessEqual(*first*, *second*, *msg=None*)

Verify that *first* stands respectively >, >=, < or <= relative to *second*, according to whichever method you named. Otherwise, the test fails:

```python
>>> self.assertGreaterEqual(3, 4)
AssertionError: "3" unexpectedly not greater than or equal to "4"

```

Added in version 3.1.

[Subject index](INDEX.md) · [Previous](unittest-testcase-assertwarns-to-unittest-testcase-assertlogs.md) · [Continue](regex-and-sequence-assertions.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)

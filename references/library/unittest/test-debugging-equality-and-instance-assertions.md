# unittest: `debug()`, `assertEqual()`, `assertNotEqual()`, `assertTrue()`, `assertFalse()`, `assertIs()`, `assertIsNot()`, `assertIsNone()`, `assertIsNotNone()`, `assertIn()`, `assertNotIn()`, `assertIsInstance()`, `assertNotIsInstance()`

debug()

Execute the test without gathering the result. Doing so lets exceptions thrown by the test bubble up to the caller, which is handy for running tests beneath a debugger.

To detect and report failures, the `TestCase` class offers a number of assert methods. The table that follows enumerates the methods used most often (additional assert methods appear in the tables further down):

| Method | Checks that | New in |
| --- | --- | --- |
| `assertEqual(a, b)` | `a == b` |  |
| `assertNotEqual(a, b)` | `a != b` |  |
| `assertTrue(x)` | `bool(x) is True` |  |
| `assertFalse(x)` | `bool(x) is False` |  |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |
| `assertIsSubclass(a, b)` | `issubclass(a, b)` | 3.14 |
| `assertNotIsSubclass(a, b)` | `not issubclass(a, b)` | 3.14 |

Every assert method takes a *msg* argument; when provided, it becomes the failure error message (refer also to `longMessage`). Be aware that you may hand the *msg* keyword argument to `assertRaises()`, `assertRaisesRegex()`, `assertWarns()`, `assertWarnsRegex()` solely in their context-manager form.

 assertEqual(*first*, *second*, *msg=None*)

Verify that *first* and *second* are equal. Should the two values not compare as equal, the test fails.

Beyond that, when *first* and *second* share the exact same type and that type is one of list, tuple, dict, set, frozenset or str — or any type a subclass has registered through `addTypeEqualityFunc()` — the type-specific equality function runs to produce a more helpful default error message (refer also to the roster of type-specific methods).

Changed in version 3.1: the type-specific equality function now gets invoked automatically.

Changed in version 3.2: when strings are compared, `assertMultiLineEqual()` became the type equality function used by default.

 assertNotEqual(*first*, *second*, *msg=None*)

Verify that *first* and *second* are not equal. Should the two values compare as equal, the test fails.

 assertTrue(*expr*, *msg=None*)

 assertFalse(*expr*, *msg=None*)

Verify that *expr* is true (or false).

Keep in mind this amounts to `bool(expr) is True` rather than `expr is True` (for the latter, reach for `assertIs(expr, True)`). You should likewise steer clear of this method whenever a more specific one exists (for instance `assertEqual(a, b)` rather than `assertTrue(a == b)`), since the specific ones yield a clearer error message on failure.

 assertIs(*first*, *second*, *msg=None*)

 assertIsNot(*first*, *second*, *msg=None*)

Verify that *first* and *second* are (or are not) the very same object.

Added in version 3.1.

 assertIsNone(*expr*, *msg=None*)

 assertIsNotNone(*expr*, *msg=None*)

Verify that *expr* is (or is not) `None`.

Added in version 3.1.

 assertIn(*member*, *container*, *msg=None*)

 assertNotIn(*member*, *container*, *msg=None*)

Verify that *member* is (or is not) inside *container*.

Added in version 3.1.

 assertIsInstance(*obj*, *cls*, *msg=None*)

 assertNotIsInstance(*obj*, *cls*, *msg=None*)

Verify that *obj* is (or is not) an instance of *cls* (where *cls* may be a single class or a tuple of classes, just as [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) permits). For a precise type match, reach for `assertIs(type(obj), cls)`.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](unittest-testcase-setup-to-unittest-testcase-subtest.md) · [Continue](subclass-and-exception-assertions.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)

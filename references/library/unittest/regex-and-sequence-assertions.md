# unittest: Regex, prefix, attribute and sequence assertions

assertRegex(*text*, *regex*, *msg=None*)

 assertNotRegex(*text*, *regex*, *msg=None*)

Verify that a *regex* search does (or does not) match *text*. On failure, the error message carries the pattern alongside the *text* (or the pattern alongside the slice of *text* that matched unexpectedly). *regex* can be a compiled regular expression object or a string holding a regular expression fit for use with [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search).

Added in version 3.1: Added under the name `assertRegexpMatches`.

Changed in version 3.2: The method `assertRegexpMatches()` has been renamed to `assertRegex()`.

Added in version 3.2: `assertNotRegex()`.

 assertCountEqual(*first*, *second*, *msg=None*)

Verify that sequence *first* holds the same elements as *second*, irrespective of ordering. If it does not, an error message enumerating the discrepancies between the sequences gets produced.

Repeated elements are *not* disregarded while *first* and *second* are compared. The check confirms that every element appears the same number of times across both sequences. This is the same as: `assertEqual(Counter(list(first)), Counter(list(second)))` yet it also handles sequences whose objects are unhashable.

Added in version 3.2.

 assertStartsWith(*s*, *prefix*, *msg=None*)

 assertNotStartsWith(*s*, *prefix*, *msg=None*)

Verify that the Unicode or byte string *s* begins (or does not begin) with a *prefix*. *prefix* may additionally be a tuple of strings to attempt.

Added in version 3.14.

 assertEndsWith(*s*, *suffix*, *msg=None*)

 assertNotEndsWith(*s*, *suffix*, *msg=None*)

Verify that the Unicode or byte string *s* concludes (or does not conclude) with a *suffix*. *suffix* may additionally be a tuple of strings to attempt.

Added in version 3.14.

 assertHasAttr(*obj*, *name*, *msg=None*)

 assertNotHasAttr(*obj*, *name*, *msg=None*)

Verify that the object *obj* possesses (or does not possess) an attribute *name*.

Added in version 3.14.

For objects sharing a type, the `assertEqual()` method routes the equality test to distinct type-specific methods. Most built-in types already have these methods implemented, yet you can register fresh ones too via `addTypeEqualityFunc()`:

 addTypeEqualityFunc(*typeobj*, *function*)

Registers a type-specific method, called by `assertEqual()`, to determine whether two objects of precisely the same *typeobj* (subclasses excluded) compare as equal. *function* has to accept two positional arguments plus a third msg=None keyword argument exactly as `assertEqual()` itself does. It has to raise `self.failureException(msg)` once it spots inequality between the first two parameters — ideally supplying useful information and spelling out the inequalities in detail within the error message.

Added in version 3.1.

The roster of type-specific methods that `assertEqual()` employs automatically is collected in the table below. Be aware that calling these methods on your own is generally unnecessary.

| Method | Used to compare | New in |
| --- | --- | --- |
| `assertMultiLineEqual(a, b)` | strings | 3.1 |
| `assertSequenceEqual(a, b)` | sequences | 3.1 |
| `assertListEqual(a, b)` | lists | 3.1 |
| `assertTupleEqual(a, b)` | tuples | 3.1 |
| `assertSetEqual(a, b)` | sets or frozensets | 3.1 |
| `assertDictEqual(a, b)` | dicts | 3.1 |

 assertMultiLineEqual(*first*, *second*, *msg=None*)

Verify that the multiline string *first* equals the string *second*. Where they differ, a diff of the two strings calling out the differences is folded into the error message. By default this method handles string comparisons made through `assertEqual()`.

Added in version 3.1.

 assertSequenceEqual(*first*, *second*, *msg=None*, *seq_type=None*)

Verifies that two sequences match. When a *seq_type* is provided, both *first* and *second* have to be instances of *seq_type*, or else a failure is raised. Where the sequences diverge, an error message is assembled that displays the difference between the two.

`assertEqual()` does not call this method on its own; rather, it underpins `assertListEqual()` and `assertTupleEqual()`.

Added in version 3.1.

[Subject index](INDEX.md) · [Previous](log-absence-and-ordering-assertions.md) · [Continue](unittest-testcase-assertlistequal-to-unittest-testcase-fail.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)

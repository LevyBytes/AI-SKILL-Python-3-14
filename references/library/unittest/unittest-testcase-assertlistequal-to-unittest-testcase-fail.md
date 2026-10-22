# unittest: `assertListEqual()`, `assertTupleEqual()`, `assertSetEqual()`, `assertDictEqual()`, `fail()`

assertListEqual(*first*, *second*, *msg=None*)

 assertTupleEqual(*first*, *second*, *msg=None*)

Verifies that two lists or tuples match. Otherwise, an error message is assembled that displays only the differences between the two. A failure is likewise raised should either parameter be of the wrong type. By default these methods handle list or tuple comparisons made through `assertEqual()`.

Added in version 3.1.

 assertSetEqual(*first*, *second*, *msg=None*)

Verifies that two sets match. Otherwise, an error message is assembled that enumerates the differences between the sets. By default this method handles set or frozenset comparisons made through `assertEqual()`.

Fails if either of *first* or *second* does not have a [`difference()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset.difference) method.

Added in version 3.1.

 assertDictEqual(*first*, *second*, *msg=None*)

Verify that two dictionaries match. Otherwise, an error message is assembled that displays the differences within the dictionaries. By default this method will handle dictionary comparisons in `assertEqual()` calls.

Added in version 3.1.

To close out, the `TestCase` supplies these methods and attributes:

 fail(*msg=None*)

Flags a test failure outright, using *msg* or `None` as the error message.

 failureException

This class attribute names the exception that the test method raises. Should a test framework require a specialized exception — perhaps to convey extra information — it must subclass this exception so as to “play fair” with the framework. This attribute starts out set to [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError).

 longMessage

This class attribute governs the behavior when a custom failure message is supplied as the msg argument to a failing assertXYY call. The default is `True`. Under that setting, the custom message is tacked onto the end of the standard failure message. Set to `False`, the custom message takes the place of the standard message.

You can override the class setting inside individual test methods by setting an instance attribute, self.longMessage, to `True` or `False` ahead of calling the assert methods.

The class setting is reset ahead of each test call.

Added in version 3.1.

 maxDiff

[Subject index](INDEX.md) · [Previous](regex-and-sequence-assertions.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md) · [Required continuation of the source contract](test-case-counting-and-cleanup.md)

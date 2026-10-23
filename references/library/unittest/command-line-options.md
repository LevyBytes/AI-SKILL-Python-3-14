# unittest - Command-line options

### Command-line options

**unittest** supports these command-line options:

 -b, --buffer

While the test run proceeds, the standard output and standard error streams are buffered. Any output a passing test produces is thrown away. On a test failure or error, output is echoed as usual and appended to the failure messages.

 -c, --catch

When Control-C is pressed during the test run, it lets the current test finish and then reports every result gathered to that point. Pressing Control-C a second time raises the usual [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception.

See Signal Handling for the functions that provide this functionality.

 -f, --failfast

Stop the test run on the first error or failure.

 -k

Run only those test methods and classes whose name matches the given pattern or substring. You may give this option more than once, whereupon every test case matching any of the supplied patterns is included.

A pattern containing a wildcard character (`*`) is matched against the test name with [`fnmatch.fnmatchcase()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatchcase); otherwise plain case-sensitive substring matching applies.

Matching of patterns is done against the fully qualified test method name as the test loader imported it.

To illustrate, `-k foo` matches `foo_tests.SomeTest.test_something`, `bar_tests.SomeTest.test_foo`, but not `bar_tests.FooTest.test_something`.

 --locals

Show local variables in tracebacks.

 --durations N

Show the N slowest test cases (N=0 for all).

Added in version 3.2: The command-line options `-b`, `-c` and `-f` were added.

Added in version 3.5: The command-line option `--locals`.

Added in version 3.7: The command-line option `-k`.

Added in version 3.12: The command-line option `--durations`.

You can likewise put the command line to use for test discovery, running every test across a project or merely some portion of them.

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Continue](test-discovery.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)

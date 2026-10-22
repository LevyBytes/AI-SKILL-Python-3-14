# Signal Handling

### Signal Handling

Added in version 3.2.

unittest's `-c/--catch` command-line option, paired with the `catchbreak` parameter on `unittest.main()`, makes control-C behave more gracefully throughout a test run. Once catch-break behavior is switched on, pressing control-C lets the test in progress finish, after which the run stops and prints every result gathered up to that point. Pressing control-c a second time triggers a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) the usual way.

The signal handler that deals with control-c tries to stay compatible with code or tests that set up a [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) handler of their own. Should the `unittest` handler get invoked while *not* being the registered `signal.SIGINT` handler - that is, when the system under test has supplanted it and is delegating to it - it then turns to the default handler. That is generally just what code which replaces a registered handler and delegates onward will expect. To switch off `unittest` control-c handling for particular tests, you can apply the `removeHandler()` decorator.

A handful of utility functions exist so that framework authors can switch on control-c handling inside their own test frameworks.

 unittest.installHandler()

Set up the control-c handler. The moment a [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) arrives (typically because the user hit control-c), `stop()` is invoked on each registered result.

 unittest.registerResult(*result*)

Enroll a `TestResult` object into control-c handling. The act of registering keeps only a weak reference to the result, so it won't stand in the way of that result being garbage collected.

When control-c handling is switched off, enrolling a `TestResult` object does nothing at all - which lets test frameworks register every result they build without first checking whether handling happens to be on.

 unittest.removeResult(*result*)

Drop a result that was previously registered. After removal, a control-c will no longer trigger `stop()` on that particular result object.

 unittest.removeHandler(*function=None*)

Called with no arguments, this function tears down the control-c handler whenever one has been set up. It doubles as a test decorator, too, letting you lift the handler for the span of a single test's execution:

```python
@unittest.removeHandler
def test_signal_handling(self):
    ...

```

[Subject index](INDEX.md) · [Previous](unittest-addmodulecleanup-to-unittest-domodulecleanups.md)

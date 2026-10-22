# logging / Logger Objects: `debug()`, `info()`, `warning()`, `error()`, `critical()`, `log()`, `exception()`

debug(*msg*, **args*, ***kwargs*)

Logs a message at level `DEBUG` on this logger. The *msg* is the message format string, while the *args* are the arguments merged into *msg* by way of the string formatting operator. (Note that this means you can put keywords in the format string, paired with a single dictionary argument.) No % formatting operation runs on *msg* when no *args* are supplied.

Four keyword arguments within *kwargs* get inspected: *exc_info*, *stack_info*, *stacklevel* and *extra*.

Should *exc_info* not evaluate as false, it triggers exception information being added onto the logging message. When an exception tuple (in the form returned by [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info)) or an exception instance is given, it's used; if not, `sys.exc_info()` is called to fetch the exception information.

The second optional keyword argument is *stack_info*, defaulting to `False`. When true, stack information is added onto the logging message, taking in the actual logging call. Note that this isn't the same stack information shown by way of specifying *exc_info*: the former spans the stack frames running from the stack's bottom up through the logging call within the current thread, while the latter concerns stack frames that got unwound, after an exception, during the search for exception handlers.

You can give *stack_info* on its own, separate from *exc_info*, e.g. just to display how you reached a certain point in your code, even when nothing was raised. The stack frames are printed beneath a header line reading:

```none
Stack (most recent call last):

```

This echoes the `Traceback (most recent call last):` shown when exception frames are displayed.

The third optional keyword argument is *stacklevel*, defaulting to `1`. When it exceeds 1, the matching number of stack frames are skipped while computing the line number and function name placed in the `LogRecord` built for the logging event. This proves handy within logging helpers, ensuring the recorded function name, filename and line number reflect not the helper function/method's own data, but instead that of its caller. This parameter's name matches the equivalent one in the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module.

The fourth keyword argument is *extra*, usable for passing a dictionary that fills the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) of the `LogRecord` built for the logging event with user-defined attributes. You can then put these custom attributes to whatever use you like. For instance, they could be folded into logged messages. For example:

```python
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

```

would print something like

```none
2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset

```

The keys within the dictionary passed in *extra* shouldn't collide with the keys the logging system already uses. (See the section on LogRecord attributes for more on which keys the logging system uses.)

Should you decide to use these attributes in logged messages, a little care is in order. In the example above, for instance, the `Formatter` has been configured with a format string that expects ‘clientip’ and ‘user’ in the attribute dictionary of the `LogRecord`. When these are absent, the message won't be logged because a string formatting exception will be raised. So here you must always pass the *extra* dictionary carrying these keys.

Annoying though this may be, the feature is meant for use in specialized situations, such as multi-threaded servers where the same code runs across many contexts, and the interesting conditions that crop up depend on that context (for instance, the remote client IP address along with the authenticated user name, as in the example above). Under such conditions, it's likely that specialized `Formatter`s would be paired with particular `Handler`s.

When no handler is attached to this logger (nor to any of its ancestors, accounting for the relevant `Logger.propagate` attributes), the message goes to the handler set on `lastResort`.

Changed in version 3.2: The *stack_info* parameter was added.

Changed in version 3.5: The *exc_info* parameter can now accept exception instances.

Changed in version 3.8: The *stacklevel* parameter was added.

 info(*msg*, **args*, ***kwargs*)

Logs a message at level `INFO` on this logger. The arguments carry the same meaning as for `debug()`.

 warning(*msg*, **args*, ***kwargs*)

Logs a message at level `WARNING` on this logger. The arguments carry the same meaning as for `debug()`.

Note

An outdated method `warn` exists that works identically to `warning`. Since `warn` is deprecated, please steer clear of it — use `warning` instead.

 error(*msg*, **args*, ***kwargs*)

Logs a message at level `ERROR` on this logger. The arguments carry the same meaning as for `debug()`.

 critical(*msg*, **args*, ***kwargs*)

Logs a message at level `CRITICAL` on this logger. The arguments carry the same meaning as for `debug()`.

 log(*level*, *msg*, **args*, ***kwargs*)

Logs a message at integer level *level* on this logger. The remaining arguments carry the same meaning as for `debug()`.

 exception(*msg*, **args*, ***kwargs*)

Logs a message at level `ERROR` on this logger. The arguments carry the same meaning as for `debug()`. Exception info is added onto the logging message. This method ought to be invoked only from inside an exception handler.

[Subject index](INDEX.md) · [Previous](logging-logger-setlevel-to-logging-logger-getchildren.md) · [Continue](logging-logger-addfilter-to-logging-logger-hashandlers.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Logger; name](logging-logger-class.md) · [Owning module, declaration or section: Logger Objects](logging-logger-class.md)

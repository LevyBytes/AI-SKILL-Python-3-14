# logging.Formatter.__init__: defaults, styles, versions and time conversion

logging.Formatter.__init__(*fmt=None*, *datefmt=None*, *style='%'*)
When no message format string is supplied, the fallback is the raw message itself. When no date format string is given, the date defaults to:

```none
%Y-%m-%d %H:%M:%S

```

with the milliseconds appended afterward. The `style` argument accepts `'%'`, `'{'`, or `'$'`. When none of these is provided, `'%'` is the value that applies.

When the `style` equals `'%'`, the message format string relies on `%(<dictionary key>)s` styled string substitution; the available keys appear in [LogRecord attributes](https://docs.python.org/3.14/library/logging.html#logrecord-attributes). When the style is `'{'`, the message format string is taken to work with [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) (via keyword arguments); when the style is `'$'`, the message format string ought to match what [`string.Template.substitute()`](https://docs.python.org/3.14/library/string.html#string.Template.substitute) expects.

Changed in version 3.2: Added the `style` parameter.

This message format string below records, in sequence, the time in a readable form, the message's severity, and the message body itself:

```python
'%(asctime)s - %(levelname)s - %(message)s'

```

To turn a record's creation time into a tuple, Formatters call a function the user can configure. The default choice is [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime); to override this on a single formatter instance, assign that instance's `converter` attribute a function whose signature matches `time.localtime()` or [`time.gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime). To override it across every formatter - say, when you want all logging times rendered in GMT - assign the `converter` attribute on the Formatter class (use `time.gmtime` for a GMT display).

[Subject index](INDEX.md) · [Previous source owning section](formatters.md) · [Formatters](formatters.md) · [Previous source context](formatters.md) · [Direct logger, handler and formatter configuration](direct-logger-handler-and-formatter-configuration.md) · [Previous source context](direct-logger-handler-and-formatter-configuration.md) · [Following source context](direct-logger-handler-and-formatter-configuration.md)

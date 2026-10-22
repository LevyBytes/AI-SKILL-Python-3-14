# Formatter style and logging-call interpolation contracts

### Use of alternative formatting styles

Back when logging joined the Python standard library, the sole technique for formatting messages with variable content was the %-formatting method. Python has picked up two more formatting options since: [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template) (introduced in Python 2.4) together with [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) (introduced in Python 2.6).

Beginning with 3.2, logging offers better handling of those two extra formatting styles. The [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) class gained an extra optional keyword argument called `style`. Its default value is `'%'`, while the alternatives `'{'` and `'$'` map onto the two other formatting styles. By default backward compatibility stays intact (just as you'd anticipate), yet once you explicitly pass a style parameter you unlock the option to write format strings compatible with [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) or [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template). The console session below demonstrates what's possible:

```pycon
>>> import logging
>>> root = logging.getLogger()
>>> root.setLevel(logging.DEBUG)
>>> handler = logging.StreamHandler()
>>> bf = logging.Formatter('{asctime} {name} {levelname:8s} {message}',
...                        style='{')
>>> handler.setFormatter(bf)
>>> root.addHandler(handler)
>>> logger = logging.getLogger('foo.bar')
>>> logger.debug('This is a DEBUG message')
2010-10-28 15:11:55,341 foo.bar DEBUG    This is a DEBUG message
>>> logger.critical('This is a CRITICAL message')
2010-10-28 15:12:11,526 foo.bar CRITICAL This is a CRITICAL message
>>> df = logging.Formatter('$asctime $name ${levelname} $message',
...                        style='$')
>>> handler.setFormatter(df)
>>> logger.debug('This is a DEBUG message')
2010-10-28 15:13:06,924 foo.bar DEBUG This is a DEBUG message
>>> logger.critical('This is a CRITICAL message')
2010-10-28 15:13:11,494 foo.bar CRITICAL This is a CRITICAL message
>>>

```

Keep in mind that how logging messages get formatted for their ultimate output to logs has nothing to do with how any single logging message gets put together. The latter is free to keep using %-formatting, as the following shows:

```python
>>> logger.error('This is an%s %s %s', 'other,', 'ERROR,', 'message')
2010-10-28 15:19:29,833 foo.bar ERROR This is another, ERROR, message
>>>

```

Logging calls (`logger.debug()`, `logger.info()` etc.) accept positional parameters solely for the logging message itself, reserving keyword parameters purely to set options governing how the actual logging call is handled (for instance, the `exc_info` keyword parameter signaling that traceback data ought to be logged, or the `extra` keyword parameter signaling extra contextual information to attach to the log). Hence you cannot make logging calls straight away in [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) or [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template) syntax, because under the hood the logging package leans on %-formatting to splice the format string together with the variable arguments. Altering that without breaking backward compatibility isn't feasible, given that every logging call already present in existing code relies on %-format strings.

[Subject index](INDEX.md) · [BraceMessage and DollarMessage implementations and use](bracemessage-and-dollarmessage-implementations-and-use.md) · [LoggerAdapter alternative-style implementation](loggeradapter-alternative-style-implementation.md) · [Previous source context](using-file-rotation.md) · [Following source context](bracemessage-and-dollarmessage-implementations-and-use.md)

# Changing the format of displayed messages

### Changing the format of displayed messages

If you want a different format for displaying messages, you have to state the format you intend to use:

```python
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

```

which would print:

```none
DEBUG:This message should appear on the console
INFO:So should this
WARNING:And this, too

```

You'll observe that the ‘root’ that showed up in the earlier examples is now gone. For the complete list of what may appear within format strings, consult the documentation on [LogRecord attributes](https://docs.python.org/3.14/library/logging.html#logrecord-attributes); for plain usage, though, all you really need are the *levelname* (severity), the *message* (event description, variable data included), and possibly a display of when the event happened. That is covered in the section that follows.

[Subject index](INDEX.md) · [Previous source context](logging-variable-data.md) · [Following source context](displaying-the-date-time-in-messages.md)

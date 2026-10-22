# Displaying the date/time in messages

### Displaying the date/time in messages

When you want an event's date and time shown, drop ‘%(asctime)s’ into your format string:

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

```

which should print something like this:

```none
2010-12-12 11:41:42,612 is when this event was logged.

```

That default date/time presentation (seen above) resembles ISO8601 or [**RFC 3339**](https://datatracker.ietf.org/doc/html/rfc3339.html). Should you want finer control over how the date/time is formatted, hand a *datefmt* argument to `basicConfig`, like in this example:

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

```

which would display something like this:

```none
12/12/2010 11:46:36 AM is when this event was logged.

```

The *datefmt* argument takes the very same format that [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) accepts.

[Subject index](INDEX.md) · [Previous source context](changing-the-format-of-displayed-messages.md) · [Following source context](next-steps.md)

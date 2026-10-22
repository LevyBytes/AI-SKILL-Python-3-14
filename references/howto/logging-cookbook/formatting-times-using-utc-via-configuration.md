# Formatting times using UTC (GMT) via configuration

### Formatting times using UTC (GMT) via configuration

There are occasions where you'd like timestamps rendered in UTC, which a class like the `UTCFormatter` shown below accomplishes:

```python
import logging
import time

class UTCFormatter(logging.Formatter):
    converter = time.gmtime

```

You can then drop the `UTCFormatter` into your code in place of [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter). To wire it up through configuration instead, the [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) API supports the technique demonstrated in this self-contained example:

```python
import logging
import logging.config
import time

class UTCFormatter(logging.Formatter):
    converter = time.gmtime

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'utc': {
            '()': UTCFormatter,
            'format': '%(asctime)s %(message)s',
        },
        'local': {
            'format': '%(asctime)s %(message)s',
        }
    },
    'handlers': {
        'console1': {
            'class': 'logging.StreamHandler',
            'formatter': 'utc',
        },
        'console2': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'root': {
        'handlers': ['console1', 'console2'],
   }
}

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING)
    logging.warning('The local time is %s', time.asctime())

```

Executing this script should yield output resembling:

```none
2015-10-17 12:53:29,501 The local time is Sat Oct 17 13:53:29 2015
2015-10-17 13:53:29,501 The local time is Sat Oct 17 13:53:29 2015

```

which shows the timestamp rendered as both local time and UTC, one per handler.

[Subject index](INDEX.md) · [Previous source context](sending-logging-messages-to-email-with-buffering.md) · [Following source context](using-a-context-manager-for-selective-logging.md)

# Logging to syslog with RFC5424 support

### Logging to syslog with RFC5424 support

Even though [**RFC 5424**](https://datatracker.ietf.org/doc/html/rfc5424.html) goes back to 2009, the typical syslog server still ships configured for the older [**RFC 3164**](https://datatracker.ietf.org/doc/html/rfc3164.html) from 2001. The `logging` package, introduced into Python in 2003, targeted the only protocol that existed back then. Because syslog servers have not broadly adopted RFC 5424 since its release, the [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) behaviour was never revised.

Among the handy capabilities in RFC 5424 is structured data; should you require logging to a syslog server that understands it, a subclassed handler resembling the following gets the job done:

```python
import datetime as dt
import logging.handlers
import re
import socket
import time

class SysLogHandler5424(logging.handlers.SysLogHandler):

    tz_offset = re.compile(r'([+-]\d{2})(\d{2})$')
    escaped = re.compile(r'([\]"\\])')

    def __init__(self, *args, **kwargs):
        self.msgid = kwargs.pop('msgid', None)
        self.appname = kwargs.pop('appname', None)
        super().__init__(*args, **kwargs)

    def format(self, record):
        version = 1
        asctime = dt.datetime.fromtimestamp(record.created).isoformat()
        m = self.tz_offset.match(time.strftime('%z'))
        has_offset = False
        if m and time.timezone:
            hrs, mins = m.groups()
            if int(hrs) or int(mins):
                has_offset = True
        if not has_offset:
            asctime += 'Z'
        else:
            asctime += f'{hrs}:{mins}'
        try:
            hostname = socket.gethostname()
        except Exception:
            hostname = '-'
        appname = self.appname or '-'
        procid = record.process
        msgid = '-'
        msg = super().format(record)
        sdata = '-'
        if hasattr(record, 'structured_data'):
            sd = record.structured_data
            # This should be a dict where the keys are SD-ID and the value is a
            # dict mapping PARAM-NAME to PARAM-VALUE (refer to the RFC for what these
            # mean)
            # There's no error checking here - it's purely for illustration, and you
            # can adapt this code for use in production environments
            parts = []

            def replacer(m):
                g = m.groups()
                return '\\' + g[0]

            for sdid, dv in sd.items():
                part = f'[{sdid}'
                for k, v in dv.items():
                    s = str(v)
                    s = self.escaped.sub(replacer, s)
                    part += f' {k}="{s}"'
                part += ']'
                parts.append(part)
            sdata = ''.join(parts)
        return f'{version} {asctime} {hostname} {appname} {procid} {msgid} {sdata} {msg}'

```

A solid grasp of RFC 5424 is required to make full sense of the code above, and your own situation might differ a little (for instance, in how structural data reaches the log). Even so, the code above ought to be adaptable to your speciric needs. Given that handler, you would supply structured data with something along these lines:

```python
sd = {
    'foo@12345': {'bar': 'baz', 'baz': 'bozz', 'fizz': r'buzz'},
    'foo@54321': {'rab': 'baz', 'zab': 'bozz', 'zzif': r'buzz'}
}
extra = {'structured_data': sd}
i = 1
logger.debug('Message %d', i, extra=extra)

```

[Subject index](INDEX.md) · [Previous source context](gui-application-and-logging-entry-point.md) · [Following source context](loggerwriter-file-like-adapter-and-stdout-stderr-routing.md)

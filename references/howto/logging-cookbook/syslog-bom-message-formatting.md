# Inserting a BOM into messages sent to a SysLogHandler continuation

Because that behaviour was faulty, the faulty BOM insertion logic was dropped starting with Python 3.2.4. No substitute was added, though, so when you want to emit [**RFC 5424**](https://datatracker.ietf.org/doc/html/rfc5424.html)-compliant messages that carry a BOM, then an optional pure-ASCII run ahead of it, and finally arbitrary Unicode afterward, all encoded in UTF-8, here is what to do:

1.

Bind a [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) object onto your [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) object, giving it a format string along these lines:

```python
'ASCII section\ufeffUnicode section'

```

Under UTF-8 encoding, the Unicode code point U+FEFF turns into a UTF-8 BOM – that is, the byte-string `b'\xef\xbb\xbf'`.

2.

Swap out the ASCII section for any placeholders you prefer, just ensure that whatever lands there post-substitution stays ASCII (so it survives UTF-8 encoding without change).

3.

Swap out the Unicode section for any placeholders you prefer; should the post-substitution data hold characters beyond the ASCII range, no problem – it gets encoded with UTF-8.

`SysLogHandler` *will* encode the formatted message using UTF-8 encoding. Obeying the rules above lets you turn out [**RFC 5424**](https://datatracker.ietf.org/doc/html/rfc5424.html)-compliant messages. Ignore them and logging itself may stay quiet, yet your messages won't be RFC 5424-compliant, and your syslog daemon could object.

[Subject index](INDEX.md) · [Previous source owning section](inserting-a-bom-into-messages-sent-to-a-sysloghandler.md) · [Following source context](implementing-structured-logging.md)

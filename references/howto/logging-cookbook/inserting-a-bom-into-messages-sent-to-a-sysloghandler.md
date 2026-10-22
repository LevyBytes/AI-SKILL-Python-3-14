# Inserting a BOM into messages sent to a SysLogHandler

### Inserting a BOM into messages sent to a SysLogHandler

[**RFC 5424**](https://datatracker.ietf.org/doc/html/rfc5424.html) mandates that a Unicode message reach a syslog daemon as a sequence of bytes laid out like so: an optional pure-ASCII portion, then a UTF-8 Byte Order Mark (BOM), then Unicode encoded in UTF-8. (Refer to the [**relevant section of the specification**](https://datatracker.ietf.org/doc/html/rfc5424.html#section-6).)

Within Python 3.1, code landed in [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) to slot a BOM into the message, but regrettably it was done wrong, placing the BOM at the very start of the message and thereby barring any pure-ASCII portion from preceding it.

[Subject index](INDEX.md) · [Following source continuation](syslog-bom-message-formatting.md) · [Previous source context](main-function-process-startup-joins-and-shutdown.md)

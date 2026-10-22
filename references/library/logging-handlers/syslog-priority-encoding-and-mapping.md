# logging.handlers.SysLogHandler: `encodePriority()`, `mapPriority()`

Changed in version 3.2.1: (See: [bpo-12168](https://bugs.python.org/issue?@action=redirect&bpo=12168).) Older releases always closed the message handed to the syslog daemons with a NUL byte, since early daemons looked for a NUL-terminated message even though no such requirement appears in the governing specification ([**RFC 5424**](https://datatracker.ietf.org/doc/html/rfc5424.html)). Newer daemons no longer look for that NUL byte but will trim it away if present, while the most recent daemons — those tracking RFC 5424 more faithfully — carry the NUL byte through as part of the message itself.

So that syslog messages can be handled more readily across all these varying daemon behaviours, whether the NUL byte is appended is now adjustable by way of a class-level attribute, `append_nul`. It starts at `True` (keeping the prior behaviour), yet on any `SysLogHandler` instance you may set it to `False` so that instance will *not* tack on the NUL terminator.

Changed in version 3.3: (See: [bpo-12419](https://bugs.python.org/issue?@action=redirect&bpo=12419).) Older releases had no mechanism for an “ident” or “tag” prefix that flags where a message came from. You can now declare one through a class-level attribute, which defaults to `""` to keep the prior behaviour but may be overridden on a `SysLogHandler` instance so that instance prepends the ident onto every message it handles. Mind that the ident you give has to be text rather than bytes, and it is placed at the front of the message verbatim.

 encodePriority(*facility*, *priority*)

Packs the facility and priority together into an integer. Either strings or integers are acceptable here; hand over strings and internal mapping dictionaries translate them into integers.

`SysLogHandler` defines the symbolic `LOG_` values, which echo those laid out in the `sys/syslog.h` header file.

**Priorities**

| Name (string) | Symbolic value |
| --- | --- |
| `alert` | LOG_ALERT |
| `crit` or `critical` | LOG_CRIT |
| `debug` | LOG_DEBUG |
| `emerg` or `panic` | LOG_EMERG |
| `err` or `error` | LOG_ERR |
| `info` | LOG_INFO |
| `notice` | LOG_NOTICE |
| `warn` or `warning` | LOG_WARNING |

**Facilities**

| Name (string) | Symbolic value |
| --- | --- |
| `auth` | LOG_AUTH |
| `authpriv` | LOG_AUTHPRIV |
| `cron` | LOG_CRON |
| `daemon` | LOG_DAEMON |
| `ftp` | LOG_FTP |
| `kern` | LOG_KERN |
| `lpr` | LOG_LPR |
| `mail` | LOG_MAIL |
| `news` | LOG_NEWS |
| `syslog` | LOG_SYSLOG |
| `user` | LOG_USER |
| `uucp` | LOG_UUCP |
| `local0` | LOG_LOCAL0 |
| `local1` | LOG_LOCAL1 |
| `local2` | LOG_LOCAL2 |
| `local3` | LOG_LOCAL3 |
| `local4` | LOG_LOCAL4 |
| `local5` | LOG_LOCAL5 |
| `local6` | LOG_LOCAL6 |
| `local7` | LOG_LOCAL7 |

 mapPriority(*levelname*)

Translates a logging level name into a syslog priority name. Overriding it may be necessary if you run custom levels or if the built-in algorithm does not suit you. That built-in algorithm sends `DEBUG`, `INFO`, `WARNING`, `ERROR` and `CRITICAL` to their matching syslog names, and routes every other level name to ‘warning’.

[Subject index](INDEX.md) · [Continue](logging-handlers-nteventloghandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.SysLogHandler](logging-handlers-sysloghandler-class.md) · [Owning module, declaration or section: SysLogHandler](logging-handlers-sysloghandler-class.md) · [Owning module, declaration or section: emit](syslog-handler-lifecycle-and-emission.md) · [Preceding source contract and version conditions](syslog-handler-lifecycle-and-emission.md)

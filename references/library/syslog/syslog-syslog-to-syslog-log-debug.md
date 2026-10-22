# syslog: Syslog messages, connection control and priorities

## syslog — Unix syslog library routines

### `syslog` — Unix syslog library routines

---

This module exposes an interface to the Unix `syslog` library routines. For a thorough account of the `syslog` facility, turn to the Unix manual pages.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not iOS.

This module is a wrapper around the system's `syslog` family of routines. For a pure Python library capable of talking to a syslog server, see [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) in the [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers) module.

This module supplies the functions below:

 syslog.syslog(*message*)

 syslog.syslog(*priority*, *message*)

Hands the string *message* off to the system logger, appending a closing newline where one is needed. Every message gets stamped with a priority made up of a *facility* and a *level*. The optional *priority* argument, defaulting to `LOG_INFO`, fixes the message's priority. When the facility is not folded into *priority* by way of logical-or (`LOG_INFO | LOG_USER`), the value supplied to the `openlog()` call applies instead.

When `openlog()` has gone uncalled ahead of the `syslog()` call, `openlog()` is invoked with no arguments.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `syslog.syslog` with arguments `priority`, `message`.

Changed in version 3.2: Earlier releases would not invoke `openlog()` on their own when it had gone uncalled before `syslog()`, instead leaving it to the syslog implementation to call `openlog()`.

Changed in version 3.12: This function carries a restriction within subinterpreters. (Only code running across several interpreters feels the effect, and the limitation matters little for most users.) `openlog()` has to run in the main interpreter before `syslog()` can be used inside a subinterpreter. Failing that, it raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 syslog.openlog([*ident*[, *logoption*[, *facility*]]])

Calling `openlog()` lets you set the logging options that later `syslog()` calls will use. When the log is not open at the time, `syslog()` invokes `openlog()` with no arguments.

The optional *ident* keyword argument is a string placed in front of every message; it defaults to `sys.argv[0]` once the leading path components are removed. The optional *logoption* keyword argument (0 by default) is a bit field — the combinable values appear below. The optional *facility* keyword argument (`LOG_USER` by default) establishes the default facility for any message that lacks one explicitly encoded.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `syslog.openlog` with arguments `ident`, `logoption`, `facility`.

Changed in version 3.2: Earlier releases barred keyword arguments and made *ident* mandatory.

Changed in version 3.12: This function carries a restriction within subinterpreters. (Only code running across several interpreters feels the effect, and the limitation matters little for most users.) It may run solely in the main interpreter, and calling it from a subinterpreter raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 syslog.closelog()

Restores the syslog module's values and invokes the system library's `closelog()`.

This returns the module to the state it holds right after its first import. To illustrate, `openlog()` will fire on the next `syslog()` call (provided `openlog()` has not already run), and *ident* along with the other `openlog()` parameters revert to their defaults.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `syslog.closelog` with no arguments.

Changed in version 3.12: This function carries a restriction within subinterpreters. (Only code running across several interpreters feels the effect, and the limitation matters little for most users.) It may run solely in the main interpreter, and calling it from a subinterpreter raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 syslog.setlogmask(*maskpri*)

Sets the priority mask to *maskpri* and hands back whatever the mask held before. Any `syslog()` call whose priority level is not flagged in *maskpri* gets skipped. By default every priority is logged. The `LOG_MASK(pri)` function works out the mask for the single priority *pri*, while `LOG_UPTO(pri)` works out the mask covering all priorities through *pri* inclusive.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `syslog.setlogmask` with argument `maskpri`.

This module supplies the constants below:

 syslog.LOG_EMERG

 syslog.LOG_ALERT

 syslog.LOG_CRIT

 syslog.LOG_ERR

 syslog.LOG_WARNING

 syslog.LOG_NOTICE

 syslog.LOG_INFO

 syslog.LOG_DEBUG

Priority levels (high to low).

[Subject index](INDEX.md) · [Continue](syslog-log-auth-to-syslog-log-local7.md)

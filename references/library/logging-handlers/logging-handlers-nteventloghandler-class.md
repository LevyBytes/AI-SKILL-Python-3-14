# logging.handlers: `logging.handlers.NTEventLogHandler`

### NTEventLogHandler

Living in the `logging.handlers` module, the `NTEventLogHandler` class lets you route logging messages into a local event log on Windows NT, Windows 2000 or Windows XP. Using it first requires that Mark Hammond's Win32 extensions for Python be installed.

 *class *logging.handlers.NTEventLogHandler(*appname*, *dllname=None*, *logtype='Application'*)

Hands back a fresh instance of the `NTEventLogHandler` class. The *appname* sets the application name that shows up in the event log, and a fitting registry entry is built from this name. The *dllname* should supply the fully qualified pathname of a .dll or .exe holding the message definitions to be kept in the log (leave it out and `'win32service.pyd'` is used instead — that file ships with the Win32 extensions and carries a few basic placeholder message definitions. Be warned that relying on those placeholders bloats your event logs, since the whole message source is stored in the log. For leaner logs, you must supply the name of your own .dll or .exe carrying the message definitions you intend to use in the event log). The *logtype* is one of `'Application'`, `'System'` or `'Security'`, defaulting to `'Application'`.

[Subject index](INDEX.md) · [Previous](syslog-priority-encoding-and-mapping.md) · [Continue](windows-event-log-handler-lifecycle-and-message-id.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)

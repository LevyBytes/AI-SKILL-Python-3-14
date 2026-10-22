# logging.config — Configuration file format — Code example: [handler_hand02]

```ini
[handler_hand02]
class=FileHandler
level=DEBUG
formatter=form02
args=('python.log', 'w')

[handler_hand03]
class=handlers.SocketHandler
level=INFO
formatter=form03
args=('localhost', handlers.DEFAULT_TCP_LOGGING_PORT)

[handler_hand04]
class=handlers.DatagramHandler
level=WARN
formatter=form04
args=('localhost', handlers.DEFAULT_UDP_LOGGING_PORT)

[handler_hand05]
class=handlers.SysLogHandler
level=ERROR
formatter=form05
args=(('localhost', handlers.SYSLOG_UDP_PORT), handlers.SysLogHandler.LOG_USER)

[handler_hand06]
class=handlers.NTEventLogHandler
level=CRITICAL
formatter=form06
args=('Python Application', '', 'Application')

[handler_hand07]
class=handlers.SMTPHandler
level=WARN
formatter=form07
args=('localhost', 'from@abc', ['user1@abc', 'user2@xyz'], 'Logger Subject')
kwargs={'timeout': 10.0}

[handler_hand08]
class=handlers.MemoryHandler
level=NOTSET
formatter=form08
target=
args=(10, ERROR)

[handler_hand09]
class=handlers.HTTPHandler
level=NOTSET
formatter=form09
args=('localhost:9022', '/log', 'GET')
kwargs={'secure': True}

```

Sections that lay out formatter configuration look like the one below.

```ini
[formatter_form01]
format=F1 %(asctime)s %(levelname)s %(message)s %(customfield)s
datefmt=
style=%
validate=True
defaults={'customfield': 'defaultvalue'}
class=logging.Formatter

```

The arguments used in the formatter configuration line up with the keys found in the formatters section of the dictionary schema.

After being [evaluated](https://docs.python.org/3.14/library/functions.html#func-eval) within the `logging` package's namespace, the `defaults` entry yields a dictionary of fallback values for custom formatting fields. Absent a value, it defaults to `None`.

Note

Because of the reliance on [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) described above, employing `listen()` to ship configurations to and from sockets carries possible security hazards. Those hazards apply only where several mutually distrustful users execute code on one shared machine; the `listen()` documentation has further details.

See also

Module [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging)

The API reference covering the logging module.

Module [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers)

Handy handlers that ship with the logging module.

[Subject index](INDEX.md) · [Previous](logging-file-configuration-overview.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md) · [Owning module, declaration or section: Configuration file format](logging-file-configuration-overview.md)

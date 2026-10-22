# CLI logging output at default, DEBUG and WARNING levels

Launching this application at the default log level produces output along these lines:

```shell
$ python app.py start foo
INFO start Started the 'foo' service.

$ python app.py stop foo bar
INFO stop Stopped the 'foo' and 'bar' services.

$ python app.py restart foo bar baz
INFO restart Restarted the 'foo', 'bar' and 'baz' services.

```

The leading word is the logging level, and the word after it is the module or package name identifying where the event was logged.

Altering the logging level changes what gets sent to the log. For instance, when we want extra detail:

```shell
$ python app.py --log-level DEBUG start foo
DEBUG start About to start foo
INFO start Started the 'foo' service.

$ python app.py --log-level DEBUG stop foo bar
DEBUG stop About to stop 'foo' and 'bar'
INFO stop Stopped the 'foo' and 'bar' services.

$ python app.py --log-level DEBUG restart foo bar baz
DEBUG restart About to restart 'foo', 'bar' and 'baz'
INFO restart Restarted the 'foo', 'bar' and 'baz' services.

```

And when we want less:

```shell
$ python app.py --log-level WARNING start foo
$ python app.py --log-level WARNING stop foo bar
$ python app.py --log-level WARNING restart foo bar baz

```

Here the commands write nothing to the console, because they log nothing at `WARNING` level or higher.

[Subject index](INDEX.md) · [CLI logging dispatcher and common log-level setup](cli-logging-dispatcher-and-common-log-level-setup.md) · [Start, stop and restart modules](start-stop-and-restart-modules.md) · [Previous source context](start-stop-and-restart-modules.md) · [Following source context](a-qt-gui-for-logging.md)

# logging.handlers.HTTPHandler: `mapLogRecord()`, `emit()`

mapLogRecord(*record*)

Yields a dictionary, drawn from `record`, that is then URL-encoded and shipped to the web server. By default the implementation merely hands back `record.__dict__`. Override this method when, say, only part of the [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) should reach the web server, or when you need finer control over what gets sent.

 emit(*record*)

Delivers the record to the web server as a URL-encoded dictionary. To turn the record into the dictionary that goes out, the `mapLogRecord()` method is used.

Note

Because getting a record ready to send to a web server differs from an ordinary formatting step, calling [`setFormatter()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.setFormatter) to name a [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) on a `HTTPHandler` accomplishes nothing. Rather than calling [`format()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.format), this handler invokes `mapLogRecord()` and then [`urllib.parse.urlencode()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlencode) to encode the dictionary into a shape fit for sending to a web server.

[Subject index](INDEX.md) · [Previous](logging-handlers-httphandler-class.md) · [Continue](logging-handlers-queuehandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.HTTPHandler](logging-handlers-httphandler-class.md) · [Owning module, declaration or section: HTTPHandler](logging-handlers-httphandler-class.md)

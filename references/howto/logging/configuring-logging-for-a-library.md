# Configuring Logging for a Library

### Configuring Logging for a Library

If you are building a library that relies on logging, be sure to document the way it uses logging - for instance, which logger names it employs. You should also think a little about its logging configuration. Should the consuming application not use logging while your library code issues logging calls, then (per the previous section) events of severity `WARNING` and above will be written to `sys.stderr`. That is considered the ideal default behaviour.

If for whatever reason you *don't* want those messages shown when no logging configuration exists, you can attach a do-nothing handler to your library's top-level logger. Doing so suppresses the printed message, because a handler will always be located for the library's events - it merely emits nothing. Should the library's user set up logging for the application, that setup presumably installs some handlers, and provided the levels are configured appropriately, logging calls in library code will direct their output to those handlers as usual.

The logging package ships with a do-nothing handler: [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) (available since Python 3.1). You could add an instance of this handler to the top-level logger of the logging namespace your library uses (*if* you wish to keep your library's logged events from going to `sys.stderr` when no logging configuration is present). Provided every log call in a library *foo* uses loggers whose names match 'foo.x', 'foo.x.y', and so on, then the code:

```python
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())

```

should achieve the intended result. When an organisation ships several libraries, the chosen logger name can be 'orgname.foo' instead of plain 'foo'.

Note

You are strongly urged *not to log to the root logger* from within your library. Instead, pick a logger whose name is unique and easy to recognise, such as the `__name__` belonging to the top-level package or module of your library. Sending output to the root logger makes it hard or impossible for the application developer to set the logging verbosity or handlers of your library to suit their wishes.

Note

You are strongly urged *not to attach any handlers other than* [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) *to your library's loggers*. The reason is that deciding on handlers is the prerogative of the application developer who consumes your library. That developer understands their audience and which handlers best fit their application: if you add handlers 'under the hood', you may well disrupt their ability to run unit tests and produce logs that meet their needs.

[Subject index](INDEX.md) · [Previous source context](what-happens-if-no-configuration-is-provided.md) · [Following source context](logging-levels.md)

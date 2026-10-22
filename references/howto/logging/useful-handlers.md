# Useful Handlers

### Useful Handlers

Beyond the base [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) class, a number of handy subclasses come supplied:

1.

[`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) instances dispatch messages to streams (file-like objects).

2.

[`FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler) instances dispatch messages to files on disk.

3.

[`BaseRotatingHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.BaseRotatingHandler) serves as the base class for handlers that rotate log files at a given point. You are not meant to instantiate it directly. Use [`RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler) or [`TimedRotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler) instead.

4.

[`RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler) instances dispatch messages to files on disk, with support for capping log file sizes and rotating log files.

5.

[`TimedRotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler) instances dispatch messages to files on disk, rotating the log file at set timed intervals.

6.

[`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler) instances dispatch messages to TCP/IP sockets. As of 3.4, Unix domain sockets are supported as well.

7.

[`DatagramHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.DatagramHandler) instances dispatch messages to UDP sockets. As of 3.4, Unix domain sockets are supported as well.

8.

[`SMTPHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SMTPHandler) instances dispatch messages to a specified email address.

9.

[`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) instances dispatch messages to a Unix syslog daemon, perhaps running on a remote machine.

10.

[`NTEventLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.NTEventLogHandler) instances dispatch messages to a Windows NT/2000/XP event log.

11.

[`MemoryHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.MemoryHandler) instances dispatch messages to an in-memory buffer that is flushed whenever particular criteria are satisfied.

12.

[`HTTPHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.HTTPHandler) instances dispatch messages to an HTTP server using either `GET` or `POST` semantics.

13.

[`WatchedFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.WatchedFileHandler) instances keep an eye on the file they log to. Should that file change, it is closed and reopened by file name. This handler helps only on Unix-like systems; Windows lacks the underlying mechanism it depends on.

14.

[`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) instances dispatch messages to a queue, like those provided by the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) or [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) modules.

15.

[`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) instances take no action on error messages. Library developers reach for them when they want to use logging but avoid the 'No handlers could be found for logger *XXX*' message that may appear when the library's user has left logging unconfigured. Refer to Configuring Logging for a Library for further details.

Added in version 3.1: The [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) class.

Added in version 3.2: The [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) class.

The [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler), [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) and [`FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler) classes reside in the core logging package. The remaining handlers live in a sub-module, [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers). (A further sub-module, [`logging.config`](https://docs.python.org/3.14/library/logging.config.html#module-logging.config), exists for configuration functionality.)

Logged messages are rendered for presentation by instances of the [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) class. They get initialized with a format string fit for use alongside the % operator and a dictionary.

To format several messages together in a batch, you can use instances of [`BufferingFormatter`](https://docs.python.org/3.14/library/logging.html#logging.BufferingFormatter). Alongside the format string (applied to each message in the batch), it also provides for header and trailer format strings.

When filtering by logger level and/or handler level does not suffice, instances of [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) can be attached to both [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) and [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) instances (through their [`addFilter()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.addFilter) method). Before choosing to take a message any further, both loggers and handlers ask all of their filters for permission. Should any filter return a false value, the message proceeds no further.

The base [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) functionality permits filtering by a particular logger name. When this feature is in play, messages directed at the named logger and its children pass the filter, while every other message is dropped.

[Subject index](INDEX.md) · [Previous source context](custom-levels.md) · [Following source context](exceptions-raised-during-logging.md)

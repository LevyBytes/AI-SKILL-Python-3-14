# What's New In Python 3.11 / logging — logging, logging.handlers

### logging

- [`getLevelNamesMapping()`](https://docs.python.org/3.14/library/logging.html#logging.getLevelNamesMapping) was added; it hands back a mapping that ties logging level names (such as `'CRITICAL'`) to the numbers of the matching [Logging Levels](https://docs.python.org/3.14/library/logging.html#levels) (such as `50`, by default). (Contributed by Andrei Kulakovin in [gh-88024](https://github.com/python/cpython/issues/88024).)

- A [`createSocket()`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler.createSocket) method was added to [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler), mirroring [`SocketHandler.createSocket()`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler.createSocket). It fires on its own while the handler initializes and whenever an event is emitted, provided no socket is currently live. (Contributed by Kirill Pinchuk in [gh-88457](https://github.com/python/cpython/issues/88457).)

[Subject index](INDEX.md) · [Previous source section](locale.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)

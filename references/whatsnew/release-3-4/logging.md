# What's New In Python 3.4 / logging — configparser, logging.config, logging.handlers

### logging

The [`TimedRotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler) picked up a fresh *atTime* parameter for naming the time of day at which rollover should occur. (Contributed by Ronald Oussoren in [bpo-9556](https://bugs.python.org/issue?@action=redirect&bpo=9556).)

[`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler) and [`DatagramHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.DatagramHandler) handle Unix domain sockets too (done by passing *port* as `None`). (Contributed by Vinay Sajip in commit ce46195b56a9.)

[`fileConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.fileConfig) accepts a [`configparser.RawConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.RawConfigParser) subclass instance for its *fname* parameter. That helps when logging settings form only one slice of the broader application configuration, or when the program tweaks the configuration ahead of handing it to `fileConfig()`. (Contributed by Vinay Sajip in [bpo-16110](https://bugs.python.org/issue?@action=redirect&bpo=16110).)

Logging configuration arriving over a socket through the [`logging.config.listen()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.listen) function can be checked before it is acted upon, by handing a verification function to the new *verify* keyword argument. (Contributed by Vinay Sajip in [bpo-15452](https://bugs.python.org/issue?@action=redirect&bpo=15452).)

[Subject index](INDEX.md) · [Previous source section](ipaddress.md) · [Next source section](marshal.md) · [Release/subject declaration](release-highlights.md)

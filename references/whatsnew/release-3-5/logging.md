# What’s New In Python 3.5 / logging — logging, logging.handlers, ssl

### logging

Alongside boolean values and exception tuples, every logging method ([`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) [`log()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.log), [`exception()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.exception), [`critical()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.critical), [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.debug), etc.) now also takes exception instances for the *exc_info* argument:

```python
>>> import logging
>>> try:
...     1/0
... except ZeroDivisionError as ex:
...     logging.error('exception', exc_info=ex)
ERROR:root:exception

```

(Contributed by Yury Selivanov in [bpo-20537](https://bugs.python.org/issue?@action=redirect&bpo=20537).)

To set up the SSL behavior of an HTTP connection, the [`handlers.HTTPHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.HTTPHandler) class now takes an optional [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance. (Contributed by Alex Gaynor in [bpo-22788](https://bugs.python.org/issue?@action=redirect&bpo=22788).)

A *respect_handler_level* keyword argument is now accepted by the [`handlers.QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) class; when it is `True`, messages reach handlers with their handler levels respected. (Contributed by Vinay Sajip.)

[Subject index](INDEX.md) · [Previous source section](locale.md) · [Next source section](lzma.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.7 / logging - logging, logging.config, logging.handlers

### logging

[`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instances can be pickled starting now. (Contributed by Vinay Sajip in [bpo-30520](https://bugs.python.org/issue?@action=redirect&bpo=30520).)

A new [`StreamHandler.setStream()`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler.setStream) method lets you swap the logger stream once the handler already exists. (Contributed by Vinay Sajip in [bpo-30522](https://bugs.python.org/issue?@action=redirect&bpo=30522).)

You can now hand keyword arguments to handler constructors through the configuration given to [`logging.config.fileConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.fileConfig). (Contributed by Preston Landers in [bpo-31080](https://bugs.python.org/issue?@action=redirect&bpo=31080).)

[Subject index](INDEX.md) · [Previous source section](locale.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)

# Creating a lot of loggers

### Creating a lot of loggers

Since loggers are singletons that are never released for the duration of a script run, creating many of them consumes memory that cannot later be reclaimed. Instead of spinning up one logger per processed file or network connection, lean on the existing facilities for feeding contextual information into your logs and keep the loggers you create to ones that describe areas of your application (usually modules, though occasionally a touch finer-grained than that).

[Subject index](INDEX.md) · [Previous source context](library-logger-handler-misuse.md) · [Following source context](other-resources.md)

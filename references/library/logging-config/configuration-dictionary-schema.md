# logging.config — Configuration dictionary schema

### Configuration dictionary schema

Spelling out a logging configuration means enumerating the assorted objects to build along with the links among them; for instance, you might build a handler called 'console' and then declare that the logger called 'startup' will route its messages to the 'console' handler. These objects aren't confined to the ones the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module ships, since you might author your own formatter or handler class. The parameters supplied to these classes may also have to take in external objects such as `sys.stderr`. The grammar for spelling out these objects and links is laid out in Object connections below.

[Subject index](INDEX.md) · [Previous](security-considerations.md) · [Continue](logging-dictionary-schema-overview.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)

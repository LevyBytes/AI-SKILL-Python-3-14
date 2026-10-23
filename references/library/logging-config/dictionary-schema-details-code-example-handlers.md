# logging.config - Dictionary Schema Details - Code example: handlers:

```yaml
handlers:
  console:
    class : logging.StreamHandler
    formatter: brief
    level   : INFO
    filters: [allow_foo]
    stream  : ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    formatter: precise
    filename: logconfig.log
    maxBytes: 1024
    backupCount: 3

```

the handler whose id is `console` is built as a [`logging.StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler), with `sys.stdout` serving as the underlying stream. The handler whose id is `file` is built as a [`logging.handlers.RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler) with the keyword arguments `filename='logconfig.log', maxBytes=1024, backupCount=3`.

- *loggers* - the matching value is a dict where each key is a logger name and each value is a dict spelling out how to configure the matching Logger instance.

The configuring dict is scanned for these keys:

  - `level` (optional). The level of the logger.

  - `propagate` (optional). The propagation setting of the logger.

  - `filters` (optional). A list of ids of the filters for this logger.

Changed in version 3.11: alongside ids, `filters` now permits filter instances too.

  - `handlers` (optional). A list of ids of the handlers for this logger.

The named loggers will be configured per the level, propagation, filters and handlers given.

- *root* - this is the configuration for the root logger. The configuration is processed as it would be for any logger, save that the `propagate` setting does not apply.

- *incremental* - whether the configuration should be read as incremental on top of the existing configuration. This value defaults to `False`, meaning the given configuration supplants the existing configuration with the same semantics the existing `fileConfig()` API uses.

When the given value is `True`, the configuration is handled as laid out in the section on Incremental Configuration.

- *disable_existing_loggers* - whether any existing non-root loggers should be disabled. This setting parallels the parameter of the same name in `fileConfig()`. When absent, this parameter defaults to `True`. The value is disregarded when *incremental* is `True`.

[Subject index](INDEX.md) · [Previous](logging-dictionary-schema-overview.md) · [Continue](incremental-configuration.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md) · [Owning module, declaration or section: Dictionary Schema Details](logging-dictionary-schema-overview.md)

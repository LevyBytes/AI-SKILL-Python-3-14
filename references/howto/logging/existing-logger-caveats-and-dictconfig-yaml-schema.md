# Existing-logger caveats and dictConfig YAML schema

Notice that the config-file route offers a couple of benefits over coding it directly in Python: chiefly, it keeps configuration apart from code and lets non-programmers tweak the logging properties with ease.

Warning

The [`fileConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.fileConfig) function accepts a default parameter, `disable_existing_loggers`, whose default is `True` to preserve backward compatibility. That default might not suit you, because it disables any non-root loggers that existed before the `fileConfig()` call, unless the configuration explicitly names them (or one of their ancestors). Consult the reference documentation for the details, and pass `False` for this parameter when that is what you prefer.

The dictionary handed to [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) may likewise carry a Boolean under the key `disable_existing_loggers`, which - if you omit it from the dictionary - is again treated as `True` by default. That produces the same logger-disabling behaviour noted above, which might not be your intent; when that applies, include the key explicitly and set it to `False`.

Bear in mind that class names cited in config files must be either relative to the logging module or absolute values resolvable through the usual import mechanisms. So you could write either [`WatchedFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.WatchedFileHandler) (relative to the logging module) or `mypackage.mymodule.MyHandler` (for a class living in package `mypackage` and module `mymodule`, with `mypackage` reachable on the Python import path).

Python 3.2 brought a fresh way to configure logging that uses dictionaries to carry the configuration details. It offers a superset of what the config-file approach above can do, and it is the recommended configuration method for new applications and deployments. Since a Python dictionary holds the configuration data, and since that dictionary can be populated by various means, you gain more flexibility in how you configure. As an example, you might draw the configuration dictionary from a file in JSON format, or - if YAML processing is available to you - from a file in YAML format. Or naturally you could assemble the dictionary in Python code, receive it in pickled form across a socket, or adopt whatever method fits your application.

What follows is the same configuration as above, expressed in YAML format for the new dictionary-based approach:

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  simpleExample:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]

```

For further details on configuring logging with a dictionary, consult [Configuration functions](https://docs.python.org/3.14/library/logging.config.html#logging-config-api).

[Subject index](INDEX.md) · [Direct logger, handler and formatter configuration](direct-logger-handler-and-formatter-configuration.md) · [fileConfig module, INI schema and resulting output](fileconfig-module-ini-schema-and-resulting-output.md) · [Previous source context](fileconfig-module-ini-schema-and-resulting-output.md) · [Following source context](what-happens-if-no-configuration-is-provided.md)

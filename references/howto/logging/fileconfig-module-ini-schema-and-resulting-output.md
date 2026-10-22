# fileConfig module, INI schema and resulting output

This next Python module builds a logger, handler, and formatter that are essentially the same as those in the preceding example; the sole change is the names given to the objects:

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

This is what the logging.conf file contains:

```ini
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

```

The result matches the earlier non-config-file example almost exactly:

```shell
$ python simple_logging_config.py
2005-03-19 15:38:55,977 - simpleExample - DEBUG - debug message
2005-03-19 15:38:55,979 - simpleExample - INFO - info message
2005-03-19 15:38:56,054 - simpleExample - WARNING - warn message
2005-03-19 15:38:56,055 - simpleExample - ERROR - error message
2005-03-19 15:38:56,130 - simpleExample - CRITICAL - critical message

```

[Subject index](INDEX.md) · [Direct logger, handler and formatter configuration](direct-logger-handler-and-formatter-configuration.md) · [Existing-logger caveats and dictConfig YAML schema](existing-logger-caveats-and-dictconfig-yaml-schema.md) · [Previous source context](direct-logger-handler-and-formatter-configuration.md) · [Following source context](existing-logger-caveats-and-dictconfig-yaml-schema.md)

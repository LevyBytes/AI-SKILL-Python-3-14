# Direct logger, handler and formatter configuration

### Configuring Logging

There are three approaches a programmer can take to configure logging:

1.

Building loggers, handlers, and formatters directly with Python code that invokes the configuration methods described above.

2.

Writing a logging config file and loading it via the [`fileConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.fileConfig) function.

3.

Building a dictionary holding the configuration details and handing it to the [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) function.

The reference docs for those latter two approaches live at [Configuration functions](https://docs.python.org/3.14/library/logging.config.html#logging-config-api). The example that follows sets up a very basic logger, a console handler, and a basic formatter, all in Python code:

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

Invoking this module from the command line yields the output below:

```shell
$ python simple_logging_module.py
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
2005-03-19 15:10:26,620 - simple_example - INFO - info message
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
2005-03-19 15:10:26,697 - simple_example - ERROR - error message
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message

```

[Subject index](INDEX.md) · [logging.Formatter.__init__: defaults, styles, versions and time conversion](logging-formatter-defaults-styles-and-time-conversion.md) · [fileConfig module, INI schema and resulting output](fileconfig-module-ini-schema-and-resulting-output.md) · [Existing-logger caveats and dictConfig YAML schema](existing-logger-caveats-and-dictconfig-yaml-schema.md) · [Following source context](logging-formatter-defaults-styles-and-time-conversion.md) · [Previous source context](logging-formatter-defaults-styles-and-time-conversion.md) · [Following source context](fileconfig-module-ini-schema-and-resulting-output.md)

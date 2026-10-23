# What's New In Python 3.2 / PEP 391: Dictionary Based Configuration for Logging - configparser, logging, logging.config

### PEP 391: Dictionary Based Configuration for Logging

The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module shipped two configuration approaches: one driven by per-option function calls, the other reading an external file written in [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) format. Neither approach allowed building configurations out of JSON or YAML, and neither permitted incremental configuration, something required when logger options come from a command line.

Aiming for greater flexibility, the module now exposes [`logging.config.dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) so that logging can be configured from ordinary Python dictionaries. Configurable elements span formatters, handlers, filters, and loggers. A functioning configuration dictionary looks like this:

```python
{"version": 1,
 "formatters": {"brief": {"format": "%(levelname)-8s: %(name)-15s: %(message)s"},
                "full": {"format": "%(asctime)s %(name)-15s %(levelname)-8s %(message)s"}
                },
 "handlers": {"console": {
                   "class": "logging.StreamHandler",
                   "formatter": "brief",
                   "level": "INFO",
                   "stream": "ext://sys.stdout"},
              "console_priority": {
                   "class": "logging.StreamHandler",
                   "formatter": "full",
                   "level": "ERROR",
                   "stream": "ext://sys.stderr"}
              },
 "root": {"level": "DEBUG", "handlers": ["console", "console_priority"]}}

```

Saving that dictionary into a file named `conf.json` lets you read and apply it with code along these lines:

```python
>>> import json, logging.config
>>> with open('conf.json') as f:
...     conf = json.load(f)
...
>>> logging.config.dictConfig(conf)
>>> logging.info("Transaction completed normally")
INFO    : root           : Transaction completed normally
>>> logging.critical("Abnormal termination")
2011-02-17 11:14:36,694 root            CRITICAL Abnormal termination

```

See also

[**PEP 391**](https://peps.python.org/pep-0391/) - Dictionary Based Configuration for Logging

PEP written by Vinay Sajip.

[Subject index](INDEX.md) · [Previous source section](pep-389-argparse-command-line-parsing-module-see-also.md) · [Next source section](pep-3148-the-concurrent-futures-module.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

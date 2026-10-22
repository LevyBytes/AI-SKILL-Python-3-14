# Route logging severities to stdout, stderr and file

### Custom handling of levels

Now and then you may want behaviour that departs a little from the usual level handling in handlers, where everything above some cutoff is dispatched by a handler. Filters are the tool for that. Consider a situation in which you would like to arrange matters this way:

- Send messages of severity `INFO` and `WARNING` to `sys.stdout`

- Send messages of severity `ERROR` and above to `sys.stderr`

- Send messages of severity `DEBUG` and above to file `app.log`

Imagine your logging is set up with this JSON:

```json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s - %(message)s"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "app.log",
            "mode": "w"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stderr",
            "stdout",
            "file"
        ]
    }
}

```

[Subject index](INDEX.md) · [Level filter factory and stdout handler configuration](level-filter-factory-and-stdout-handler-configuration.md) · [Complete custom-severity main.py](complete-custom-severity-main-py.md) · [Run and inspect custom severity output](run-and-inspect-custom-severity-output.md) · [Previous source context](logging-to-multiple-destinations.md) · [Following source context](level-filter-factory-and-stdout-handler-configuration.md)

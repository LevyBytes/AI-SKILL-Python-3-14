# Level filter factory and stdout handler configuration

This setup gets us *almost* there, with one snag: `sys.stdout` would surface messages of severity `ERROR`, and events at that severity and above get captured along with the `INFO` and `WARNING` messages. To stop that, we can install a filter that drops those messages and bolt it onto the appropriate handler. The way to wire this in is to add a `filters` section alongside `formatters` and `handlers`:

```json
{
    "filters": {
        "warnings_and_below": {
            "()" : "__main__.filter_maker",
            "level": "WARNING"
        }
    }
}

```

and reworking the `stdout` handler section so it references the filter:

```json
{
    "stdout": {
        "class": "logging.StreamHandler",
        "level": "INFO",
        "formatter": "simple",
        "stream": "ext://sys.stdout",
        "filters": ["warnings_and_below"]
    }
}

```

Since a filter is nothing more than a function, the `filter_maker` (a factory function) can be written like so:

```python
def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter

```

It turns the string argument it receives into a numeric level and hands back a function that yields `True` only when the level of the supplied record sits at or beneath the named level. Be aware that here I have placed the `filter_maker` inside a test script `main.py` launched from the command line, so its module turns out to be `__main__` - which is why the configuration reads `__main__.filter_maker`. Swap that out if your definition lives in some other module.

[Subject index](INDEX.md) · [Route logging severities to stdout, stderr and file](route-logging-severities-to-stdout-stderr-and-file.md) · [Complete custom-severity main.py](complete-custom-severity-main-py.md) · [Run and inspect custom severity output](run-and-inspect-custom-severity-output.md) · [Previous source context](route-logging-severities-to-stdout-stderr-and-file.md) · [Following source context](complete-custom-severity-main-py.md)

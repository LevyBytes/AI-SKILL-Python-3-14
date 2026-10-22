# Imparting contextual information in handlers

### Imparting contextual information in handlers

Every [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) carries an independent filter chain. To attach contextual data to a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) without that data spilling over into other handlers, apply a filter that hands back a fresh `LogRecord` rather than editing the original in place. The script below illustrates the idea:

```python
import copy
import logging

def filter(record: logging.LogRecord):
    record = copy.copy(record)
    record.user = 'jim'
    return record

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s from %(user)-8s')
    handler.setFormatter(formatter)
    handler.addFilter(filter)
    logger.addHandler(handler)

    logger.info('A log message')

```

[Subject index](INDEX.md) · [Previous source context](context-variable-logging-output.md) · [Following source context](imports-listener-configuration-and-whole-queue-listener-loop.md)

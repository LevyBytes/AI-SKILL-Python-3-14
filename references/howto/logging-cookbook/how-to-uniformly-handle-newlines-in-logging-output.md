# How to uniformly handle newlines in logging output

### How to uniformly handle newlines in logging output

Logged messages (to the console or a file, say) are commonly a single line of text. Yet now and then you must cope with multi-line messages - either because a logging format string carries newlines, or because the logged data itself does. To process such messages consistently, so that every line of the logged message comes out formatted just as if it had been logged on its own, a handler mixin like the snippet below does the trick:

```python
# Assume this is in a module mymixins.py
import copy

class MultilineMixin:
    def emit(self, record):
        s = record.getMessage()
        if '\n' not in s:
            super().emit(record)
        else:
            lines = s.splitlines()
            rec = copy.copy(record)
            rec.args = None
            for line in lines:
                rec.msg = line
                super().emit(rec)

```

The mixin can be applied as shown in the script below:

```python
import logging

from mymixins import MultilineMixin

logger = logging.getLogger(__name__)

class StreamHandler(MultilineMixin, logging.StreamHandler):
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-9s %(message)s',
                        handlers = [StreamHandler()])
    logger.debug('Single line')
    logger.debug('Multiple lines:\nfool me once ...')
    logger.debug('Another single line')
    logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')

```

Executing the script prints roughly:

```text
2025-07-02 13:54:47,234 DEBUG     Single line
2025-07-02 13:54:47,234 DEBUG     Multiple lines:
2025-07-02 13:54:47,234 DEBUG     fool me once ...
2025-07-02 13:54:47,234 DEBUG     Another single line
2025-07-02 13:54:47,234 DEBUG     Multiple lines:
2025-07-02 13:54:47,234 DEBUG     fool me ...
2025-07-02 13:54:47,234 DEBUG     can't get fooled again

```

If instead [log injection](https://owasp.org/www-community/attacks/Log_Injection) is your worry, a formatter that escapes newlines will serve, as the example below shows:

```python
import logging

logger = logging.getLogger(__name__)

class EscapingFormatter(logging.Formatter):
    def format(self, record):
        s = super().format(record)
        return s.replace('\n', r'\n')

if __name__ == '__main__':
    h = logging.StreamHandler()
    h.setFormatter(EscapingFormatter('%(asctime)s %(levelname)-9s %(message)s'))
    logging.basicConfig(level=logging.DEBUG, handlers = [h])
    logger.debug('Single line')
    logger.debug('Multiple lines:\nfool me once ...')
    logger.debug('Another single line')
    logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')

```

You are of course free to apply whichever escaping scheme suits you best. Executing the script ought to yield output resembling this:

```text
2025-07-09 06:47:33,783 DEBUG     Single line
2025-07-09 06:47:33,783 DEBUG     Multiple lines:\nfool me once ...
2025-07-09 06:47:33,783 DEBUG     Another single line
2025-07-09 06:47:33,783 DEBUG     Multiple lines:\nfool me ...\ncan't get fooled again

```

Making such escaping the stdlib default is not possible, since doing so would break backwards compatibility.

[Subject index](INDEX.md) · [Previous source context](fragmented-traceback-buffering-writer.md) · [Following source context](patterns-to-avoid.md)

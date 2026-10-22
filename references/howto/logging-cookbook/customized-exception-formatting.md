# Customized exception formatting

### Customized exception formatting

On occasion you may want customized exception formatting - for the sake of argument, suppose you want precisely one line per logged event, even when exception information is included. A custom formatter class lets you do exactly that, as the example below shows:

```python
import logging

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        """
        Format an exception so that it prints on a single line.
        """
        result = super().formatException(exc_info)
        return repr(result)  # or format into one line however you want to

    def format(self, record):
        s = super().format(record)
        if record.exc_text:
            s = s.replace('\n', '') + '|'
        return s

def configure_logging():
    fh = logging.FileHandler('output.txt', 'w')
    f = OneLineExceptionFormatter('%(asctime)s|%(levelname)s|%(message)s|',
                                  '%d/%m/%Y %H:%M:%S')
    fh.setFormatter(f)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(fh)

def main():
    configure_logging()
    logging.info('Sample message')
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logging.exception('ZeroDivisionError: %s', e)

if __name__ == '__main__':
    main()

```

Once run, this yields a file containing exactly two lines:

```none
28/01/2015 07:21:23|INFO|Sample message|
28/01/2015 07:21:23|ERROR|ZeroDivisionError: division by zero|'Traceback (most recent call last):\n  File "logtest7.py", line 30, in main\n    x = 1 / 0\nZeroDivisionError: division by zero'|

```

Simplistic though the treatment above is, it indicates how exception information can be shaped to suit your taste. For more specialized requirements the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module may come in handy.

[Subject index](INDEX.md) · [Previous source context](configuring-filters-with-dictconfig.md) · [Following source context](speaking-logging-messages.md)

# LoggerAdapter alternative-style implementation

Should you rather, a [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) lets you reach an outcome much like the one above, illustrated in the example that follows:

```python
import logging

class Message:
    def __init__(self, fmt, args):
        self.fmt = fmt
        self.args = args

    def __str__(self):
        return self.fmt.format(*self.args)

class StyleAdapter(logging.LoggerAdapter):
    def log(self, level, msg, /, *args, stacklevel=1, **kwargs):
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            self.logger.log(level, Message(msg, args), **kwargs,
                            stacklevel=stacklevel+1)

logger = StyleAdapter(logging.getLogger(__name__))

def main():
    logger.debug('Hello, {}', 'world!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()

```

Running the script above under Python 3.8 or newer should emit the message `Hello, world!`.

[Subject index](INDEX.md) · [Formatter style and logging-call interpolation contracts](formatter-style-and-logging-call-interpolation-contracts.md) · [BraceMessage and DollarMessage implementations and use](bracemessage-and-dollarmessage-implementations-and-use.md) · [Previous source context](bracemessage-and-dollarmessage-implementations-and-use.md) · [Following source context](log-record-factories.md)

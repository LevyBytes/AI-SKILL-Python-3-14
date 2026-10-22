# Implementing structured logging

### Implementing structured logging

Most logging messages target human readers and so resist easy machine parsing, but some situations call for emitting messages in a structured layout that *is* parseable by a program (with no need for elaborate regular expressions to read the log message). The logging package makes this simple to do. Several routes lead there, and the one below is a basic technique that leans on JSON to serialise the event in a way a machine can parse:

```python
import json
import logging

class StructuredMessage:
    def __init__(self, message, /, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))

_ = StructuredMessage   # optional, to improve readability

logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(_('message 1', foo='bar', bar='baz', num=123, fnum=123.456))

```

Running the script above outputs:

```none
message 1 >>> {"fnum": 123.456, "num": 123, "bar": "baz", "foo": "bar"}

```

Be aware that item ordering can vary depending on which Python version you run.

Should you require more specialised handling, a custom JSON encoder works, as the complete example below demonstrates:

```python
import json
import logging

class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return tuple(o)
        elif isinstance(o, str):
            return o.encode('unicode_escape').decode('ascii')
        return super().default(o)

class StructuredMessage:
    def __init__(self, message, /, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        s = Encoder().encode(self.kwargs)
        return '%s >>> %s' % (self.message, s)

_ = StructuredMessage   # optional, to improve readability

def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(_('message 1', set_value={1, 2, 3}, snowman='\u2603'))

if __name__ == '__main__':
    main()

```

Running the script above outputs:

```none
message 1 >>> {"snowman": "\u2603", "set_value": [1, 2, 3]}

```

Be aware that item ordering can vary depending on which Python version you run.

[Subject index](INDEX.md) · [Previous source context](syslog-bom-message-formatting.md) · [Following source context](owned-file-handler-factory-and-dictconfig-schema.md)

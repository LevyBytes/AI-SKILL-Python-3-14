# Using custom message objects

### Using custom message objects

A different and arguably simpler route lets you apply {}- and $- formatting when assembling your individual log messages. You might remember (from [Using arbitrary objects as messages](https://docs.python.org/3.14/howto/logging.html#arbitrary-object-messages)) that while logging you're free to hand in any arbitrary object to act as the message format string, with the logging package then calling [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) upon it to derive the genuine format string. Take these two classes as an example:

```python
class BraceMessage:
    def __init__(self, fmt, /, *args, **kwargs):
        self.fmt = fmt
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.fmt.format(*self.args, **self.kwargs)

class DollarMessage:
    def __init__(self, fmt, /, **kwargs):
        self.fmt = fmt
        self.kwargs = kwargs

    def __str__(self):
        from string import Template
        return Template(self.fmt).substitute(**self.kwargs)

```

You can drop either one in where a format string would go, so that {}- or $-formatting builds the actual “message” portion that shows up in the formatted log output instead of “%(message)s” or “{message}” or “$message”. If spelling out the class names every time you want to log feels clunky, you can make it more palatable with an alias such as `M` or `_` for the message (or maybe `__`, in case you've reserved `_` for localization).

Examples of this approach follow below. First, formatting via [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format):

```python
>>> __ = BraceMessage
>>> print(__('Message with {0} {1}', 2, 'placeholders'))
Message with 2 placeholders
>>> class Point: pass
...
>>> p = Point()
>>> p.x = 0.5
>>> p.y = 0.5
>>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})', point=p))
Message with coordinates: (0.50, 0.50)

```

Second, formatting via [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template):

```python
>>> __ = DollarMessage
>>> print(__('Message with $num $what', num=2, what='placeholders'))
Message with 2 placeholders
>>>

```

Worth noting is that this approach costs you no meaningful performance penalty: the real formatting occurs not at the moment you issue the logging call, but later (and only if) a handler is actually about to write the logged message to a log. So the lone slightly odd thing that may catch you out is that the parentheses wrap the format string together with the arguments, not the format string alone. That happens because the __ notation is merely syntax sugar over a constructor call to one of the `*XXX*Message` classes shown above.

[Subject index](INDEX.md) · [Previous source context](using-logrecord-factories.md) · [Following source context](configuring-filters-with-dictconfig.md)

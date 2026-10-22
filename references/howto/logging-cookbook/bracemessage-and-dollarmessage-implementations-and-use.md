# BraceMessage and DollarMessage implementations and use

Still, there does exist a route by which you can apply {}- and $- formatting when assembling your individual log messages. Bear in mind that a message may take an arbitrary object as its message format string, and that the logging package invokes `str()` on that object to obtain the real format string. Take the two classes below:

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

You can drop either one in where a format string would go, enabling {}- or $-formatting to assemble the genuine "message" portion that lands in the formatted log output instead of "%(message)s" or "{message}" or "$message". Spelling out the full class names every time you log gets clumsy, yet it becomes quite tolerable once you adopt an alias like __ (double underscore — don't mix it up with _, the single underscore that serves as a synonym/alias for [`gettext.gettext()`](https://docs.python.org/3.14/library/gettext.html#gettext.gettext) and friends).

These classes aren't bundled with Python, though copying and pasting them into your own code is trivial. Here's how they'd be used (presuming they live in a module named `wherever`):

```pycon
>>> from wherever import BraceMessage as __
>>> print(__('Message with {0} {name}', 2, name='placeholders'))
Message with 2 placeholders
>>> class Point: pass
...
>>> p = Point()
>>> p.x = 0.5
>>> p.y = 0.5
>>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})',
...       point=p))
Message with coordinates: (0.50, 0.50)
>>> from wherever import DollarMessage as __
>>> print(__('Message with $num $what', num=2, what='placeholders'))
Message with 2 placeholders
>>>

```

Even though the samples above lean on `print()` to illustrate the formatting, you'd naturally reach for `logger.debug()` or the like to do the actual logging via this technique.

Worth flagging is that this technique costs you no real performance hit: the formatting itself fires not at the moment you issue the logging call, but later, when (and only if) a handler is genuinely on the verge of emitting the logged message to a log. Thus the lone faintly odd detail that could catch you off guard is that the parentheses enclose both the format string and the arguments together, not the format string alone. The reason is that the __ notation amounts to nothing more than syntactic sugar for a constructor call against one of the `*XXX*Message` classes.

[Subject index](INDEX.md) · [Formatter style and logging-call interpolation contracts](formatter-style-and-logging-call-interpolation-contracts.md) · [LoggerAdapter alternative-style implementation](loggeradapter-alternative-style-implementation.md) · [Previous source context](formatter-style-and-logging-call-interpolation-contracts.md) · [Following source context](loggeradapter-alternative-style-implementation.md)

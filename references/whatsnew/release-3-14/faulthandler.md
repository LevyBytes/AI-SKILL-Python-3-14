# What's new in Python 3.14 / faulthandler - faulthandler

### faulthandler

- Printing the C stack trace is now supported on platforms that [support it](https://docs.python.org/3.14/library/faulthandler.html#c-stack-compatibility), either through the new [`dump_c_stack()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.dump_c_stack) function or by way of the *c_stack* argument within [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable). (Contributed by Peter Bierma in [gh-127604](https://github.com/python/cpython/issues/127604).)

[Subject index](INDEX.md) · [Previous source section](errno.md) · [Next source section](fnmatch.md) · [Release/subject declaration](summary-release-highlights.md)

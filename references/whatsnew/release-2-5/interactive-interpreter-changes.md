# What's New in Python 2.5 / Interactive Interpreter Changes

### Interactive Interpreter Changes

Within the interactive interpreter, `quit` and `exit` have for a long time been strings, giving newcomers a moderately useful hint when they attempt to leave:

```python
>>> quit
'Use Ctrl-D (i.e. EOF) to exit.'

```

Under Python 2.5, `quit` and `exit` become objects that still render string representations of themselves yet are additionally callable. Beginners who type `quit()` or `exit()` will now leave the interpreter just as they assume. (Implemented by Georg Brandl.)

The Python executable now recognizes the conventional long options [`--help`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-help) and [`--version`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-version); under Windows it additionally honors the [`/?`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-0) option to print a help message. (Implemented by Georg Brandl.)

[Subject index](INDEX.md) · [Previous source section](other-language-changes-c.md) · [Next source section](optimizations.md) · [Release/subject declaration](pep-308-conditional-expressions.md)

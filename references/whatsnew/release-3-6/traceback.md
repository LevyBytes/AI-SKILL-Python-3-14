# What's New In Python 3.6 / traceback

### traceback

Lengthy stretches of identical lines inside tracebacks are now condensed by both the traceback module and the interpreter's built-in exception display, illustrated by the example below:

```python
>>> def f(): f()
...
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded

```

(Contributed by Emanuel Barry in [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)

[Subject index](INDEX.md) · [Previous source section](tkinter.md) · [Next source section](tracemalloc.md) · [Release/subject declaration](summary-release-highlights.md)

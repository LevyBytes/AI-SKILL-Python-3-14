# 10.4. Error output redirection and program termination

### 10.4. Error output redirection and program termination

Attributes for *stdin*, *stdout*, and *stderr* are likewise present on the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module. That last one is handy for pushing out warnings and error text so they stay visible even after *stdout* gets redirected:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one

```

Reaching for `sys.exit()` is the simplest route to halting a script.

[Subject index](INDEX.md) · [Previous source section](command-line-arguments.md) · [Following source section](string-pattern-matching.md)

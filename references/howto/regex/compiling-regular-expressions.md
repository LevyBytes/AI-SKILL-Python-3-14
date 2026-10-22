# Compiling regular expressions

### Compiling regular expressions

A regular expression compiles into a pattern object, which carries methods for tasks such as hunting for pattern matches or doing string substitutions.

```python
>>> import re
>>> p = re.compile('ab*')
>>> p
re.compile('ab*')

```

[`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) will additionally take an optional *flags* argument, which switches on assorted special behaviors and syntax tweaks. The full set of settings comes up further along, but one quick example suffices for now:

```python
>>> p = re.compile('ab*', re.IGNORECASE)

```

You hand the RE to [`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) as a string. REs live as strings because regular expressions are not built into the core Python language, and no dedicated syntax was invented for them. (Plenty of applications never touch REs, so there is no reason to swell the language specification by baking them in.) Rather, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module is just a C extension module bundled with Python, in the same way the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) or [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) modules are.

Holding REs inside strings leaves the Python language tidier, though it brings a single drawback, which the following section takes up.

[Subject index](INDEX.md) · [Previous source context](using-regular-expressions.md) · [Following source context](the-backslash-plague.md)

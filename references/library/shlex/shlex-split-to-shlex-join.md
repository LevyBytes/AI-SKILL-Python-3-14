# shlex: `shlex.split()`, `shlex.join()`

# Shlex

### `shlex` - Simple lexical analysis

**Source code:** [Lib/shlex.py](https://github.com/python/cpython/tree/3.14/Lib/shlex.py)

---

With the `shlex` class you can readily build lexical analyzers for straightforward grammars that mimic the Unix shell. It comes in handy when designing minilanguages (such as the run control files used by Python programs) or when interpreting strings that contain quoting.

These are the functions exported by the `shlex` module:

`shlex.split(*s*, *comments=False*, *posix=True*)`

Break apart the string *s* using shell-style rules. When *comments* keeps its [`False`](https://docs.python.org/3.14/library/constants.html#False) default, comment handling within the supplied text is switched off (which sets the `commenters` attribute on the `shlex` instance to an empty string). By default the call runs under POSIX mode, switching to non-POSIX behavior whenever the *posix* argument is given as false.

Changed in version 3.12: Supplying `None` as the *s* argument now triggers an exception instead of falling back to reading [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin).

`shlex.join(*split_command*)`

Join together the items of the *split_command* list into a single string. It performs the reverse operation of `split()`.

```python
>>> from shlex import join
>>> print(join(['echo', '-n', 'Multiple words']))
echo -n 'Multiple words'

```

Its result is shell-escaped, which guards you against injection attacks (refer to `quote()`).

Added in version 3.8.

[Subject index](INDEX.md) · [Continue](shlex-quote.md)

# What’s New in Python 2.0 / Changes to Built-in Functions - sys

### Changes to Built-in Functions

There’s a new built-in, `zip(seq1, seq2, ...)`. [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) hands back a list of tuples, with each tuple holding the i-th item drawn from each of the supplied sequences. Where `zip()` and `map(None, seq1, seq2)` differ is that [`map()`](https://docs.python.org/3.14/library/functions.html#map) fills shorter sequences out with `None` when they aren’t all equal in length, whereas `zip()` trims the returned list down to the length of the shortest sequence passed in.

The [`int()`](https://docs.python.org/3.14/library/functions.html#int) and `long()` functions will now take an optional “base” argument whenever the first argument is a string. `int('123', 10)` gives back 123, and `int('123', 16)` gives back 291. `int(123, 16)` throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception carrying the message “can’t convert non-string with explicit base”.

The [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module gains a new variable that carries fuller version information. `sys.version_info` is a tuple `(major, minor, micro, level, serial)` So, for instance, in an imaginary 2.0.1beta1, `sys.version_info` would read `(2, 0, 1, 'beta', 1)`. *level* is a string like `"alpha"`, `"beta"`, or `"final"` for a final release.

Dictionaries pick up a peculiar new method, `setdefault(key, default)`, which works much like the existing `get()` method. The difference is that when the key isn’t present, `setdefault()` both hands back the value of *default* the way `get()` would, and stores it in the dictionary as the value associated with *key*. So these lines:

```python
if dict.has_key( key ): return dict[key]
else:
    dict[key] = []
    return dict[key]

```

collapse into one `return dict.setdefault(key, [])` statement.

To trap runaway recursion before it fills the C stack and triggers a core dump or GPF, the interpreter enforces a ceiling on recursion depth. That ceiling used to be baked in at compile time, but under 2.0 the recursion-depth ceiling can be queried and changed through [`sys.getrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit) and [`sys.setrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit). It defaults to 1000, and you can estimate a workable ceiling for any given platform by running the new `Misc/find_recursionlimit.py` script.

[Subject index](INDEX.md) · [Previous source section](minor-language-changes.md) · [Next source section](porting-to-2-0.md) · [Release/subject declaration](introduction.md)

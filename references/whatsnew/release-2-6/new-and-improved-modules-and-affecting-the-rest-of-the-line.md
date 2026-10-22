# What’s New in Python 2.6 / New and Improved Modules — curses, datetime, decimal, difflib, ftplib, functools, getpass, glob, heapq, http.cookies

```python
>>> from collections import deque
>>> dq=deque(maxlen=3)
>>> dq
deque([], maxlen=3)
>>> dq.append(1); dq.append(2); dq.append(3)
>>> dq
deque([1, 2, 3], maxlen=3)
>>> dq.append(4)
>>> dq
deque([2, 3, 4], maxlen=3)

```

(Contributed by Raymond Hettinger.)

- [`Morsel`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel) objects from the [`Cookie`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies) module now carry an [`httponly`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.httponly) attribute. On certain browsers, JavaScript code cannot read or alter cookies that have this attribute turned on. (Contributed by Arvin Schnell; [bpo-1638033](https://bugs.python.org/issue?@action=redirect&bpo=1638033).)

- The [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module offers a new window method, `chgat()`, that alters the display attributes for some count of characters on one line. (Contributed by Fabian Kreutz.)

```python
# Boldface text starting at y=0,x=21
# and affecting the rest of the line.
stdscr.chgat(0, 21, curses.A_BOLD)

```

The `Textbox` class from the [`curses.textpad`](https://docs.python.org/3.14/library/curses.html#module-curses.textpad) module now permits editing in insert mode on top of overwrite mode. You switch insert mode on by passing a true value for the *insert_mode* parameter when you build the `Textbox` instance.

- The `strftime()` methods of the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module now recognize a `%f` format code that expands into the object’s microsecond count, left-padded with zeros to six digits. (Contributed by Skip Montanaro; [bpo-1158](https://bugs.python.org/issue?@action=redirect&bpo=1158).)

- The [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module was brought up to version 1.66 of [the General Decimal Specification](https://speleotrove.com/decimal/decarith.html). Among the new capabilities are methods for a few basic mathematical functions such as `exp()` and `log10()`:

```python
>>> Decimal(1).exp()
Decimal("2.718281828459045235360287471")
>>> Decimal("2.7182818").ln()
Decimal("0.9999999895305022877376682436")
>>> Decimal(1000).log10()
Decimal("3")

```

The `as_tuple()` method on `Decimal` objects now hands back a named tuple holding `sign`, `digits`, and `exponent` fields.

(Implemented by Facundo Batista together with Mark Dickinson. Raymond Hettinger added the named tuple support.)

- The `SequenceMatcher` class in the [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module now hands back named tuples standing for matches, sporting `a`, `b`, and `size` attributes. (Contributed by Raymond Hettinger.)

- An optional `timeout` parameter, expressed as a number of seconds, was wired into the [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) class constructor and likewise into the `connect()` method. (Added by Facundo Batista.) Beyond that, the `FTP` class’s `storbinary()` and `storlines()` now accept an optional *callback* parameter invoked with each block of data once that data has gone out. (Contributed by Phil Schwartz; [bpo-1221598](https://bugs.python.org/issue?@action=redirect&bpo=1221598).)

- The `reduce()` built-in function can also be reached from the [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module. Under Python 3.0 the builtin goes away and `reduce()` is reachable solely through `functools`; for now there is no intention of removing the builtin throughout the 2.x line. (Patched by Christian Heimes; [bpo-1739906](https://bugs.python.org/issue?@action=redirect&bpo=1739906).)

- Where it can, the [`getpass`](https://docs.python.org/3.14/library/getpass.html#module-getpass) module will now reach for `/dev/tty` to display the prompt and collect the password, dropping back to standard error and standard input otherwise. Should there be a chance the password gets echoed to the terminal, a warning appears ahead of the prompt. (Contributed by Gregory P. Smith.)

- The [`glob.glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob) function is now able to hand back Unicode filenames when a Unicode path was passed in and Unicode filenames turn up inside the directory. ([bpo-1001604](https://bugs.python.org/issue?@action=redirect&bpo=1001604))

- The [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module gained a new function, `merge(iter1, iter2, ...)`, which accepts any number of iterables that yield data already in sorted order, and produces a new generator yielding the combined contents of all those iterators, still in sorted order. As an example:

[Subject index](INDEX.md) · [Previous source section](standard-library-module-changes.md) · [Next source section](heapq-through-itertools-module-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md)

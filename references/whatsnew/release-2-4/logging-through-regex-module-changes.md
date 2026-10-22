# What’s New in Python 2.4 / New, Improved, and Deprecated Modules — email, email.utils, gettext, logging, marshal, operator, optparse, os, poplib, posix, profile, random, re

```python
import logging
logging.basicConfig(filename='/var/log/application.log',
    level=0,  # Log all messages
    format='%(levelname):%(process):%(thread):%(message)')

```

The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package picked up further additions too: a handy `log(level, msg)` method plus a `TimedRotatingFileHandler` class whose log files roll over on a scheduled interval. A `RotatingFileHandler` was already present, cycling logs the moment a file grew past a set size. Each of these classes now descends from a freshly introduced `BaseRotatingHandler` class, which you can lean on to build rotating handlers of your own.

(Changes implemented by Vinay Sajip.)

- As it unpacks a data structure, the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) module now reuses interned strings. That can trim certain pickle strings, though where it really tells is in cutting `.pyc` files down to a markedly smaller size. (Contributed by Martin von Löwis.)

- Over in the `nntplib` module, the `NNTP` class picked up `description()` and `descriptions()` methods for pulling newsgroup descriptions, whether for one group alone or across a span of them. (Contributed by Jürgen A. Erhard.)

- A pair of fresh functions joined the [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module: `attrgetter(attr)` and `itemgetter(index)`. Each hands you a callable that, given one argument, yields the matching attribute or item; such callables shine as data extractors paired with [`map()`](https://docs.python.org/3.14/library/functions.html#map) or [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted). To illustrate:

```python
>>> L = [('c', 2), ('d', 1), ('a', 4), ('b', 3)]
>>> map(operator.itemgetter(0), L)
['c', 'd', 'a', 'b']
>>> map(operator.itemgetter(1), L)
[2, 1, 4, 3]
>>> sorted(L, key=operator.itemgetter(1)) # Sort list by second tuple item
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

```

(Contributed by Raymond Hettinger.)

- Several refinements landed in the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module. Its messages now run through [`gettext.gettext()`](https://docs.python.org/3.14/library/gettext.html#gettext.gettext), so Optik's help and error text can be internationalized. An option's help message may now embed the string `'%default'`, which gets swapped out for that option's default value. (Contributed by Greg Ward.)

- Down the road the intent is to retire the `rfc822` module in some later Python release, handing its role to the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package. With that goal in view, the [`email.Utils.formatdate`](https://docs.python.org/3.14/library/email.utils.html#email.utils.formatdate) function was reworked so it can stand in for `rfc822.formatdate()`. Fresh e-mail handling code is best written with this shift in mind. (Change implemented by Anthony Baxter.)

- The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module gained a `urandom(n)` function that yields a string holding *n* bytes of random data. Through it you tap into whatever randomness source the platform offers — `/dev/urandom` on Linux, say, or the Windows CryptoAPI. (Contributed by Trevor Perrin.)

- One more new function: `os.path.lexists(path)` reports true when the file at *path* is present, symbolic link or not. That sets it apart from the existing `os.path.exists(path)`, which comes back false should *path* be a symlink aimed at a target that isn't there. (Contributed by Beni Cherniavsky.)

- A `getsid()` function now appears in the [`posix`](https://docs.python.org/3.14/library/posix.html#module-posix) module sitting beneath the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module. (Contributed by J. Raynor.)

- POP over SSL is now handled by the [`poplib`](https://docs.python.org/3.14/library/poplib.html#module-poplib) module. (Contributed by Hector Urtubia.)

- C extension functions can now be profiled by the [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile) module. (Contributed by Nick Bastin.)

- A fresh method named `getrandbits(N)`, returning a long integer that spans *N* bits, now lives in the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module. Where it fits, the established `randrange()` method draws on `getrandbits()`, which makes turning out arbitrarily large random numbers run more efficiently. (Contributed by Raymond Hettinger.)

- The regular-expression syntax the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module understands grew to include basic conditional expressions, spelled `(?(group)A|B)`. Here *group* may be a numeric group ID or a group name set up earlier via `(?P<group>...)`. Should that group have matched, pattern *A* is tried against the string; otherwise pattern *B* takes its place. (Contributed by Gustavo Niemeyer.)

- On top of that, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module has shed its recursion, the fruit of an enormous effort by Gustavo Niemeyer. Within a recursive regular-expression engine, some patterns burn through a great deal of C stack, opening the door to a stack overflow. Match a 30000-byte run of `a` characters against `(a|b)+`, for instance, and every single character ate one stack frame. Python 2.3 attempted to catch such overflows and throw a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception, but a few patterns slipped past that guard, and with bad luck Python might segfault. The 2.4 regular-expression engine copes with that pattern without trouble.

-

[Subject index](INDEX.md) · [Next source section](signal-through-xmlrpc-module-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](new-improved-and-deprecated-modules.md) · [Preceding release/subject continuation](logging-basicconfig-keywords.md)

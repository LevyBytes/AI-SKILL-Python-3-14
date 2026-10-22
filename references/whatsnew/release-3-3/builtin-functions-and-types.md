# What's New In Python 3.3 / Builtin functions and types — os

### Builtin functions and types

- [`open()`](https://docs.python.org/3.14/library/functions.html#open) gains a new *opener* parameter: the file object’s backing file descriptor is then produced by invoking *opener* with (*file*, *flags*). Doing so lets you apply custom flags, for instance [`os.O_CLOEXEC`](https://docs.python.org/3.14/library/os.html#os.O_CLOEXEC). The `'x'` mode also arrived: open for exclusive creation, failing if the file already exists.

- [`print()`](https://docs.python.org/3.14/library/functions.html#print): a *flush* keyword argument is now available. Should that *flush* keyword argument hold a true value, flushing of the stream happens forcibly.

- [`hash()`](https://docs.python.org/3.14/library/functions.html#hash): hash randomization is enabled by default, see [`object.__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) and [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED).

- A new [`casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold) method joins the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type: it hands back a casefolded duplicate of the string, and such casefolded strings serve caseless matching. To illustrate, `'ß'.casefold()` returns `'ss'`.

- The sequence documentation got a thorough rewrite that clarifies the binary versus text sequence split and adds dedicated documentation sections covering each individual builtin sequence type ([bpo-4966](https://bugs.python.org/issue?@action=redirect&bpo=4966)).

[Subject index](INDEX.md) · [Previous source section](a-finer-grained-import-lock.md) · [Next source section](faulthandler.md) · [Release/subject declaration](summary-release-highlights.md)

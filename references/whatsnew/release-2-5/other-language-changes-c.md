# Python 2.5 changes: Unicode comparisons and warning behavior

Python now issues a fresh warning, [`UnicodeWarning`](https://docs.python.org/3.14/library/exceptions.html#UnicodeWarning), whenever you compare a Unicode string against an 8-bit string that the default ASCII encoding cannot turn into Unicode. Such a comparison evaluates to false:

```python
>>> chr(128) == unichr(128)   # Can't convert chr(128) to Unicode
__main__:1: UnicodeWarning: Unicode equal comparison failed
  to convert both arguments to Unicode - interpreting them
  as being unequal
False
>>> chr(127) == unichr(127)   # chr(127) can be converted
True

```

In earlier releases this raised a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) exception, yet under 2.5 that behavior could lead to baffling failures during dictionary access. Suppose `chr(128)` served as a key and you queried `unichr(128)`; the lookup would surface a `UnicodeDecodeError` exception. The dictionary implementation in `dictobject.c` previously swallowed this exception, but other 2.5 changes caused it to propagate instead.

Treating such a comparison as an error is technically the right call, but doing so risked breaking existing programs, so [`UnicodeWarning`](https://docs.python.org/3.14/library/exceptions.html#UnicodeWarning) was added as a gentler alternative.

(Implemented by Marc-Andr?? Lemburg.)

- A common slip among Python programmers is leaving out the `__init__.py` module from a package directory. Tracking down this oversight can be bewildering and often means rerunning Python with the [`-v`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-v) switch to record every path that was searched. Python 2.5 adds a new [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning) warning that fires when an import would have treated a directory as a package even though no `__init__.py` was present. By default the warning stays quiet; pass the [`-Wd`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) option when launching the Python executable to surface the warning message. (Implemented by Thomas Wouters.)

- A class definition may now list no base classes at all. For instance, the following is now valid:

```python
class C():
    pass

```

(Implemented by Brett Cannon.)

[Subject index](INDEX.md) · [Next source section](interactive-interpreter-changes.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Release/subject declaration](other-language-changes-zerodict-and-is-image-file.md) · [Preceding release/subject continuation](other-language-changes-zerodict-and-is-image-file.md)

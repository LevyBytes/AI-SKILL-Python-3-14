# What’s New in Python 2.1 / Other Changes and Fixes - readline, string, sys

### Other Changes and Fixes

Thanks to the compressed release cycle, Python 2.1 saw comparatively few of the smaller changes. Combing the CVS change logs surfaces 117 patches landed and 136 bugs squashed, though both numbers are probably on the low side. A few of the more striking changes follow:

- An optional purpose-built object allocator is now on offer, expected to outpace the system `malloc()` while carrying less memory overhead. It calls on C's `malloc()` to grab sizable pools of memory and then services smaller requests out of those pools. Turning it on is a matter of handing the `--with-pymalloc` option to the **configure** script; the implementation specifics sit in `Objects/obmalloc.c`.

Anyone writing C extension modules ought to exercise their code with the object allocator switched on, since certain faulty code can break and dump core at runtime. Python's C API holds a fair number of memory allocation functions that until now were merely aliases for the C library's `malloc()` and `free()`, so calling mismatched ones by accident left no visible trace. Flip on the object allocator and those functions stop being aliases of `malloc()` and `free()`, so freeing memory with the wrong one earns you a core dump. If memory came from [`PyMem_New`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_New), for instance, it must be released through [`PyMem_Del()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Del) rather than `free()`. A handful of modules bundled with Python stumbled here and needed fixing, and no doubt further third-party modules will run into the same trap.

The object allocator was contributed by Vladimir Marangozov.

- Line-oriented file I/O got quicker, prompted both by the steady complaints about its sluggishness and by its frequent role as a naïve benchmark. To that end, the [`readline()`](https://docs.python.org/3.14/library/readline.html#module-readline) method on file objects was rewritten for far greater speed. How big the gain turns out to be shifts from platform to platform according to how slow the C library's `getc()` happened to be, but it sits near 66% and may run considerably higher on certain operating systems. Spurred by a thread on comp.lang.python, Tim Peters handled much of the benchmarking and coding behind the change.

Jeff Epler contributed a new module along with a new method for file objects. That method, `xreadlines()`, parallels the `xrange()` built-in already in place. `xreadlines()` gives back an opaque sequence object you can only iterate over, pulling one line per iteration instead of slurping the whole file into memory the way the existing `readlines()` method does. Here's how you'd put it to work:

```python
for line in sys.stdin.xreadlines():
    # ... do something for each line ...
    ...

```

For a deeper treatment of the line I/O changes, turn to the python-dev summary covering January 1–15, 2001 at [https://mail.python.org/pipermail/python-dev/2001-January/](https://mail.python.org/pipermail/python-dev/2001-January/).

- Dictionaries gained a new method, [`popitem()`](https://docs.python.org/3.14/library/stdtypes.html#dict.popitem), which lets you walk destructively through a dictionary's contents; for big dictionaries this can run faster, since you skip building a list of every key or value. `D.popitem()` pulls some arbitrary `(key, value)` pair out of dictionary `D` and hands it back as a 2-tuple. Tim Peters and Guido van Rossum did most of the implementing, following a suggestion and an early patch from Moshe Zadka.

- A module can now dictate which names `from module import *` brings in, by setting an `__all__` attribute that holds the list of names to import. A frequent gripe is that when the module itself imports others — [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) or [`string`](https://docs.python.org/3.14/library/string.html#module-string), say — `from module import *` drags those into the importing module's namespace too. The cure is simply to enumerate the public names in `__all__`:

```python
# List public names
__all__ = ['Database', 'open']

```

Ben Wolfson originally proposed and built a stricter form of this patch, but following some discussion on python-dev a softer final version is what got committed.

- Calling [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) on strings used to render non-printable characters with octal escapes — a newline, for instance, showed up as `'\012'`. That was a leftover echo of Python's C lineage, yet octal carries almost no practical value nowadays. Ka-Ping Yee proposed swapping the octal escapes for hex ones and using the `\n`, `\t`, `\r` escapes where they fit, and he built this new formatting.

- A syntax error caught at compile-time can now throw an exception that carries the error's filename and line number — a welcome by-product of Jeremy Hylton's compiler reorganization.

- C extensions that import other modules have been reworked to go through [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule), so they'll now respect whatever import hooks happen to be installed. The same approach is recommended for third-party extensions that have to import another module from C code.

- Fredrik Lundh trimmed a further 340K off the Unicode character database's footprint.

- Several fresh ports arrived. Steven Majewski handled the one for MacOS X; the Cygwin work came from Jason Tishler; Dietmar Schwertberger took on RISCOS; and Billy G. Allie produced the Unixware 7 port.

Beyond that sits the customary assortment of small bugfixes, small memory leaks, docstring touch-ups, and other adjustments — far too many to bother listing out; consult the CVS logs if you want every detail.

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules.md) · [Release/subject declaration](introduction.md)

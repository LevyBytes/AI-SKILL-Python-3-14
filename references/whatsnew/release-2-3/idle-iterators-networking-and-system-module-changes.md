# What’s New in Python 2.3 / New, Improved, and Deprecated Modules — idle, imaplib, itertools, math, optparse, os, platform, posix, pyexpat, random, time

```python
>>> import heapq
>>> heap = []
>>> for item in [3, 7, 5, 11, 1]:
...    heapq.heappush(heap, item)
...
>>> heap
[1, 3, 5, 11, 7]
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
3
>>> heap
[5, 7, 11]

```

(Contributed by Kevin O'Connor.)

- The IDLE integrated development environment was refreshed using code drawn from the IDLEfork project ([https://idlefork.sourceforge.net](https://idlefork.sourceforge.net)). Its standout feature is that the code under development now runs inside a subprocess, so manual `reload()` operations are no longer required. IDLE's core code has been folded into the standard library as the [`idlelib`](https://docs.python.org/3.14/library/idle.html#module-idlelib) package.

- The [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module now handles IMAP over SSL. (Contributed by Piers Lauder and Tino Lange.)

- The [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) holds a number of handy functions for working with iterators, drawing inspiration from various functions found in the ML and Haskell languages. For instance, `itertools.ifilter(predicate, iterator)` yields every element in the iterator for which the function `predicate()` returns [`True`](https://docs.python.org/3.14/library/constants.html#True), and `itertools.repeat(obj, N)` yields `obj` *N* times. The module holds several other functions as well; refer to the package's reference documentation for the specifics. (Contributed by Raymond Hettinger.)

- Two fresh functions in the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module, `degrees(rads)` and `radians(degs)`, translate between radians and degrees. Other `math` module functions like [`math.sin()`](https://docs.python.org/3.14/library/math.html#math.sin) and [`math.cos()`](https://docs.python.org/3.14/library/math.html#math.cos) have always expected their inputs in radians. In addition, an optional *base* argument was given to [`math.log()`](https://docs.python.org/3.14/library/math.html#math.log) so that computing logarithms in bases other than `e` and `10` is easier. (Contributed by Raymond Hettinger.)

- A handful of new POSIX functions (`getpgid()`, `killpg()`, `lchown()`, `loadavg()`, `major()`, `makedev()`, `minor()`, and `mknod()`) were appended to the [`posix`](https://docs.python.org/3.14/library/posix.html#module-posix) module that sits beneath the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module. (Contributed by Gustavo Niemeyer, Geert Jansen, and Denis S. Otkidach.)

- Within the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module, the `*stat()` group of functions is now able to record sub-second fractions inside a timestamp. These time stamps are given as floats, much like the value [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) returns.

Testing revealed that certain applications break when time stamps are floats. To preserve compatibility, the tuple interface of [`stat_result`](https://docs.python.org/3.14/library/os.html#os.stat_result) reports time stamps as integers. With named fields (a capability that arrived first in Python 2.2), time stamps still come through as integers, unless `os.stat_float_times()` is called to switch on float return values:

```python
>>> os.stat("/tmp").st_mtime
1034791200
>>> os.stat_float_times(True)
>>> os.stat("/tmp").st_mtime
1034791200.6335014

```

Starting in Python 2.4, the default will switch to always handing back floats.

Application authors should turn this feature on only when all of their libraries behave correctly in the face of floating-point time stamps, or when they rely on the tuple API. When in use, the feature ought to be switched on at the application level rather than attempting to toggle it on a per-use basis.

- The [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module supplies a new parser for command-line arguments that can coerce option values into a specific Python type and will generate a usage message automatically. Refer to the next section for further details.

- The aging and never-documented `linuxaudiodev` module has been deprecated, and a replacement called `ossaudiodev` has been introduced. The rename happened because the OSS sound drivers run on platforms beyond Linux, and the interface was also cleaned up and modernized in several respects. (Contributed by Greg Ward and Nicholas FitzRoy-Dale.)

- The new [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) module bundles a number of functions that attempt to figure out various characteristics of the platform you are running on. Functions exist to fetch the machine architecture, the CPU type, which Windows OS version is running, and even the version of the Linux distribution. (Contributed by Marc-Andr?? Lemburg.)

- The parser objects from the [`pyexpat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) module can now optionally buffer character data, which cuts down the number of calls to your character data handler and thereby speeds things up. Set the parser object's [`buffer_text`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text) attribute to [`True`](https://docs.python.org/3.14/library/constants.html#True) to switch on buffering.

- The `sample(population, k)` function was introduced into the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module. *population* is a sequence or `xrange` object holding the members of a population, and [`sample()`](https://docs.python.org/3.14/library/random.html#random.sample) picks *k* members from the population without putting chosen ones back. *k* may be any value up to `len(population)`. For instance:

[Subject index](INDEX.md) · [Previous source section](standard-library-module-changes.md) · [Next source section](random-through-textwrap-module-changes.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](standard-library-module-changes.md)

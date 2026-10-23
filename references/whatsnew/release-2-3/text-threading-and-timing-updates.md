# What’s New in Python 2.3 / New, Improved, and Deprecated Modules - textwrap, threading, time, timeit

```python
>>> import textwrap
>>> paragraph = "Not a whit, we defy augury: ... more text ..."
>>> textwrap.wrap(paragraph, 60)
["Not a whit, we defy augury: there's a special providence in",
 "the fall of a sparrow. If it be now, 'tis not to come; if it",
 ...]
>>> print textwrap.fill(paragraph, 35)
Not a whit, we defy augury: there's
a special providence in the fall of
a sparrow. If it be now, 'tis not
to come; if it be not to come, it
will be now; if it be not now, yet
it will come: the readiness is all.
>>>

```

The module additionally provides a [`TextWrapper`](https://docs.python.org/3.14/library/textwrap.html#textwrap.TextWrapper) class that actually carries out the text wrapping strategy. The `TextWrapper` class together with the [`wrap()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.wrap) and [`fill()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.fill) functions accept a number of extra keyword arguments for fine-tuning the formatting; see the module's documentation for the specifics. (Contributed by Greg Ward.)

- The `thread` and [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) modules are now joined by companion modules, `dummy_thread` and `dummy_threading`, which provide a do-nothing implementation of the `thread` module's interface for platforms lacking thread support. The goal is to make thread-aware modules (the ones that *don't* depend on threads to operate) simpler by placing the following code at the top:

```python
try:
    import threading as _threading
except ImportError:
    import dummy_threading as _threading

```

In this case, `_threading` serves as the module name to signal that the module in play is not necessarily the real [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module. Code can invoke functions and use classes in `_threading` regardless of whether threads are supported, sidestepping an [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement and making the code a bit cleaner. This module will not magically run multithreaded code without threads; code that waits on another thread to return or to act will simply hang forever.

- The [`strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) function in the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module has long been a source of irritation because it leans on the platform C library's `strptime()` implementation, and various platforms occasionally carry strange bugs. Brett Cannon contributed a portable implementation written in pure Python that ought to behave the same everywhere.

- The new [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module assists in gauging how long fragments of Python code take to run. You can run the `timeit.py` file straight from the command line, or import the module's [`Timer`](https://docs.python.org/3.14/library/timeit.html#timeit.Timer) class and use it directly. Here is a brief example that works out whether converting an 8-bit string to Unicode is faster by tacking an empty Unicode string onto it or by calling the `unicode()` function:

```python
import timeit

timer1 = timeit.Timer('unicode("abc")')
timer2 = timeit.Timer('"abc" + u""')

# Run three trials
print timer1.repeat(repeat=3, number=100000)
print timer2.repeat(repeat=3, number=100000)

# On my laptop this outputs:
# [0.36831796169281006, 0.37441694736480713, 0.35304892063140869]
# [0.17574405670166016, 0.18193507194519043, 0.17565798759460449]

```

- The `Tix` module received an assortment of bug fixes and updates for the current release of the Tix package.

- The `Tkinter` module now operates with a thread-enabled build of Tcl. Tcl's threading model demands that widgets be touched only from the thread that created them; accessing them from another thread can make Tcl panic. For certain Tcl interfaces, `Tkinter` will now sidestep this automatically when a widget is reached from a different thread by marshalling a command, handing it to the proper thread, and waiting for the outcome. The remaining interfaces resist automatic handling, yet `Tkinter` will now throw an exception when such an access occurs, so you at the very least learn that the problem exists. See [https://mail.python.org/pipermail/python-dev/2002-December/031107.html](https://mail.python.org/pipermail/python-dev/2002-December/031107.html) for a fuller account of why this changed. (Implemented by Martin von Löwis.)

- Invoking Tcl methods by way of `_tkinter` no longer returns strings alone. Instead, when Tcl returns other objects, those objects are turned into their Python equivalent, if one exists, or wrapped in a `_tkinter.Tcl_Obj` object when no Python equivalent is available. You can govern this behavior through the `wantobjects()` method of `tkapp` objects.

When `_tkinter` is used by way of the `Tkinter` module (as the bulk of Tkinter applications will), this feature is always switched on. It should not introduce compatibility issues, since Tkinter would always turn string results into Python types where possible.

[Subject index](INDEX.md) · [Previous source section](random-through-textwrap-module-changes.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](standard-library-module-changes.md) · [Following release/subject continuation](tkinter-shelve-and-dom-compatibility.md)

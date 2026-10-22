# What’s New in Python 2.6 / New and Improved Modules — textwrap, threading, timeit, turtle

```python
with test_support.TransientResource(IOError,
                                errno=errno.ETIMEDOUT):
    f = urllib.urlopen('https://sf.net')
    ...

```

Lastly, `check_warnings()` clears the `warning` module's warning filters and returns an object that captures every warning message that fires ([bpo-3781](https://bugs.python.org/issue?@action=redirect&bpo=3781)):

```python
with test_support.check_warnings() as wrec:
    warnings.simplefilter("always")
    # ... code that triggers a warning ...
    assert str(wrec.message) == "function is outdated"
    assert len(wrec.warnings) == 1, "Multiple warnings raised"

```

(Contributed by Brett Cannon.)

- By passing `drop_whitespace=False` as an argument, you can now have the [`textwrap`](https://docs.python.org/3.14/library/textwrap.html#module-textwrap) module keep whatever whitespace already sits at the start and end of the freshly produced lines:

```python
>>> S = """This  sentence  has a bunch   of
...   extra   whitespace."""
>>> print textwrap.fill(S, width=15)
This  sentence
has a bunch
of    extra
whitespace.
>>> print textwrap.fill(S, drop_whitespace=False, width=15)
This  sentence
  has a bunch
   of    extra
   whitespace.
>>>

```

(Contributed by Dwayne Bailey; [bpo-1581073](https://bugs.python.org/issue?@action=redirect&bpo=1581073).)

- The API of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module is shifting toward properties like `daemon` rather than the `setDaemon()` and `isDaemon()` methods, and several methods were renamed to favor underscores over camel-case; the `activeCount()` method, for one, becomes `active_count()`. The 2.6 and 3.0 editions of the module both carry the same properties and renamed methods, yet keep the old methods around. No timeline exists for deprecating the old APIs in Python 3.x, and they won't disappear in any 2.x release. (Carried out by several people, most notably Benjamin Peterson.)

`Thread` objects in the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module gained an `ident` property reporting the thread's identifier, a nonzero integer. (Contributed by Gregory P. Smith; [bpo-2871](https://bugs.python.org/issue?@action=redirect&bpo=2871).)

- For the statement under timing and for the setup code alike, the [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module now takes callables in addition to strings. Two convenience functions arrived for building `Timer` instances: `repeat(stmt, setup, time, repeat, number)` and `timeit(stmt, setup, time, number)` each build an instance and invoke the matching method. (Contributed by Erik Demaine; [bpo-1533909](https://bugs.python.org/issue?@action=redirect&bpo=1533909).)

- The `Tkinter` module now takes lists and tuples for options, splitting the elements with spaces before the resulting value reaches Tcl/Tk. (Contributed by Guilherme Polo; [bpo-2906](https://bugs.python.org/issue?@action=redirect&bpo=2906).)

- Gregor Lingl substantially expanded the [`turtle`](https://docs.python.org/3.14/library/turtle.html#module-turtle) module for turtle graphics. The module's new capabilities include:

  - Smoother animation as the turtle moves and turns.

  - Steering turtle movement through the new `delay()`, `tracer()`, and `speed()` methods.

  - The means to assign fresh shapes to the turtle and to lay out a new coordinate system.

  - Turtles now carry an `undo()` method capable of rolling back actions.

  - Basic support for responding to input events like mouse and keyboard activity, which makes writing simple games feasible.

  -

[Subject index](INDEX.md) · [Previous source section](signal-wakeup-and-network-module-changes.md) · [Next source section](turtle-unicode-url-warning-and-xmlrpc-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](attribute-lookup-and-process-module-changes.md)

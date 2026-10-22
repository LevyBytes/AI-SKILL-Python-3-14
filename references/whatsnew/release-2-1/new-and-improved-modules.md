# What’s New in Python 2.1 / New and Improved Modules — curses.panel, difflib, doctest, ftplib, profile, socket, sys, time, xml

### New and Improved Modules

- A pair of new modules came from Ka-Ping Yee: `inspect.py`, which pulls information about live Python code, and `pydoc.py`, which turns docstrings into HTML or text on the fly. On top of that, `Tools/scripts/pydoc` — installed automatically now — leans on `pydoc.py` to show documentation for any Python module, package, or class name you name. Running `pydoc xml.dom`, say, produces this:

```python
Python Library Documentation: package xml.dom in xml

NAME
    xml.dom - W3C Document Object Model implementation for Python.

FILE
    /usr/local/lib/python2.1/xml/dom/__init__.pyc

DESCRIPTION
    The Python mapping of the Document Object Model is documented in the
    Python Library Reference in the section on the xml.dom package.

    This package contains the following modules:
      ...

```

A Tk-based interactive help browser ships inside `pydoc` as well. `pydoc` has a way of becoming habit-forming fast, so give it a spin!

- A couple of separate unit-testing modules joined the standard library. From Tim Peters came the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module, a framework that runs the examples embedded in docstrings and checks their results against what was expected. Steve Purcell contributed PyUnit, a unit-testing framework modeled on JUnit — itself a port of Kent Beck's Smalltalk testing framework. Details about PyUnit live at [https://pyunit.sourceforge.net/](https://pyunit.sourceforge.net/).

- Inside the [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module sits a class called [`SequenceMatcher`](https://docs.python.org/3.14/library/difflib.html#difflib.SequenceMatcher) that takes two sequences and works out what edits would turn one into the other. With it you could, for instance, build a tool along the lines of the Unix **diff** program — and indeed the example program `Tools/scripts/ndiff.py` shows exactly how such a script gets written.

- Thomas Gellekum contributed [`curses.panel`](https://docs.python.org/3.14/library/curses.panel.html#module-curses.panel), which wraps the panel library found in ncurses and in SYSV curses. That panel library hands windows an extra dimension — depth. A window can be shifted up or down in the depth ordering, and the panel library works out where panels sit on top of one another and which portions remain visible.

- Several PyXML releases have shipped since Python 2.0, and the refreshed [`xml`](https://docs.python.org/3.14/library/xml.html#module-xml) package rides along in Python 2.1. Among the changes worth calling out are support for Expat 1.2 and newer, the capacity of Expat parsers to read files in any encoding Python knows, plus a range of bugfixes touching SAX, DOM, and the `minidom` module.

- Ping additionally supplied another hook, this one for dealing with exceptions that go uncaught. You can assign [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) any callable object. Whenever no [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)…[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) block catches an exception, that exception is routed to `sys.excepthook()`, which is then free to do as it pleases. Ping showed off one use for the hook at the Ninth Python Conference: producing an extended traceback that records not just the stack frames but also each frame's function arguments and local variables.

- A number of functions in the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module — [`asctime()`](https://docs.python.org/3.14/library/time.html#time.asctime) and [`localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime) among them — want a floating-point argument holding the time in seconds since the epoch. Since people most often call these against the current moment, that floating-point argument is now optional; leave it off and the current time fills in. Log file entries, for example, typically need a string of the current time, and in Python 2.1 a plain `time.asctime()` does the trick rather than the wordier `time.asctime(time.localtime(time.time()))` once demanded.

This change was proposed and implemented by Thomas Wouters.

- By default the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) module now fetches files in passive mode, which stands a better chance of working from behind a firewall. The push for this came out of the Debian bug tracking system, given that other Debian packages rely on `ftplib` to fetch files and then fail behind a firewall. The change is judged unlikely to trip anyone up, since Netscape also defaults to passive mode without drawing many complaints; still, if passive mode doesn't fit your application or network setup, call `set_pasv(0)` on FTP objects to switch it off.

- Grant Edwards contributed raw socket access, which now appears in the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module.

- A straightforward interactive statistics browser now lives in the [`pstats`](https://docs.python.org/3.14/library/profile.html#module-pstats) module; it shows timing profiles for Python programs and fires up when you run the module as a script. This came from Eric S. Raymond.

- A fresh implementation-specific function, `sys._getframe([depth])`, has arrived to pull a particular frame object out of the current call stack. Called bare, [`sys._getframe()`](https://docs.python.org/3.14/library/sys.html#sys._getframe) gives you the frame sitting at the top of the call stack; pass the optional integer *depth* and it instead returns the frame located *depth* calls down from that top. So `sys._getframe(1)`, for example, yields the caller's frame object.

You'll find this function in CPython alone — neither Jython nor the .NET implementation has it. Keep it to debugging, and don't give in to the urge to ship it in production code.

[Subject index](INDEX.md) · [Previous source section](pep-241-metadata-in-python-packages.md) · [Next source section](other-changes-and-fixes.md) · [Release/subject declaration](introduction.md)

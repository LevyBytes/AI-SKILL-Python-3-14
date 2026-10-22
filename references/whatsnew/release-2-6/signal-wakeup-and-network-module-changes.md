# What’s New in Python 2.6 / New and Improved Modules — signal, smtplib, socket, socketserver, sqlite3, struct, subprocess, sys, tarfile, tempfile, test

To take advantage of this, an event loop opens a pipe yielding two descriptors, one to read and one to write. The writable end is fed to `set_wakeup_fd()`, while the readable end joins the descriptors that the event loop watches through `select()` or `poll()`. When a signal lands, a byte gets written and the central event loop wakes, removing the need to poll.

(Contributed by Adam Olsen; [bpo-1583](https://bugs.python.org/issue?@action=redirect&bpo=1583).)

Python code can now reach the `siginterrupt()` function, which lets you toggle whether signals are allowed to interrupt system calls. (Contributed by Ralf Schmitt.)

The `setitimer()` and `getitimer()` functions have also been introduced (wherever the platform offers them). `setitimer()` lets you arm interval timers that fire a signal at the process after a chosen duration, counted in wall-clock time, consumed process time, or process plus system time combined. (Contributed by Guilherme Polo; [bpo-2240](https://bugs.python.org/issue?@action=redirect&bpo=2240).)

- Thanks to the new `SMTP_SSL` class, the [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) module can now carry SMTP over SSL. That class exposes an interface that matches the existing `SMTP` class. (Contributed by Monty Taylor.) Each class constructor also gained an optional `timeout` parameter, giving the initial connection attempt a timeout expressed in seconds. (Contributed by Facundo Batista.)

The module also gained an implementation of the LMTP protocol ([**RFC 2033**](https://datatracker.ietf.org/doc/html/rfc2033.html)). LMTP stands in for SMTP when moving e-mail between agents that keep no mail queue. (LMTP implemented by Leif Hedstrom; [bpo-957003](https://bugs.python.org/issue?@action=redirect&bpo=957003).)

`SMTP.starttls()` now conforms to [**RFC 3207**](https://datatracker.ietf.org/doc/html/rfc3207.html) and discards anything it learned from the server that didn't come out of the TLS negotiation itself. (Patch contributed by Bill Fenner; [bpo-829951](https://bugs.python.org/issue?@action=redirect&bpo=829951).)

- The [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now handles TIPC ([https://tipc.sourceforge.net/](https://tipc.sourceforge.net/)), a fast, non-IP-based protocol intended for clustered deployments. A TIPC address is a 4- or 5-tuple. (Contributed by Alberto Bertogli; [bpo-1646](https://bugs.python.org/issue?@action=redirect&bpo=1646).)

There's a new `create_connection()` function that accepts an address, connects with an optional timeout value, and returns the connected socket object. It also figures out the address's type and reaches it over IPv4 or IPv6 as fitting. Swapping `socket(socket.AF_INET, ...)` for `create_connection()` might be the only edit needed to get your code running over IPv6.

- The base classes within the [`SocketServer`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver) module can now invoke a [`handle_timeout()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.handle_timeout) method once a stretch of idleness, defined by the server's [`timeout`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.timeout) attribute, has elapsed. (Contributed by Michael Pomraning.) The [`serve_forever()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.serve_forever) method now accepts an optional poll interval given in seconds, governing how frequently the server inspects for a shutdown request. (Contributed by Pedro Werneck and Jeffrey Yasskin; [bpo-742598](https://bugs.python.org/issue?@action=redirect&bpo=742598), [bpo-1193577](https://bugs.python.org/issue?@action=redirect&bpo=1193577).)

- Gerhard Häring's [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module has moved up from the version 2.3.2 found in Python 2.5 to version 2.4.1.

- By way of the `'?'` format character, the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module now handles the C99 _Bool type. (Contributed by David Remahl.)

- The [`Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) objects that the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module hands out have acquired [`terminate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.terminate), [`kill()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.kill), and [`send_signal()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.send_signal) methods. Under Windows, `send_signal()` handles only the [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) signal, and every one of these methods stands in for the Win32 API function `TerminateProcess()`. (Contributed by Christian Heimes.)

- A new variable, `float_info`, in the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module is an object holding details drawn from the `float.h` file about how the platform supports floating point. Among this object's attributes are `mant_dig` (how many digits the mantissa holds), `epsilon` (the smallest gap separating 1.0 from the next representable value above it), plus several more. (Contributed by Christian Heimes; [bpo-1534](https://bugs.python.org/issue?@action=redirect&bpo=1534).)

A second new variable, `dont_write_bytecode`, decides whether Python emits any `.pyc` or `.pyo` files while importing a module. When this variable holds true, those compiled files go unwritten. Its initial value is established at start-up either by handing the [`-B`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-B) switch to the Python interpreter, or by defining the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable ahead of launching the interpreter. Later on, Python code may reassign this variable to govern whether bytecode files get written. (Contributed by Neal Norwitz and Georg Brandl.)

You can learn about the command-line arguments handed to the Python interpreter by inspecting attributes of a named tuple exposed as `sys.flags`. For instance, the `verbose` attribute is true when Python ran in verbose mode, `debug` is true under debugging mode, and so on. None of these attributes can be written. (Contributed by Christian Heimes.)

There's a new `getsizeof()` function that accepts a Python object and reports how much memory, counted in bytes, the object occupies. Built-in objects give back accurate figures; third-party extensions might not, though they can supply a `__sizeof__()` method to report the object's size. (Contributed by Robert Schuppenies; [bpo-2898](https://bugs.python.org/issue?@action=redirect&bpo=2898).)

You can now learn the active profiler and tracer functions by invoking [`sys.getprofile()`](https://docs.python.org/3.14/library/sys.html#sys.getprofile) and [`sys.gettrace()`](https://docs.python.org/3.14/library/sys.html#sys.gettrace). (Contributed by Georg Brandl; [bpo-1648](https://bugs.python.org/issue?@action=redirect&bpo=1648).)

- Beyond the POSIX.1-1988 (ustar) and GNU tar formats it already handled, the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module now supports POSIX.1-2001 (pax) tarfiles. GNU tar is the default format; hand over the `format` parameter to open a file in a different one:

```python
tar = tarfile.open("output.tar", "w",
                   format=tarfile.PAX_FORMAT)

```

Fresh `encoding` and `errors` parameters name an encoding plus an error handling scheme for character conversions. Python's three standard approaches to errors are `'strict'`, `'ignore'`, and `'replace'`,; the special value `'utf-8'` swaps in the UTF-8 representation for bad characters. (These character conversions happen because the PAX format allows Unicode filenames, defaulting to UTF-8 encoding.)

The `TarFile.add()` method now takes an `exclude` argument, a function usable for keeping certain filenames out of an archive. That function receives a filename and returns true when the file ought to be excluded or false when it should be archived. It is applied both to the name first passed into `add()` and to the names of files inside directories added recursively.

(All changes contributed by Lars Gustäbel).

- The constructor of the `telnetlib.Telnet` class gained an optional `timeout` parameter that names a timeout in seconds. (Added by Facundo Batista.)

- Ordinarily the [`tempfile.NamedTemporaryFile`](https://docs.python.org/3.14/library/tempfile.html#tempfile.NamedTemporaryFile) class removes the temporary file it made once that file is closed. You can now alter that behaviour by handing `delete=False` to the constructor. (Contributed by Damien Miller; [bpo-1537850](https://bugs.python.org/issue?@action=redirect&bpo=1537850).)

There's a new `SpooledTemporaryFile` class that acts like a temporary file yet keeps its data in memory until a ceiling size is passed. Once that limit is hit, the contents get flushed to an on-disk temporary file. (Contributed by Dustin J. Mitchell.)

Both the `NamedTemporaryFile` and `SpooledTemporaryFile` classes operate as context managers, letting you write `with tempfile.NamedTemporaryFile() as tmp: ...`. (Contributed by Alexander Belopolsky; [bpo-2021](https://bugs.python.org/issue?@action=redirect&bpo=2021).)

- A handful of context managers handy for writing tests landed in the [`test.test_support`](https://docs.python.org/3.14/library/test.html#module-test.support) module. [`EnvironmentVarGuard()`](https://docs.python.org/3.14/library/test.html#test.support.os_helper.EnvironmentVarGuard) is a context manager that swaps environment variables temporarily and then puts them back to their former values automatically.

A different context manager, `TransientResource`, can wrap calls to resources whose availability is uncertain; it catches and swallows a given list of exceptions. As an example, a network test might overlook particular failures while connecting out to an external web site:

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules-baseexception.md) · [Next source section](new-and-improved-modules-whitespace-to-whitespace.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](attribute-lookup-and-process-module-changes.md)

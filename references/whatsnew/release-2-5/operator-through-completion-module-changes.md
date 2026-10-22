# What's New in Python 2.5 / New, Improved, and Removed Modules — operator, optparse, os, pdb, pickle, pkgutil, queue, readline, resource, rlcompleter

- The `itemgetter()` and `attrgetter()` functions of the [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module now accept multiple fields. Calling `operator.attrgetter('a', 'b')`, for example, yields a function that fetches the `a` and `b` attributes. Pairing this new capability with the `sort()` method's `key` parameter makes it easy to sort lists by more than one field. (Contributed by Raymond Hettinger.)

- The [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module was synced to the Optik library at version 1.5.1. On the `OptionParser` class there is now an `epilog` attribute — a string printed after the help message — alongside a `destroy()` method for breaking the reference cycles the object creates. (Contributed by Greg Ward.)

- The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module saw a number of changes. The `stat_float_times` variable now defaults to true, which means [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) now returns time values as floats. (That does not guarantee `os.stat()` will hand back times accurate to fractions of a second; not every system offers that precision.)

Constants called [`os.SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET), [`os.SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR), and [`os.SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END) were added; they are the arguments to the [`os.lseek()`](https://docs.python.org/3.14/library/os.html#os.lseek) function. Two further constants for locking are [`os.O_SHLOCK`](https://docs.python.org/3.14/library/os.html#os.O_SHLOCK) and [`os.O_EXLOCK`](https://docs.python.org/3.14/library/os.html#os.O_EXLOCK).

Two new functions, `wait3()` and `wait4()`, were introduced. They resemble the `waitpid()` function — which pauses for a child process to finish and yields a tuple holding the process ID together with its exit status — but `wait3()` and `wait4()` report extra information. Because `wait3()` takes no process ID, it pauses for any child process to finish and yields a 3-tuple holding *process-id*, *exit-status*, *resource-usage* exactly as the [`resource.getrusage()`](https://docs.python.org/3.14/library/resource.html#resource.getrusage) function supplies it. `wait4(pid)` does accept a process ID. (Contributed by Chad J. Schroeder.)

On FreeBSD, the [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) function now reports times at nanosecond resolution, and the object it returns now carries `st_gen` and `st_birthtime`. Where the platform supports it, the `st_flags` attribute is available too. (Contributed by Antti Louko and Diego Petten??.)

- The Python debugger from the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module can now hold lists of commands to run once a breakpoint is hit and execution pauses. After breakpoint #1 exists, type `commands 1` and supply a sequence of commands to run, closing the list with `end`. That command list may contain commands that resume execution, like `continue` or `next`. (Contributed by Grégoire Dooms.)

- The [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and `cPickle` modules no longer tolerate a return value of `None` from the [`__reduce__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce__) method; that method must hand back a tuple of arguments instead. Returning `None` was deprecated back in Python 2.4, so this finishes removing the feature.

- The [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil) module, which holds assorted utility functions for locating packages, was extended to support [**PEP 302**](https://peps.python.org/pep-0302/)'s import hooks and now functions for packages held in ZIP-format archives as well. (Contributed by Phillip J. Eby.)

- Marc-Andr?? Lemburg's pybench benchmark suite is now bundled in the `Tools/pybench` directory. The pybench suite improves on the widely used `pystone.py` program because pybench measures the interpreter's speed in finer detail. It times specific operations — function calls, tuple slicing, method lookups, and numeric operations — rather than running many assorted operations and collapsing the result into a single figure the way `pystone.py` does.

- The `pyexpat` module now relies on version 2.0 of the Expat parser. (Contributed by Trent Mick.)

- The [`Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) class from the `Queue` module gained two new methods. `join()` blocks until every item in the queue has been fetched and all work on those items has finished. Worker threads invoke the second new method, `task_done()`, to indicate that processing of an item is complete. (Contributed by Raymond Hettinger.)

- The aging `regex` and `regsub` modules, deprecated all the way back since Python 2.0, have at last been removed. Other removed modules: `statcache`, `tzparse`, `whrandom`.

- Removed as well: the `lib-old` directory, home to antique modules such as `dircmp` and `ni`, is gone. Because `lib-old` was not on the default `sys.path`, this removal should not touch your code unless your programs explicitly added the directory to `sys.path`.

- The [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) module no longer depends on importing the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module, so it now works on non-Unix platforms. (Patch from Robert Kiendl.)

-

[Subject index](INDEX.md) · [Previous source section](new-improved-and-removed-modules-individual-messages.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Release/subject declaration](standard-library-module-changes.md) · [Following release/subject continuation](xmlrpc-paths-and-network-module-changes.md)

# What’s New in Python 2.6 / New and Improved Modules — pdb, pickletools, pkgutil, queue, random, re, rlcompleter, sched, select, shutil, signal, sys

A fresh command landed in the Python debugger that ships with the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module: "run" relaunches the program under debugging, and you may hand it fresh command-line arguments for that program if you wish. (Contributed by Rocky Bernstein; [bpo-1393667](https://bugs.python.org/issue?@action=redirect&bpo=1393667).)

- When you call [`pdb.post_mortem()`](https://docs.python.org/3.14/library/pdb.html#pdb.post_mortem) to start debugging a traceback and pass none, it will now fall back on whatever traceback [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) hands back. (Contributed by Facundo Batista; [bpo-1106316](https://bugs.python.org/issue?@action=redirect&bpo=1106316).)

- An `optimize()` function is now part of the [`pickletools`](https://docs.python.org/3.14/library/pickletools.html#module-pickletools) module; given a string holding a pickle, it strips out certain opcodes that go unused and hands back a smaller pickle encoding the very same data structure. (Contributed by Raymond Hettinger.)

- The [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil) module picked up a `get_data()` function, which yields the bytes of resource files shipped alongside an installed Python package. As an illustration:

```python
>>> import pkgutil
>>> print pkgutil.get_data('test', 'exception_hierarchy.txt')
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
 ...

```

(Contributed by Paul Moore; [bpo-2439](https://bugs.python.org/issue?@action=redirect&bpo=2439).)

- `Parser` objects belonging to the `pyexpat` module can now have their `buffer_size` attribute assigned, which adjusts how large the buffer that holds character data will be. (Contributed by Achim Gaedke; [bpo-1137](https://bugs.python.org/issue?@action=redirect&bpo=1137).)

- The `Queue` module ships additional queue flavors that pull entries out in alternate sequences. Items placed in a `PriorityQueue` live in a heap and emerge by priority, whereas a `LifoQueue` hands back the entries added most recently first, so it acts like a stack. (Contributed by Raymond Hettinger.)

- `Random` objects from the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module can at last be pickled under a 32-bit system and then unpickled under a 64-bit one, and the reverse too. The downside is that this same change keeps Python 2.6's `Random` objects from unpickling properly under older Python releases. (Contributed by Shawn Ligocki; [bpo-1727780](https://bugs.python.org/issue?@action=redirect&bpo=1727780).)

A fresh `triangular(low, high, mode)` function hands back random numbers drawn from a triangular distribution. The values produced fall between *low* and *high*, with *high* itself excluded, and *mode* being the value that turns up most often across the distribution. (Contributed by Wladmir van der Laan and Raymond Hettinger; [bpo-1681432](https://bugs.python.org/issue?@action=redirect&bpo=1681432).)

- Lengthy regular expression matches run through the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module will watch for incoming signals, so a search that drags on may now be cut short. (Contributed by Josh Hoyt and Ralf Schmitt; [bpo-846388](https://bugs.python.org/issue?@action=redirect&bpo=846388).)

The regular expression engine works by compiling bytecodes aimed at a small virtual machine built specifically for regexes. Since untrusted code might hand-craft hostile bytecode strings and provoke crashes, the regex bytecode now gets checked by a verifier that Python 2.6 ships. (Contributed by Guido van Rossum from work for Google App Engine; [bpo-3487](https://bugs.python.org/issue?@action=redirect&bpo=3487).)

- The `Completer.complete()` method belonging to the [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) module will from now on swallow exceptions that fire while a name is being evaluated. (Fixed by Lorenz Quack; [bpo-2250](https://bugs.python.org/issue?@action=redirect&bpo=2250).)

- `scheduler` instances in the [`sched`](https://docs.python.org/3.14/library/sched.html#module-sched) module now carry a read-only [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) attribute, which reports the scheduler's queue contents as a list of named tuples whose fields are `(time, priority, action, argument)`. (Contributed by Raymond Hettinger; [bpo-1861](https://bugs.python.org/issue?@action=redirect&bpo=1861).)

- Wrapper functions covering the Linux `epoll()` and BSD `kqueue()` system calls have been added to the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module. The pre-existing `poll` objects picked up a `modify()` method; calling `pollobj.modify(fd, eventmask)` with either a file descriptor or a file object plus an event mask updates the stored event mask for that file. (Contributed by Christian Heimes; [bpo-1657](https://bugs.python.org/issue?@action=redirect&bpo=1657).)

- There is now an optional *ignore* argument on the [`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) function, and it expects a callable object. That callable is handed each directory path together with a list of what that directory holds, and it returns a list of names to skip rather than copy.

For pairing with this new parameter, the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module also supplies an `ignore_patterns()` function. You give `ignore_patterns()` any number of glob-style patterns and it produces a callable that skips every file and directory matching one of those patterns. In the example below, a directory tree is copied while leaving out both `.svn` directories and Emacs backup files, whose names finish with "~":

```python
shutil.copytree('Doc/library', '/tmp/library',
                ignore=shutil.ignore_patterns('*~', '.svn'))

```

(Contributed by Tarek Ziad??; [bpo-2663](https://bugs.python.org/issue?@action=redirect&bpo=2663).)

- Marrying signal handling to GUI event loops such as the ones in Tkinter or GTk+ has been a headache for ages; most programs resort to polling, waking up several times a second to see whether any GUI events have arrived. The [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module can now handle this more efficiently. A call to `signal.set_wakeup_fd(fd)` designates a file descriptor for use; whenever a signal arrives, one byte is written into that descriptor. A C-level counterpart, [`PySignal_SetWakeupFd()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PySignal_SetWakeupFd), exists for assigning the descriptor as well.

[Subject index](INDEX.md) · [Next source section](signal-wakeup-and-network-module-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](attribute-lookup-and-process-module-changes.md)

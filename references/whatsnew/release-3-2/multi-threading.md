# What's New In Python 3.2 / Multi-threading - sys, threading

### Multi-threading

- The machinery that serializes the running of Python threads executing at the same time (commonly called the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL), or Global Interpreter Lock) was rebuilt. Its goals counted more predictable switching intervals plus lighter overhead arising from lock contention and the resulting volume of system calls. The earlier idea of a “check interval” governing thread switches was dropped, swapped for an absolute span measured in seconds. You can tune this parameter via [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval). At present its default sits at 5 milliseconds.

Further notes on how this was implemented appear in a [python-dev mailing-list message](https://mail.python.org/pipermail/python-dev/2009-October/093321.html) (note, though, that the “priority requests” described there were not retained for inclusion).

(Contributed by Antoine Pitrou.)

- Both regular and recursive locks now take an optional *timeout* argument on their [`acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire) method. (Contributed by Antoine Pitrou; [bpo-7316](https://bugs.python.org/issue?@action=redirect&bpo=7316).)

- In the same vein, [`threading.Semaphore.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore.acquire) picked up a *timeout* argument too. (Contributed by Torsten Landschoff; [bpo-850728](https://bugs.python.org/issue?@action=redirect&bpo=850728).)

- On platforms built atop Pthreads, signals can now interrupt regular and recursive lock acquisitions. Consequently, Python programs stuck deadlocked while taking locks can be terminated by sending SIGINT to the process over and over (which in most shells means pressing Ctrl+C). (Contributed by Reid Kleckner; [bpo-8844](https://bugs.python.org/issue?@action=redirect&bpo=8844).)

[Subject index](INDEX.md) · [Previous source section](turtledemo.md) · [Next source section](optimizations.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

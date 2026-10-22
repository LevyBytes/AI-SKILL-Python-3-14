# What's New In Python 3.11 / time — time

### time

- On Unix, when the `clock_nanosleep()` or `nanosleep()` function is on hand, [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) now calls it for a resolution of 1 nanosecond (10-9 seconds), instead of falling back on `select()`, whose resolution of 1 microsecond (10-6 seconds) is coarser.
> (Contributed by Benjamin Szőke and Victor Stinner in [bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302).)

- On Windows 8.1 and newer, [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) now relies on a waitable timer built upon [high-resolution timers](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/high-resolution-timers); that gives a resolution of 100 nanoseconds (10-7 seconds). Beforehand, what it offered was a resolution of 1 millisecond (10-3 seconds).

[Subject index](INDEX.md) · [Previous source section](threading.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)

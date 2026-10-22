# Python 3.6.4 release candidate 1 / library / functions and types

[bpo-27666](https://bugs.python.org/issue?@action=redirect&bpo=27666): Repaired stack corruption inside curses.box() and curses.ungetmouse() whenever the chtype or mmask_t type is narrower than a C long. As arguments, curses.box() now takes characters. Steve Fink provided the patch this is based on.

[bpo-28416](https://bugs.python.org/issue?@action=redirect&bpo=28416): A pickle.Pickler subclass carrying a persistent_id() method, and a pickle.Unpickler subclass carrying a persistent_load() method, no longer produce reference cycles in their instances.

[bpo-31457](https://bugs.python.org/issue?@action=redirect&bpo=31457): When log adapters are nested, the inner `process()` methods no longer get skipped.

[bpo-31770](https://bugs.python.org/issue?@action=redirect&bpo=31770): Stop a crash that occurred whenever a `sqlite3.Cursor` object had its `__init__()` method invoked repeatedly. Oren Milman wrote the patch.

[bpo-31673](https://bugs.python.org/issue?@action=redirect&bpo=31673): Corrected a typo within the name of Tkinter’s adderrorinfo() method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

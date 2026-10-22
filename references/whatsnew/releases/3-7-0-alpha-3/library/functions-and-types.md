# Python 3.7.0 alpha 3 / library / functions and types

[bpo-31457](https://bugs.python.org/issue?@action=redirect&bpo=31457): When log adapters are nested, the inner `process()` methods are no longer skipped.

[bpo-30541](https://bugs.python.org/issue?@action=redirect&bpo=30541): A new function lets you seal a mock so that child mocks are no longer created automatically. Mario Corchero contributed the patch.

[bpo-31770](https://bugs.python.org/issue?@action=redirect&bpo=31770): Stop a crash that happened when the `__init__()` method of a `sqlite3.Cursor` object was invoked more than one time. Oren Milman provided the patch.

[bpo-32214](https://bugs.python.org/issue?@action=redirect&bpo=32214): PEP 557, Data Classes. Supplies a decorator that injects boilerplate methods into classes relying on type annotations to declare fields.

[bpo-32018](https://bugs.python.org/issue?@action=redirect&bpo=32018): When a parameter carries both an annotation and a default value, inspect.signature ought to obey [**PEP 8**](https://peps.python.org/pep-0008/). Donghee Na wrote the patch.

[bpo-27666](https://bugs.python.org/issue?@action=redirect&bpo=27666): Repairs stack corruption inside curses.box() and curses.ungetmouse() whenever the chtype or mmask_t types are smaller than a C long. curses.box() now takes characters as arguments. Steve Fink's patch was the basis.

[bpo-28281](https://bugs.python.org/issue?@action=redirect&bpo=28281): Drops the year limit (1-9999) from the Calendar.weekday() function. Mark Gollahon wrote the patch.

[bpo-28564](https://bugs.python.org/issue?@action=redirect&bpo=28564): A 20–40% speed boost was given to the shutil.rmtree() function, accomplished by leaning on the os.scandir() function.

[bpo-28416](https://bugs.python.org/issue?@action=redirect&bpo=28416): No more reference cycles are created by instances of a pickle.Pickler subclass carrying the persistent_id() method, nor by instances of a pickle.Unpickler subclass carrying the persistent_load() method.

[bpo-31827](https://bugs.python.org/issue?@action=redirect&bpo=31827): Drops the os.stat_float_times() function, which arrived in Python 2.3 for backward compatibility with Python 2.2 and had been deprecated ever since Python 3.1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

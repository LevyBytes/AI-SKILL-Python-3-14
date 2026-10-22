# Python 3.5.3 release candidate 1 / library / text and unicode

[bpo-22115](https://bugs.python.org/issue?@action=redirect&bpo=22115): Corrected the tracing of Tkinter variables: trace_vdelete() called with the wrong mode no longer disrupts tracing, trace_vinfo() consistently returns a list of string pairs, and tracing under the "u" mode now functions.

- Resolved a scoping problem in importlib.util.LazyLoader that raised an UnboundLocalError while lazily loading a module already present in sys.modules.

[bpo-26754](https://bugs.python.org/issue?@action=redirect&bpo=26754): A handful of functions (compile() and friends) used to take a filename argument supplied as an iterable of integers. From now on only strings and byte-like objects qualify.

[bpo-27897](https://bugs.python.org/issue?@action=redirect&bpo=27897): Repair a possible crash in sqlite3.Connection.create_collation() that occurred when an invalid string-like object was passed as a name. Xiang Zhang supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

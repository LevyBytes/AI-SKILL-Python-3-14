# Python 3.8.0 alpha 1 / library / memory and lifetimes

[bpo-30977](https://bugs.python.org/issue?@action=redirect&bpo=30977): uuid.UUID now relies on `__slots__` to shrink its memory footprint. The work builds on an original patch from Wouter Bolsterlee.

[bpo-34794](https://bugs.python.org/issue?@action=redirect&bpo=34794): Closed a Tkinter leak triggered by handing the Python wrapper around Tcl_Obj back across to Tcl/Tk.

[bpo-33263](https://bugs.python.org/issue?@action=redirect&bpo=33263): Repair an FD leak within `_SelectorSocketTransport` Patch by Vlad Starostin.

[bpo-35445](https://bugs.python.org/issue?@action=redirect&bpo=35445): Memory errors that happen while building posix.environ are no longer ignored.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

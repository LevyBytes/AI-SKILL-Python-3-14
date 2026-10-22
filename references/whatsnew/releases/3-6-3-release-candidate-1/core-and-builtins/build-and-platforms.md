# Python 3.6.3 release candidate 1 / core and builtins / build and platforms

[bpo-31471](https://bugs.python.org/issue?@action=redirect&bpo=31471): Repair an assertion failure within `subprocess.Popen()` on Windows whenever the env argument carries a faulty `keys()` method. Oren Milman wrote the patch.

[bpo-30703](https://bugs.python.org/issue?@action=redirect&bpo=30703): Better signal delivery. Steer clear of using Py_AddPendingCall from within a signal handler, so that signal-unsafe functions are not invoked. The tests added here fail without the remainder of the patch, both on Linux and on OS X. That shows our signal delivery logic had defects (certain signals could vanish).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

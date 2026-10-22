# Python 3.7.0 alpha 1 / core and builtins / build and platforms

[bpo-30703](https://bugs.python.org/issue?@action=redirect&bpo=30703): Make signal delivery better. Steer clear of Py_AddPendingCall inside the signal handler so that signal-unsafe functions aren't invoked. The tests added here fail without the remainder of the patch on both Linux and OS X. That demonstrates our signal delivery logic had bugs (certain signals could go missing).

[bpo-31471](https://bugs.python.org/issue?@action=redirect&bpo=31471): On Windows, an assertion failure inside `subprocess.Popen()` was fixed when the env argument supplies a broken `keys()` method. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

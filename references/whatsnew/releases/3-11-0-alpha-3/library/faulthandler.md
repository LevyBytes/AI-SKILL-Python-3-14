# Python 3.11.0 alpha 3 / library / faulthandler

[bpo-45831](https://bugs.python.org/issue?@action=redirect&bpo=45831): While dumping a traceback, [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) is now able to emit ASCII-only strings (such as filenames and function names) using just one write() syscall. That lowers the chance of an unreadable dump whenever two threads or two processes write a traceback into the same file (for instance stderr) concurrently. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.0 alpha 1 / library / traceback

[bpo-14285](https://bugs.python.org/issue?@action=redirect&bpo=14285): Running a package through the "python -m package" option will now surface a correct traceback should the package initialization fail. Instead of throwing ImportError, the "runpy" module now permits exceptions raised during package initialization to propagate up to the caller.

[bpo-23848](https://bugs.python.org/issue?@action=redirect&bpo=23848): Under Windows, faulthandler.enable() now additionally registers an exception handler that dumps every Python thread's traceback on any Windows exception, not merely on the UNIX signals SIGSEGV, SIGFPE, SIGABRT.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

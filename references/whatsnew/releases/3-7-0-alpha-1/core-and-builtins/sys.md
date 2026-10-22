# Python 3.7.0 alpha 1 / core and builtins / sys

[bpo-28799](https://bugs.python.org/issue?@action=redirect&bpo=28799): Drop the `PyEval_GetCallStats()` function and mark the undocumented, untested `sys.callstats()` function as deprecated. The `CALL_PROFILE` special build is gone too; for profiling function calls reach instead for the [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) function, [`cProfile`](https://docs.python.org/3.14/library/profile.html#module-cProfile), or [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile).

[bpo-28932](https://bugs.python.org/issue?@action=redirect&bpo=28932): Skip including <sys/random.h> whenever it isn't present.

[bpo-31343](https://bugs.python.org/issue?@action=redirect&bpo=31343): Pull in sys/sysmacros.h for major(), minor(), and makedev(). The GNU C library intends to drop those functions from sys/types.h.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

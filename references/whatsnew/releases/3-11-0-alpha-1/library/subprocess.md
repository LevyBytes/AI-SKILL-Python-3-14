# Python 3.11.0 alpha 1 / library / subprocess

[bpo-40497](https://bugs.python.org/issue?@action=redirect&bpo=40497): When user code hands the bogus keyword argument *check* to [`subprocess.check_output()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.check_output), it now raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). The earlier behaviour deferred the breakage to a later [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Rémi Lapeyre authored the change.

[bpo-44935](https://bugs.python.org/issue?@action=redirect&bpo=44935): For improved performance, [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) running on Solaris now likewise leans on [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.10.0 alpha 2 / library / profile

[bpo-40492](https://bugs.python.org/issue?@action=redirect&bpo=40492): Corrects `--outfile` behavior for [`cProfile`](https://docs.python.org/3.14/library/profile.html#module-cProfile) / [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile): the report is now placed in the starting directory even when the profiled program switches its working directory mid-run. Anthony Sottile sent the PR.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 6 / tools demos / os

[bpo-40094](https://bugs.python.org/issue?@action=redirect&bpo=40094): Correct the exit code of the `which.py` script: it now relies on [`os.waitstatus_to_exitcode()`](https://docs.python.org/3.14/library/os.html#os.waitstatus_to_exitcode) to translate the [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) exit status into an exit code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

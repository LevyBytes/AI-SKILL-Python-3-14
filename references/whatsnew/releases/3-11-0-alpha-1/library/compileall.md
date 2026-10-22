# Python 3.11.0 alpha 1 / library / compileall

[bpo-34990](https://bugs.python.org/issue?@action=redirect&bpo=34990): Corrected a Y2k38 defect in the compileall module that prevented compilation of files whose modification time landed after the year 2038.

[bpo-44666](https://bugs.python.org/issue?@action=redirect&bpo=44666): Fixed a problem in [`compileall.compile_file()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_file) that arose whenever `sys.stdout` had been redirected. Stefan Hölzl authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

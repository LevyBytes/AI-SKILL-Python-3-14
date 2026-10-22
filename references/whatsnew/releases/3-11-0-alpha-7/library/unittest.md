# Python 3.11.0 alpha 7 / library / unittest

[bpo-46421](https://bugs.python.org/issue?@action=redirect&bpo=46421): Resolve a unittest problem where invoking the command as `python -m unittest` with filename(s) starting with a dot (.) caused a `ValueError` to come back.

[bpo-24959](https://bugs.python.org/issue?@action=redirect&bpo=24959): A defect is fixed in which [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) would occasionally lose frames from the tracebacks of exceptions thrown during tests.

[bpo-14265](https://bugs.python.org/issue?@action=redirect&bpo=14265): unittest output now carries the fully qualified test name

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

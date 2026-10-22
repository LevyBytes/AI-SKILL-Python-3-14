# Python 3.11.0 alpha 1 / security / tempfile

[bpo-42278](https://bugs.python.org/issue?@action=redirect&bpo=42278): Swapped the [`tempfile.mktemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mktemp) call for [`TemporaryDirectory`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory) so a possible race condition is avoided.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

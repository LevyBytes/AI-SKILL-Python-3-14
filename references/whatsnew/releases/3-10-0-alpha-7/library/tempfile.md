# Python 3.10.0 alpha 7 / library / tempfile

[bpo-40701](https://bugs.python.org/issue?@action=redirect&bpo=40701): Assigning a bytes value to the [`tempfile.tempdir`](https://docs.python.org/3.14/library/tempfile.html#tempfile.tempdir) global is now treated consistently. Formerly, certain tempfile APIs could raise exceptions in that scenario when the directory was not already present. This also guarantees that [`tempfile.gettempdir()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.gettempdir) and [`tempfile.gettempdirb()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.gettempdirb) *always* hand back `str` and `bytes` respectively.

[bpo-29982](https://bugs.python.org/issue?@action=redirect&bpo=29982): Provide an optional *ignore_cleanup_errors* parameter for [`tempfile.TemporaryDirectory()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory) and permit `cleanup()` to be retried more than once. C.A.M. Gerlach contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

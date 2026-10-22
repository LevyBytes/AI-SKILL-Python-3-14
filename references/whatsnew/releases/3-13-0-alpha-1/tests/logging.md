# Python 3.13.0 alpha 1 / tests / logging

[gh-110033](https://github.com/python/cpython/issues/110033): Repaired `test_interprocess_signal()` belonging to `test_signal`. Guarantee the `subprocess.Popen` object gets torn down ahead of the test throwing an exception within a signal handler. If not, `Popen.__del__()` may capture that exception, which surfaces as `Exception ignored in: ...` logging and breaks the test. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

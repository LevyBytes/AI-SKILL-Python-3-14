# Python 3.10.0 alpha 1 / library / build and platforms

[bpo-41687](https://bugs.python.org/issue?@action=redirect&bpo=41687): Made the sendfile implementation work correctly under Solaris.

[bpo-39010](https://bugs.python.org/issue?@action=redirect&bpo=39010): Restarting a `ProactorEventLoop` under Windows no longer emits spurious `ConnectionResetErrors` into the log.

[bpo-39244](https://bugs.python.org/issue?@action=redirect&bpo=39244): Corrected `multiprocessing.context.get_all_start_methods` so the default method is returned first on macOS as expected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

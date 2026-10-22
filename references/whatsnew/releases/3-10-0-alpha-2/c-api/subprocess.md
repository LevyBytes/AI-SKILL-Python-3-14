# Python 3.10.0 alpha 2 / c api / subprocess

[bpo-40423](https://bugs.python.org/issue?@action=redirect&bpo=40423): Whenever the `close_range(low, high, flags)` syscall exists, the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module together with `os.closerange` will rely on it to close descriptor ranges more efficiently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

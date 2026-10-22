# Python 3.8.0 alpha 1 / macos / threads and concurrency

[bpo-31903](https://bugs.python.org/issue?@action=redirect&bpo=31903): Within `_scproxy`, release the GIL during calls into `SystemConfiguration` so deadlocks are avoided.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

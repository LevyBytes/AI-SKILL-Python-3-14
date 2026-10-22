# Python 3.9.0 alpha 1 / idle / writing non encodable characters stderr no longer breaks idle

[bpo-36698](https://bugs.python.org/issue?@action=redirect&bpo=36698): Writing non-encodable characters to stderr no longer breaks IDLE. Matching the standard Python interpreter, it escapes them with a backslash. The `errors` field was added to the standard streams.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

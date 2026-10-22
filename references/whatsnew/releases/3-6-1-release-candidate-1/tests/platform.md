# Python 3.6.1 release candidate 1 / tests / platform

[bpo-28087](https://bugs.python.org/issue?@action=redirect&bpo=28087): On macOS, skip the poll failures in test_asyncore and test_eintr. A handful of select.poll tests are skipped on macOS too, because the platform's underlying poll function has unresolved problems on certain macOS releases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.4 release candidate 1 / tests / platform

[bpo-28087](https://bugs.python.org/issue?@action=redirect&bpo=28087): Bypass the test_asyncore and test_eintr poll failures seen on macOS. Several select.poll tests are skipped on macOS because the platform poll function still has unresolved issues on some macOS releases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

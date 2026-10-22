# Python 3.9.0 alpha 1 / tests / numeric behavior

[bpo-38270](https://bugs.python.org/issue?@action=redirect&bpo=38270): test.support gained a helper function that checks whether a hash digest function is available. A number of tests were reworked to steer clear of MD5 and rely on SHA256 instead. The remaining tests are flagged as MD5 users and skipped wherever MD5 is disabled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 beta 1 / library / hmac

[bpo-40645](https://bugs.python.org/issue?@action=redirect&bpo=40645): The [`hmac.HMAC`](https://docs.python.org/3.14/library/hmac.html#hmac.HMAC) leaks internal implementation details. Its `digest_cons`, `inner`, and `outer` attributes are deprecated and are scheduled for removal later on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

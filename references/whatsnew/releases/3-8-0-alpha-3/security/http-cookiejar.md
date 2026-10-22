# Python 3.8.0 alpha 3 / security / http cookiejar

[bpo-35121](https://bugs.python.org/issue?@action=redirect&bpo=35121): Avoid sending domain A's cookies that lack a Domain attribute over to domain B when domain A happens to be a suffix match of domain B, given a cookiejar using the [`http.cookiejar.DefaultCookiePolicy`](https://docs.python.org/3.14/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy) policy. Karthikeyan Singaravelan supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

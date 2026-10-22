# Python 3.8.0 alpha 3 / library / files and paths

[bpo-36043](https://bugs.python.org/issue?@action=redirect&bpo=36043): `FileCookieJar` now accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). Stéphane Wirtel contributed this

[bpo-35121](https://bugs.python.org/issue?@action=redirect&bpo=35121): Refrain from setting a cookie on a request when the request path matches the cookie's path attribute as a prefix yet does not finish with "/". Karthikeyan Singaravelan wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

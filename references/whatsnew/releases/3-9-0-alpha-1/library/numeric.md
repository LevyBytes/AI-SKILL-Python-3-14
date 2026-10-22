# Python 3.9.0 alpha 1 / library / numeric

[bpo-27657](https://bugs.python.org/issue?@action=redirect&bpo=27657): Correct urllib.parse.urlparse() when handling numeric paths. An input such as "path:80" is now treated not as a path but as a scheme ("path") plus a path ("80").

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

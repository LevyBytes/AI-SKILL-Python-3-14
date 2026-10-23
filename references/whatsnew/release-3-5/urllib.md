# What’s New In Python 3.5 / urllib - ssl, urllib.parse, urllib.request

### urllib

The freshly added [`request.HTTPPasswordMgrWithPriorAuth`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth) class lets HTTP Basic Authentication credentials be tracked, which removes pointless `401` response handling or sends credentials up front on the very first request, so it can reach servers that answer with a `404` rather than a `401` when no `Authorization` header arrives. (Contributed by Matej Cepl in [bpo-19494](https://bugs.python.org/issue?@action=redirect&bpo=19494) and Akshit Khurana in [bpo-7159](https://bugs.python.org/issue?@action=redirect&bpo=7159).)

An added *quote_via* parameter on the [`parse.urlencode()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlencode) function gives you a means to govern how query segments get encoded when that matters. (Contributed by Samwyse and Arnon Yaari in [bpo-13866](https://bugs.python.org/issue?@action=redirect&bpo=13866).)

You can now hand an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object as the *context* argument to [`request.urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen), and that object drives the HTTPS connection. (Contributed by Alex Gaynor in [bpo-22366](https://bugs.python.org/issue?@action=redirect&bpo=22366).)

[`parse.urljoin()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urljoin) now resolves relative URLs following [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) rules, replacing the older [**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html) and [**RFC 2396**](https://datatracker.ietf.org/doc/html/rfc2396.html) behavior. (Contributed by Demian Brecht and Senthil Kumaran in [bpo-22118](https://bugs.python.org/issue?@action=redirect&bpo=22118).)

[Subject index](INDEX.md) · [Previous source section](unittest-mock.md) · [Next source section](wsgiref.md) · [Release/subject declaration](summary-release-highlights.md)

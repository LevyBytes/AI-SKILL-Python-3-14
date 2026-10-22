# Python 3.6.0 alpha 1 / library / urllib request

[bpo-26864](https://bugs.python.org/issue?@action=redirect&bpo=26864): Inside urllib.request, the proxy-bypass comparison of a host against no_proxy is now case-insensitive and will no longer match unrelated hostnames that merely end with a bypassed name as a suffix. Xiang Zhang supplied the patch.

[bpo-26804](https://bugs.python.org/issue?@action=redirect&bpo=26804): When choosing proxy environment variables, urllib.request now favors lower_case over UPPER_CASE or Mixed_Case variants. Hans-Peter Jansen sent in the patch.

[bpo-14132](https://bugs.python.org/issue?@action=redirect&bpo=14132): Repair urllib.request redirect handling for the case where the target carries only a query string. Ján Janech provided the original fix.

[bpo-17214](https://bugs.python.org/issue?@action=redirect&bpo=17214): Any non-ASCII bytes appearing in a redirect target URL are now percent-encoded by the "urllib.request" module. Because certain servers put non-ASCII bytes into their Location header fields while "http.client" insists that the request target be ASCII-encodable, a UnicodeEncodeError would otherwise get raised. Christian Heimes' patch served as the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

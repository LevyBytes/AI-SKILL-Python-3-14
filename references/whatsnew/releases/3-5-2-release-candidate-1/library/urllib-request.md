# Python 3.5.2 release candidate 1 / library / urllib request

[bpo-14132](https://bugs.python.org/issue?@action=redirect&bpo=14132): Correct urllib.request redirect handling for targets that consist only of a query string. Ján Janech provided the original fix.

[bpo-17214](https://bugs.python.org/issue?@action=redirect&bpo=17214): Non-ASCII bytes appearing in redirect target URLs are now percent-encoded by the "urllib.request" module. Certain servers emit Location header fields containing non-ASCII bytes, yet "http.client" needs the request target to be ASCII-encodable, otherwise it raises a UnicodeEncodeError. Christian Heimes's patch served as the basis.

[bpo-26864](https://bugs.python.org/issue?@action=redirect&bpo=26864): In urllib.request, make the proxy-bypass host comparison against no_proxy case-insensitive, and ensure it does not match unrelated hostnames that merely end with a bypassed hostname as a suffix. Xiang Zhang authored the patch.

[bpo-26804](https://bugs.python.org/issue?@action=redirect&bpo=26804): urllib.request will favor lower_case proxy environment variables ahead of UPPER_CASE or Mixed_Case variants. Hans-Peter Jansen contributed this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

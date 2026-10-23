# http.cookiejar - Examples

### Examples

This opening example demonstrates the everyday use of `http.cookiejar`:

```python
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

Here is how you would fetch a URL while reusing the cookies from your Netscape, Mozilla, or Lynx setup (it presumes the Unix/Netscape arrangement for where the cookies file sits):

```python
import os, http.cookiejar, urllib.request
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

The following example shows `DefaultCookiePolicy` in action. It enables [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies, tightens domain handling when Netscape cookies are stored and sent back, and prevents certain domains from either setting cookies or receiving them:

```python
import urllib.request
from http.cookiejar import CookieJar, DefaultCookiePolicy
policy = DefaultCookiePolicy(
    rfc2965=True, strict_ns_domain=Policy.DomainStrict,
    blocked_domains=["ads.net", ".ads.net"])
cj = CookieJar(policy)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

[Subject index](INDEX.md) · [Previous](cookie-version-to-cookie-is-expired.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

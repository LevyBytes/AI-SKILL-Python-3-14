# http.cookiejar: Cookie domain blocklists and name restrictions

### DefaultCookiePolicy Objects

Implements the standard rules for accepting and returning cookies.

It covers both [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) and Netscape cookies. RFC 2965 handling is switched off by default.

The simplest path to supplying your own policy is to override this class and have your overriding implementations call its methods before you tack on your own extra checks:

```python
import http.cookiejar
class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):
    def set_ok(self, cookie, request):
        if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
            return False
        if i_dont_want_to_store_this_cookie(cookie):
            return False
        return True

```

Beyond the capabilities needed to implement the `CookiePolicy` interface, this class lets you block and allow domains from setting and receiving cookies. It also offers a few strictness switches with which you can firm up the rather loose Netscape protocol rules somewhat (at the price of blocking some harmless cookies).

Both a domain blocklist and a domain allowlist are available (each disabled by default). Cookie setting and returning involves only those domains kept off the blocklist while also on the allowlist (whenever the allowlist is in effect). Use the *blocked_domains* constructor argument, plus the `blocked_domains()` and `set_blocked_domains()` methods (and the matching argument and methods for *allowed_domains*). After setting an allowlist, you can disable it once more by assigning it [`None`](https://docs.python.org/3.14/library/constants.html#None).

Domains on block or allow lists that don't begin with a dot have to equal the cookie domain to count as a match. For instance, `"example.com"` matches a blocklist entry of `"example.com"`, whereas `"www.example.com"` does not. Domains that do begin with a dot are matched by more specific domains as well. For instance, both `"www.example.com"` and `"www.coyote.example.com"` match `".example.com"` (yet `"example.com"` on its own does not). IP addresses form an exception and have to match exactly. For instance, if blocked_domains holds `"192.168.1.2"` and `".168.1.2"`, then 192.168.1.2 is blocked, but 193.168.1.2 is not.

`DefaultCookiePolicy` provides the following additional methods:

 DefaultCookiePolicy.blocked_domains()

Return the sequence of blocked domains (as a tuple).

 DefaultCookiePolicy.set_blocked_domains(*blocked_domains*)

Set the sequence of blocked domains.

 DefaultCookiePolicy.is_blocked(*domain*)

Return `True` when *domain* sits on the blocklist that governs setting or receiving cookies.

 DefaultCookiePolicy.allowed_domains()

Return [`None`](https://docs.python.org/3.14/library/constants.html#None), or the sequence of allowed domains (as a tuple).

 DefaultCookiePolicy.set_allowed_domains(*allowed_domains*)

Set the sequence of allowed domains, or [`None`](https://docs.python.org/3.14/library/constants.html#None).

 DefaultCookiePolicy.is_not_allowed(*domain*)

Return `True` when *domain* is absent from the allowlist that governs setting or receiving cookies.

`DefaultCookiePolicy` instances carry the following attributes, each of which is initialised from the constructor argument bearing the same name, and each of which may be assigned to.

 DefaultCookiePolicy.rfc2109_as_netscape

When true, request that the `CookieJar` instance turn [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies (that is, cookies that arrived in a *Set-Cookie* header whose version cookie-attribute equals 1) into Netscape cookies, accomplished by assigning 0 to the `Cookie` instance's version attribute. Its default is [`None`](https://docs.python.org/3.14/library/constants.html#None); under that setting, the downgrade happens for RFC 2109 cookies precisely when [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) handling has been disabled. Hence the default behaviour downgrades RFC 2109 cookies.

General strictness switches:

 DefaultCookiePolicy.strict_domain

Prevent sites from setting two-component domains that use country-code top-level domains such as `.co.uk`, `.gov.uk`, `.co.nz`.etc. This is far from perfect and isn't guaranteed to work!

[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) protocol strictness switches:

 DefaultCookiePolicy.strict_rfc2965_unverifiable

Obey the [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) rules covering unverifiable transactions (typically, an unverifiable transaction stems from a redirect or from a request for an image that lives on another site). When this is false, verifiability *never* causes cookies to be blocked

Netscape protocol strictness switches:

 DefaultCookiePolicy.strict_ns_unverifiable

Extend the [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) rules for unverifiable transactions so they apply to Netscape cookies too.

 DefaultCookiePolicy.strict_ns_domain

Flags that say how strictly the domain-matching rules apply to Netscape cookies. The permitted values appear below.

 DefaultCookiePolicy.strict_ns_set_initial_dollar

Disregard any cookie in a Set-Cookie: header whose name begins with `'$'`.

[Subject index](INDEX.md) · [Previous](cookiepolicy-set-ok-to-cookiepolicy-hide-cookie2.md) · [Continue](cookie-path-and-domain-strictness.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

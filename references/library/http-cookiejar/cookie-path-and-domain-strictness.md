# http.cookiejar: Cookie path and domain acceptance strictness

DefaultCookiePolicy.strict_ns_set_path

Forbid setting a cookie when its path fails to path-match the request URI.

`strict_ns_domain` holds a set of flags. You build its value by or-ing flags together (for instance, `DomainStrictNoDots|DomainStrictNonDomain` indicates that both flags are set).

 DefaultCookiePolicy.DomainStrictNoDots

While setting cookies, the "host prefix" is not allowed to contain a dot (eg. `www.foo.bar.com` can't set a cookie for `.bar.com`, since `www.foo` contains a dot).

 DefaultCookiePolicy.DomainStrictNonDomain

Cookies that never explicitly named a `domain` cookie-attribute may only be sent back to a domain identical to the domain that set the cookie (eg. `spam.example.com` won't receive cookies from `example.com` that carried no `domain` cookie-attribute).

 DefaultCookiePolicy.DomainRFC2965Match

When setting cookies, require a full [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) domain-match.

The attributes below are offered for convenience, being the handiest combinations of the flags above:

 DefaultCookiePolicy.DomainLiberal

The same as 0 (ie. every one of the Netscape domain strictness flags above turned off).

 DefaultCookiePolicy.DomainStrict

Equivalent to `DomainStrictNoDots|DomainStrictNonDomain`.

[Subject index](INDEX.md) · [Previous](cookie-domain-blocklists-and-name-restrictions.md) · [Continue](cookie-objects.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md) · [Owning module, declaration or section: DefaultCookiePolicy Objects](cookie-domain-blocklists-and-name-restrictions.md)

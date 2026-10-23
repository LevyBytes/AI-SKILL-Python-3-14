# What’s New in Python 2.4 / cookielib - http.cookiejar, http.cookies, urllib.request

### cookielib

Client-side management of HTTP cookies is what the [`cookielib`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar) library handles, serving as the counterpart to the server-side cookie support in the [`Cookie`](https://docs.python.org/3.14/library/http.cookies.html#module-http.cookies) module. Cookie jars hold the cookies: behind the scenes the library tucks away any cookie the web server sends into the jar, then pulls it back out of the jar when it reconnects to that server. Much as browsers do, policy objects decide whether a cookie is taken or refused.

For keeping cookies between sessions, the library ships two cookie-jar implementations — one that writes them in the Netscape format, so programs can reuse the Mozilla or Lynx cookie files, and another that matches the format used by the Perl libwww library.

The [`urllib2`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) module was reworked to cooperate with [`cookielib`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar): an `HTTPCookieProcessor` looks after a cookie jar drawn on whenever URLs are accessed.

John J. Lee contributed this module.

[Subject index](INDEX.md) · [Previous source section](signal-through-xmlrpc-module-changes.md) · [Next source section](doctest-f-and-o-and-p-and-g.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)

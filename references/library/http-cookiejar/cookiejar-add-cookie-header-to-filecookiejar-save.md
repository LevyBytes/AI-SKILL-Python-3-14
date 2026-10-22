# http.cookiejar: CookieJar request headers and file persistence

### CookieJar and FileCookieJar Objects

`CookieJar` objects honor the [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) protocol so you can iterate across the `Cookie` objects they hold.

`CookieJar` offers these methods:

 CookieJar.add_cookie_header(*request*)

Add correct *Cookie* header to *request*.

Where policy permits (ie. the `rfc2965` and `hide_cookie2` attributes on the `CookieJar`'s `CookiePolicy` instance are true and false respectively), the *Cookie2* header gets added as well when that is appropriate.

The *request* object (typically a [`urllib.request.Request`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.Request) instance) is required to support the methods `get_full_url()`, `has_header()`, `get_header()`, `header_items()`, `add_unredirected_header()` and the attributes `host`, `type`, `unverifiable` and `origin_req_host` as set out by [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request).

Changed in version 3.3: now the *request* object requires an `origin_req_host` attribute; reliance on the deprecated `get_origin_req_host()` method is gone.

 CookieJar.extract_cookies(*response*, *request*)

Pull cookies out of the HTTP *response* and place them inside the `CookieJar`, wherever policy permits it.

The `CookieJar` searches for permissible *Set-Cookie* and *Set-Cookie2* headers within the *response* argument, and saves cookies accordingly (provided the `CookiePolicy.set_ok()` method approves).

The *response* object (typically what a call to [`urllib.request.urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen), or something comparable, returns) ought to support an `info()` method that yields an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance.

The *request* object (typically a [`urllib.request.Request`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.Request) instance) is required to support the method `get_full_url()` plus the attributes `host`, `unverifiable` and `origin_req_host`, as set out by [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request). The request supplies default values for cookie-attributes and is also used to verify that the cookie may be set.

Changed in version 3.3: the *request* object from here on must carry an `origin_req_host` attribute; the dependence on the deprecated `get_origin_req_host()` method was dropped.

 CookieJar.set_policy(*policy*)

Set the `CookiePolicy` instance to be used.

 CookieJar.make_cookies(*response*, *request*)

Return sequence of `Cookie` objects extracted from *response* object.

Consult the documentation on `extract_cookies()` to learn which interfaces the *response* and *request* arguments must satisfy.

 CookieJar.set_cookie_if_ok(*cookie*, *request*)

Set a `Cookie` if policy says it's OK to do so.

 CookieJar.set_cookie(*cookie*)

Set a `Cookie` directly, skipping any policy check on whether it ought to be set.

 CookieJar.clear([*domain*[, *path*[, *name*]]])

Clear some cookies.

When called with no arguments, every cookie is cleared. When handed a single argument, only the cookies that belong to that *domain* get removed. When handed two arguments, the cookies tied to the given *domain* and URL *path* are removed. When handed three arguments, then the single cookie with the given *domain*, *path* and *name* is removed.

Raises [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) if no matching cookie exists.

 CookieJar.clear_session_cookies()

Discard all session cookies.

Throws away every contained cookie whose `discard` attribute is true (typically because they carried neither a `max-age` nor an `expires` cookie-attribute, or else an explicit `discard` cookie-attribute). With interactive browsers, a session generally ends when the browser window is closed.

Bear in mind that the `save()` method won't persist session cookies in any case, unless you request otherwise by handing it a true *ignore_discard* argument.

`FileCookieJar` adds the following methods:

 FileCookieJar.save(*filename=None*, *ignore_discard=False*, *ignore_expires=False*)

Save cookies to a file.

This base class raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError). Subclasses may leave this method unimplemented.

*filename* is the name of file in which to save cookies. When *filename* goes unspecified, `self.filename` is used (whose default is whatever value was passed to the constructor, if any); should `self.filename` be [`None`](https://docs.python.org/3.14/library/constants.html#None), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

*ignore_discard*: persist cookies even when they are marked for discarding. *ignore_expires*: persist cookies even after they have expired

Should the file already exist, it is overwritten, which wipes out every cookie it held. Cookies that were saved can be brought back afterward by means of the `load()` or `revert()` methods.

[Subject index](INDEX.md) · [Previous](http-cookiejar-cookie-class.md) · [Continue](filecookiejar-load-to-filecookiejar-delayload.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

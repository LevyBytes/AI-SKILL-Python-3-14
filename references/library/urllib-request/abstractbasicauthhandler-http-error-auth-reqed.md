# urllib.request - AbstractBasicAuthHandler Objects

### AbstractBasicAuthHandler Objects

 AbstractBasicAuthHandler.http_error_auth_reqed(*authreq*, *host*, *req*, *headers*)

Service an authentication request by obtaining a user/password pair and then re-attempting the request. *authreq* ought to name the header that carries the realm information within the request, *host* identifies the URL and path being authenticated against, *req* ought to be the (failed) `Request` object, and *headers* ought to be the error headers.

*host* takes the form of either an authority (e.g. `"python.org"`) or a URL that carries an authority component (e.g. `"https://python.org/"`). Whichever it is, that authority is forbidden to include a userinfo component (hence `"python.org"` and `"python.org:80"` work, whereas `"joe:password@python.org"` does not).

[Subject index](INDEX.md) · [Previous](http-preauthorization-password-state.md) · [Continue](httpbasicauthhandler-http-error-401.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

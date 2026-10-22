# http.cookiejar: Cookie attribute model and standards differences

### Cookie Objects

`Cookie` instances carry Python attributes that loosely line up with the standard cookie-attributes laid out across the assorted cookie standards. The match isn't one-to-one, because intricate rules govern how default values are assigned, because the `max-age` plus `expires` cookie-attributes carry the same information in two forms, and because `http.cookiejar` can "downgrade" [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies from version 1 down to version 0 (Netscape) cookies.

You shouldn't need to assign to these attributes except in rare situations inside a `CookiePolicy` method. The class doesn't enforce internal consistency, so you'd better know what you're doing if you go that route.

[Subject index](INDEX.md) · [Previous](cookie-path-and-domain-strictness.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

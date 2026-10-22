# http.cookies: `Morsel.copy()`, `Morsel.setdefault()`

Morsel.copy(*value*)

Hand back a shallow duplicate of the given Morsel object.

Changed in version 3.5: return a Morsel object instead of a dict.

 Morsel.setdefault(*key*, *value=None*)

Throw an error when key isn't a legitimate [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attribute; in every other case act exactly like [`dict.setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault).

[Subject index](INDEX.md) · [Previous](morsel-value-to-morsel-update.md) · [Continue](example.md) · [Owning module, declaration or section: http.cookies](http-cookies-cookieerror.md) · [Owning module, declaration or section: http.cookies.Morsel](http-cookies-morsel-class.md) · [Owning module, declaration or section: Morsel Objects](http-cookies-morsel-class.md)

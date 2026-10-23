# http.cookies: `Morsel.value`, `Morsel.coded_value`, `Morsel.key`, `Morsel.set()`, `Morsel.isReservedKey()`, `Morsel.output()`, `Morsel.js_output()`, `Morsel.OutputString()`, `Morsel.update()`

expires

 path

 comment

 domain

 max-age

 secure

 version

 httponly

 samesite

 partitioned

Setting the `httponly` attribute marks the cookie so it travels only with HTTP requests and stays hidden from JavaScript. The purpose is to blunt certain cross-site scripting attacks.

The `samesite` attribute governs whether the browser includes the cookie on cross-site requests, which helps blunt CSRF attacks. Its allowed settings are “Strict” (delivered only on same-site requests), “Lax” (delivered on same-site requests plus top-level navigations), and “None” (delivered on both same-site and cross-site requests). Choosing “None” means you must also turn on the “secure” attribute, since modern browsers demand it.

A `partitioned` attribute tells user agents that such cross-site cookies *should* surface only within the very top-level context where they were originally stored. So that a user agent honors this, you **must** likewise enable `Secure`.

On top of that, prefixing partitioned cookies with `__Host` is advised, tying them to the hostname rather than the registrable domain. Consult [CHIPS (Cookies Having Independent Partitioned State)](https://github.com/privacycg/CHIPS/blob/main/README.md) for the complete rundown and worked examples.

These keys ignore case, and `''` is their default value.

Changed in version 3.5: `__eq__()` now takes `key` and `value` into account.

Changed in version 3.7: Attributes `key`, `value` and `coded_value` are read-only. Use `set()` for setting them.

Changed in version 3.8: Added support for the `samesite` attribute.

Changed in version 3.14: Added support for the `partitioned` attribute.

 Morsel.value

The value of the cookie.

 Morsel.coded_value

The cookie's encoded value: the form meant to go over the wire.

 Morsel.key

The name of the cookie.

 Morsel.set(*key*, *value*, *coded_value*)

Set the *key*, *value* and *coded_value* attributes.

 Morsel.isReservedKey(*K*)

Reports whether *K* belongs to the collection of keys recognized by a `Morsel`.

 Morsel.output(*attrs=None*, *header='Set-Cookie:'*)

Produce the Morsel's string form, fit to ship as an HTTP header. Every attribute is present by default; supply *attrs* — a list of which attributes to emit — to override that. The *header* argument defaults to `"Set-Cookie:"`.

 Morsel.js_output(*attrs=None*)

Hand back an embeddable piece of JavaScript that, once a JavaScript-aware browser runs it, has the same effect as delivering the HTTP header would.

Here *attrs* carries the same sense it does in `output()`.

 Morsel.OutputString(*attrs=None*)

Yield a string standing for the Morsel on its own, stripped of any wrapping HTTP or JavaScript.

For *attrs*, the interpretation is identical to the one in `output()`.

 Morsel.update(*values*)

Merge the entries from the *values* dictionary into the Morsel dictionary. Should any key in the *values* dict fail to be a legitimate [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attribute, the call raises an error.

Changed in version 3.5: an error is raised for invalid keys.

[Subject index](INDEX.md) · [Previous](http-cookies-morsel-class.md) · [Continue](morsel-copy-to-morsel-setdefault.md) · [Owning module, declaration or section: http.cookies](http-cookies-cookieerror.md) · [Owning module, declaration or section: http.cookies.Morsel](http-cookies-morsel-class.md) · [Owning module, declaration or section: Morsel Objects](http-cookies-morsel-class.md)

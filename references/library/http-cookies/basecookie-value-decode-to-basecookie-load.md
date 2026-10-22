# http.cookies — Cookie Objects

### Cookie Objects

 BaseCookie.value_decode(*val*)

Given a string form, hand back a `(real_value, coded_value)` tuple. The `real_value` portion may be of any type. Inside `BaseCookie` this routine decodes nothing — it is present purely as a hook for subclasses to replace.

 BaseCookie.value_encode(*val*)

Hand back a `(real_value, coded_value)` tuple. While *val* may hold any type, `coded_value` is always coerced into a string. Within `BaseCookie` this routine encodes nothing — it sits there only so subclasses can supply their own version.

As a rule, `value_encode()` and `value_decode()` ought to undo one another across the range of *value_decode*.

 BaseCookie.output(*attrs=None*, *header='Set-Cookie:'*, *sep='\r\n'*)

Produce a string form ready to go out as HTTP headers. Both *attrs* and *header* get forwarded to every `Morsel`'s `output()` method. The *sep* argument stitches the separate headers together and defaults to `'\r\n'` (CRLF).

 BaseCookie.js_output(*attrs=None*)

Give back a piece of JavaScript you can embed; executed by a JavaScript-capable browser, it behaves just as though the HTTP headers had been delivered.

What *attrs* means here matches its meaning in `output()`.

 BaseCookie.load(*rawdata*)

When *rawdata* is a string, treat it as an `HTTP_COOKIE` and register the values it contains as `Morsel`s. When it is a dictionary instead, this is the same as writing:

```python
for k, v in rawdata.items():
    cookie[k] = v

```

[Subject index](INDEX.md) · [Previous](http-cookies-simplecookie-class.md) · [Continue](http-cookies-morsel-class.md) · [Owning module, declaration or section: http.cookies](http-cookies-cookieerror.md)

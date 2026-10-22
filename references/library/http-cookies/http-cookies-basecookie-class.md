# http.cookies: `http.cookies.BaseCookie`

*class *http.cookies.BaseCookie([*input*])

Behaving like a dictionary, this class maps string keys onto `Morsel` instances as their values. Keep in mind that when you assign a value to a key, that value gets wrapped into a `Morsel` holding both the key and the value before storage.

Should *input* be supplied, the class forwards it to the `load()` method.

[Subject index](INDEX.md) · [Previous](http-cookies-cookieerror.md) · [Continue](http-cookies-simplecookie-class.md) · [Owning module, declaration or section: http.cookies](http-cookies-cookieerror.md)

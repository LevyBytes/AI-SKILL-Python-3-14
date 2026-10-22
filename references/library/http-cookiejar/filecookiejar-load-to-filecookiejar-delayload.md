# http.cookiejar: `FileCookieJar.load()`, `FileCookieJar.revert()`, `FileCookieJar.filename`, `FileCookieJar.delayload`

FileCookieJar.load(*filename=None*, *ignore_discard=False*, *ignore_expires=False*)

Load cookies from a file.

Existing cookies are retained unless a freshly loaded cookie overwrites them.

Arguments are as for `save()`.

The named file has to be in the format the class understands, otherwise `LoadError` is raised. On top of that, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) may be raised, for instance when the file is missing.

Changed in version 3.3: [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) was raised in the past; these days it stands as an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 FileCookieJar.revert(*filename=None*, *ignore_discard=False*, *ignore_expires=False*)

Clear all cookies and reload cookies from a saved file.

`revert()` may raise the very same exceptions that `load()` does. Should something fail, the object's state remains unchanged.

`FileCookieJar` instances expose these public attributes:

 FileCookieJar.filename

Name of the default file where cookies are kept. You may assign to this attribute.

 FileCookieJar.delayload

When true, cookies are loaded lazily from disk. You should not assign to this attribute. It serves only as a hint, since it touches performance alone, not behaviour (except when the on-disk cookies are being changed). A `CookieJar` object is free to disregard it. None of the `FileCookieJar` classes shipped in the standard library load cookies lazily.

[Subject index](INDEX.md) · [Previous](cookiejar-add-cookie-header-to-filecookiejar-save.md) · [Continue](http-cookiejar-mozillacookiejar-class.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md) · [Owning module, declaration or section: CookieJar and FileCookieJar Objects](cookiejar-add-cookie-header-to-filecookiejar-save.md)

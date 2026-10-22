# http.cookiejar: `http.cookiejar.MozillaCookieJar`

### FileCookieJar subclasses and co-operation with web browsers

These `CookieJar` subclasses are supplied for reading and writing.

 *class *http.cookiejar.MozillaCookieJar(*filename=None*, *delayload=None*, *policy=None*)

A `FileCookieJar` capable of loading from and saving cookies to disk in the Mozilla `cookies.txt` file format (which curl plus the Lynx and Netscape browsers use as well).

Note

Details about [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies are lost this way, along with any newer or non-standard cookie-attributes like `port`.

Warning

Make a backup of your cookies before you save if any of them would be inconvenient to lose or have corrupted (a few subtleties can cause the file to shift slightly across a load / save round-trip).

Note as well that any cookies saved while Mozilla is active will end up clobbered by Mozilla.

[Subject index](INDEX.md) · [Previous](filecookiejar-load-to-filecookiejar-delayload.md) · [Continue](http-cookiejar-lwpcookiejar-class.md) · [Owning module, declaration or section: http.cookiejar](http-cookiejar-loaderror.md)

# Python 3.5.0 alpha 1 / library / http cookies

[bpo-23250](https://bugs.python.org/issue?@action=redirect&bpo=23250): Within the http.cookies module, "HttpOnly" and "Secure" are now capitalized to match how the standard spells them.

[bpo-22419](https://bugs.python.org/issue?@action=redirect&bpo=22419): An incoming HTTP request in the wsgiref server is now capped at 65536 bytes, and anything longer gets a 414 error code. Devin Cook contributed the patch.

- Lax cookie parsing in http.cookies could become a security issue once paired with the non-standard cookie handling found in certain web browsers. Sergey Bobrov reported it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

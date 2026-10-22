# urllib.response / Response classes used by urllib: `geturl()`, `info()`, `getcode()`

headers

Hands back the response's headers packaged as an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) instance.

 status

Added in version 3.9.

The status code that the server sent back.

 geturl()

Deprecated since version 3.9: Deprecated in favor of `url`.

 info()

Deprecated since version 3.9: Deprecated in favor of `headers`.

 code

Deprecated since version 3.9: Deprecated in favor of `status`.

 getcode()

Deprecated since version 3.9: Deprecated in favor of `status`.

[Subject index](INDEX.md) · [Previous](urllib-response-addinfourl-class.md) · [Owning module, declaration or section: urllib.response](urllib-response-addinfourl-class.md) · [Owning module, declaration or section: urllib.response.addinfourl; url](urllib-response-addinfourl-class.md)

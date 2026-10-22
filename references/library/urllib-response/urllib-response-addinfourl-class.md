# urllib.response: `urllib.response.addinfourl`

### `urllib.response` — Response classes used by urllib

A bare-bones file-like interface — `read()` and `readline()` among its members — is laid out by the functions and classes that the `urllib.response` module declares. The `urllib.request` module draws on this module's functions behind the scenes. Your usual response object turns out to be a `urllib.response.addinfourl` instance:

`*class *urllib.response.addinfourl`

 url

The URL of the resource that was fetched, often consulted to tell whether a redirect took place.

[Subject index](INDEX.md) · [Previous](../urllib-request/urllib-request-restrictions.md) · [Continue](url-response-address-and-status.md)

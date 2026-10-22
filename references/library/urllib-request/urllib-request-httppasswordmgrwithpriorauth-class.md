# urllib.request: `urllib.request.HTTPPasswordMgrWithPriorAuth`

*class *urllib.request.HTTPPasswordMgrWithPriorAuth

A variant of `HTTPPasswordMgrWithDefaultRealm` that additionally holds a database of `uri -> is_authenticated` mappings. A BasicAuth handler can use it to decide when to send authentication credentials right away instead of first awaiting a `401` response.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](urllib-request-httppasswordmgrwithdefaultrealm-class.md) · [Continue](urllib-request-abstractbasicauthhandler-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

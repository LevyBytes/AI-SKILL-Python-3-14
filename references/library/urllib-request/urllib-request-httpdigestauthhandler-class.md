# urllib.request: `urllib.request.HTTPDigestAuthHandler`

*class *urllib.request.HTTPDigestAuthHandler(*password_mgr=None*)

Manage authentication toward the remote host. *password_mgr*, when supplied, should be something compatible with `HTTPPasswordMgr`; see section HTTPPasswordMgr Objects for the interface that must be supported. When both the Digest Authentication Handler and the Basic Authentication Handler are added, Digest Authentication is always attempted first. Should Digest Authentication again return a 40x response, it is passed along to the Basic Authentication handler to Handle. This Handler method will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when handed an authentication scheme that is neither Digest nor Basic.

Changed in version 3.3: Raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) on unsupported Authentication Scheme.

[Subject index](INDEX.md) · [Previous](urllib-request-abstractdigestauthhandler-class.md) · [Continue](urllib-request-proxydigestauthhandler-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

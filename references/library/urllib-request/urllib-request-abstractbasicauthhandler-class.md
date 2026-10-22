# urllib.request: `urllib.request.AbstractBasicAuthHandler`

*class *urllib.request.AbstractBasicAuthHandler(*password_mgr=None*)

A mixin class that assists with HTTP authentication, toward both the remote host and a proxy. *password_mgr*, when supplied, should be something compatible with `HTTPPasswordMgr`; see section HTTPPasswordMgr Objects for the interface that must be supported. When *passwd_mgr* additionally exposes `is_authenticated` and `update_authenticated` methods (see HTTPPasswordMgrWithPriorAuth Objects), the handler consults the `is_authenticated` result for a given URI to decide whether to attach authentication credentials to the request. When `is_authenticated` yields `True` for the URI, credentials are sent. When `is_authenticated` is `False`, credentials are withheld, and then upon receiving a `401` response the request is re-sent carrying the authentication credentials. Once authentication succeeds, `update_authenticated` is invoked to mark `is_authenticated` as `True` for the URI, so that later requests to the URI or any of its super-URIs include the authentication credentials automatically.

Added in version 3.5: Added `is_authenticated` support.

[Subject index](INDEX.md) · [Previous](urllib-request-httppasswordmgrwithpriorauth-class.md) · [Continue](urllib-request-httpbasicauthhandler-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

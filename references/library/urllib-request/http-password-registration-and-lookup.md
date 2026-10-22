# urllib.request — HTTPPasswordMgr Objects

### HTTPPasswordMgr Objects

These methods are available on `HTTPPasswordMgr` and `HTTPPasswordMgrWithDefaultRealm` objects.

 HTTPPasswordMgr.add_password(*realm*, *uri*, *user*, *passwd*)

*uri* may be a lone URI or else a sequence of URIs. The values *realm*, *user* and *passwd* have to be strings. The effect is that `(user, passwd)` becomes the authentication tokens applied whenever authentication is requested for *realm* together with a super-URI of any URI among those provided.

 HTTPPasswordMgr.find_user_password(*realm*, *authuri*)

Fetch the user/password for the given realm and URI, where one exists. Whenever nothing matches, this method gives back `(None, None)`.

With `HTTPPasswordMgrWithDefaultRealm` objects, should the supplied *realm* turn up no matching user/password, the realm `None` gets searched as a fallback.

[Subject index](INDEX.md) · [Previous](proxyhandler-objects.md) · [Continue](http-preauthorization-password-state.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

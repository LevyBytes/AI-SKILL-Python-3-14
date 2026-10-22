# urllib.request — HTTPPasswordMgrWithPriorAuth Objects

### HTTPPasswordMgrWithPriorAuth Objects

This password manager builds on `HTTPPasswordMgrWithDefaultRealm`, adding the ability to track the URIs for which authentication credentials ought always to be sent.

 HTTPPasswordMgrWithPriorAuth.add_password(*realm*, *uri*, *user*, *passwd*, *is_authenticated=False*)

The parameters *realm*, *uri*, *user*, *passwd* match those of `HTTPPasswordMgr.add_password()`. The starting state of the `is_authenticated` flag, for the supplied URI or list of URIs, comes from *is_authenticated*. Passing `True` for *is_authenticated* causes *realm* to be disregarded.

 HTTPPasswordMgrWithPriorAuth.find_user_password(*realm*, *authuri*)

Same as for `HTTPPasswordMgrWithDefaultRealm` objects

 HTTPPasswordMgrWithPriorAuth.update_authenticated(*self*, *uri*, *is_authenticated=False*)

Update the `is_authenticated` flag for the given *uri* or list of URIs.

 HTTPPasswordMgrWithPriorAuth.is_authenticated(*self*, *authuri*)

Returns the current state of the `is_authenticated` flag for the given URI.

[Subject index](INDEX.md) · [Previous](http-password-registration-and-lookup.md) · [Continue](abstractbasicauthhandler-http-error-auth-reqed.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)

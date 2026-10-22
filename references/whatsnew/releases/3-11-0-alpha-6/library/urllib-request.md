# Python 3.11.0 alpha 6 / library / urllib request

[bpo-46756](https://bugs.python.org/issue?@action=redirect&bpo=46756): Patch a defect in [`urllib.request.HTTPPasswordMgr.find_user_password()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.HTTPPasswordMgr.find_user_password) together with [`urllib.request.HTTPPasswordMgrWithPriorAuth.is_authenticated()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth.is_authenticated) that permitted an authorization bypass. As one illustration, reaching URI `example.org/foobar` succeeded whenever the user held authorization for URI `example.org/foo`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

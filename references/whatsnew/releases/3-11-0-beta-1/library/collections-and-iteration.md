# Python 3.11.0 beta 1 / library / collections and iteration

[bpo-46415](https://bugs.python.org/issue?@action=redirect&bpo=46415): Stop ipaddress.ip_{address,interface,network} from throwing TypeError when it ought to throw ValueError after being handed an invalid tuple as the address parameter.

[bpo-46075](https://bugs.python.org/issue?@action=redirect&bpo=46075): A `CookieJar` paired with `DefaultCookiePolicy` is now able to handle cookies from localhost when domain=localhost is spelled out in the Set-Cookie header.

[bpo-42066](https://bugs.python.org/issue?@action=redirect&bpo=42066): Stop cookies from being sorted inside `CookieJar.__iter__()`, which was extra behavior absent from RFC 2965 and the Netscape cookie protocol. The cookies held in `CookieJar` now keep to the ordering of the `Set-Cookie` header. Iman Kermani authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.10.0 beta 1 / security / urllib request

[bpo-43075](https://bugs.python.org/issue?@action=redirect&bpo=43075): Patch a Regular Expression Denial of Service (ReDoS) vulnerability within [`urllib.request.AbstractBasicAuthHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler). The ReDoS-vulnerable regex carries quadratic worst-case complexity, opening the door to a denial of service while parsing crafted invalid RFCs. This ReDoS issue lives on the client side and depends on remote attackers being in command of the HTTP server.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

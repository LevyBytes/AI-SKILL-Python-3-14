# Python 3.10.0 alpha 7 / library / http client

[bpo-43332](https://bugs.python.org/issue?@action=redirect&bpo=43332): Boost the networking efficiency of [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) whenever a proxy is reached through `set_tunnel()`. Connection setup now issues fewer small send calls.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

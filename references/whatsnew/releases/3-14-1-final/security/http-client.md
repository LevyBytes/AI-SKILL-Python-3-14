# Python 3.14.1 final / security / http client

[gh-119451](https://github.com/python/cpython/issues/119451): Address a possible memory denial of service inside the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) module. Connecting to a malicious server could cause an arbitrary quantity of memory to be allocated. Possible consequences ranged from a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError), swapping, out of memory (OOM) killed processes or containers, through to outright system crashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

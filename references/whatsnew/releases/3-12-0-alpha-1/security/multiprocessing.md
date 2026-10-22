# Python 3.12.0 alpha 1 / security / multiprocessing

[gh-97514](https://github.com/python/cpython/issues/97514): On Linux the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module goes back to filesystem-backed unix domain sockets when talking to the *forkserver* process, rather than relying on the Linux abstract socket namespace. Affected code is only that which opts into the ["forkserver" start method](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

Because abstract sockets carry no permissions, any user sharing the same [network namespace](https://man7.org/linux/man-pages/man7/network_namespaces.7.html) (frequently the entire machine) could have injected code into the multiprocessing *forkserver* process. That opened a path to privilege escalation. Socket permissions rooted in the filesystem confine access to the *forkserver* process user, matching the behavior shipped in Python 3.8 and before.

This shuts down Linux [**CVE 2022-42919**](https://www.cve.org/CVERecord?id=CVE-2022-42919).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

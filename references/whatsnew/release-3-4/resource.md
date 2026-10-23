# What's New In Python 3.4 / resource - resource

### resource

A fresh [`prlimit()`](https://docs.python.org/3.14/library/resource.html#resource.prlimit) function — offered on Linux hosts running a kernel of version 2.6.36 or newer together with glibc 2.13 or newer — lets you read or assign resource ceilings for processes besides the caller itself. (Contributed by Christian Heimes in [bpo-16595](https://bugs.python.org/issue?@action=redirect&bpo=16595).)

Where the Linux kernel is at version 2.6.36 or above, several additional Linux-only constants appear as well: [`RLIMIT_MSGQUEUE`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_MSGQUEUE), [`RLIMIT_NICE`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_NICE), [`RLIMIT_RTPRIO`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_RTPRIO), [`RLIMIT_RTTIME`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_RTTIME), and [`RLIMIT_SIGPENDING`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_SIGPENDING). (Contributed by Christian Heimes in [bpo-19324](https://bugs.python.org/issue?@action=redirect&bpo=19324).)

For FreeBSD release 9 and above, a handful of FreeBSD-only constants now exist: [`RLIMIT_SBSIZE`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_SBSIZE), [`RLIMIT_SWAP`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_SWAP), and [`RLIMIT_NPTS`](https://docs.python.org/3.14/library/resource.html#resource.RLIMIT_NPTS). (Contributed by Claudiu Popa in [bpo-19343](https://bugs.python.org/issue?@action=redirect&bpo=19343).)

[Subject index](INDEX.md) · [Previous source section](re.md) · [Next source section](select.md) · [Release/subject declaration](release-highlights.md)

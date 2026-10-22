# Python 3.8.0 alpha 1 / tests / aix getsockname over af unix family sockets supplies no sockname

[bpo-34490](https://bugs.python.org/issue?@action=redirect&bpo=34490): On AIX, getsockname() over AF_UNIX family sockets supplies no "sockname", so bypass any calls to transport.get_extra_info("sockname")

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

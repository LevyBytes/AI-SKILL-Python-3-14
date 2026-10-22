# Python 3.8.0 alpha 1 / tests / platform

[bpo-11192](https://bugs.python.org/issue?@action=redirect&bpo=11192): Repair `test_socket` for AIX 6.1 onward, where IPv6 zone ids are only handled through `inet_pton6_zone()`. Determine the active platform at runtime with `platform.system()` rather than the build-time `sys.platform()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

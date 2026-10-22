# Python 3.7.0 alpha 1 / tests / build and platforms

[bpo-26936](https://bugs.python.org/issue?@action=redirect&bpo=26936): Repair the test_socket breakages seen on Android - on certain Android API levels getservbyname(), getservbyport() and getaddrinfo() do not function.

[bpo-26944](https://bugs.python.org/issue?@action=redirect&bpo=26944): Repair test_posix on Android, where ‘id -G’ either reports completely wrong values or omits the effective gid.

[bpo-26939](https://bugs.python.org/issue?@action=redirect&bpo=26939): Provide the support.setswitchinterval() helper to stop test_functools from hanging on the Android armv7 qemu emulator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

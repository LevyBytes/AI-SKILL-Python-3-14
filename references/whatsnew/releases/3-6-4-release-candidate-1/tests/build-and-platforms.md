# Python 3.6.4 release candidate 1 / tests / build and platforms

[bpo-31380](https://bugs.python.org/issue?@action=redirect&bpo=31380): On macOS, skip test_httpservers test_undecodable_file because it fails on APFS.

[bpo-31705](https://bugs.python.org/issue?@action=redirect&bpo=31705): On a Linux kernel below 4.5, skip test_socket.test_sha256(). The test fails with ENOKEY under kernel 3.10 (running on ppc64le); the kernel 4.5 release merged a fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

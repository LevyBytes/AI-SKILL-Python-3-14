# Python 3.7.0 alpha 3 / tests / build and platforms

[bpo-31380](https://bugs.python.org/issue?@action=redirect&bpo=31380): On macOS, skip the test_httpservers test_undecodable_file case: it fails under APFS.

[bpo-31705](https://bugs.python.org/issue?@action=redirect&bpo=31705): On any Linux kernel earlier than 4.5, skip test_socket.test_sha256(). With kernel 3.10 (on ppc64le) the test errors out with ENOKEY. The kernel received a fix in 4.5.

[bpo-32138](https://bugs.python.org/issue?@action=redirect&bpo=32138): On Android, skip the test_faulthandler tests that trigger SIGSEGV, and drop the test.support.requires_android_level decorator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

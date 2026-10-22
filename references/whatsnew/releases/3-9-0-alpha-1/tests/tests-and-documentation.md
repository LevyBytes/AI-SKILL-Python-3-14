# Python 3.9.0 alpha 1 / tests / tests and documentation

[bpo-37169](https://bugs.python.org/issue?@action=redirect&bpo=37169): Rewrite the `_PyObject_IsFreed()` unit tests.

[bpo-36919](https://bugs.python.org/issue?@action=redirect&bpo=36919): Make `test_source_encoding.test_issue2301` independent of the implementation. The test will now succeed on both CPython and IronPython.

[bpo-30202](https://bugs.python.org/issue?@action=redirect&bpo=30202): Revise `test.test_importlib.test_abc` so it exercises `find_spec()`.

[bpo-37472](https://bugs.python.org/issue?@action=redirect&bpo=37472): Delete `Lib/test/outstanding_bugs.py`.

[bpo-37199](https://bugs.python.org/issue?@action=redirect&bpo=37199): Repair test failures arising when IPv6 is missing or switched off.

[bpo-37400](https://bugs.python.org/issue?@action=redirect&bpo=37400): Repair test_os.test_chown(): obtain groups via os.getgroups() instead of grp.getgrall(). Also rename the test to test_chown_gid().

[bpo-37252](https://bugs.python.org/issue?@action=redirect&bpo=37252): Repair the assertions inside the `test_close` and `test_events_mask_overflow` devpoll tests.

[bpo-38117](https://bugs.python.org/issue?@action=redirect&bpo=38117): Test against OpenSSL 1.1.1d

[bpo-37805](https://bugs.python.org/issue?@action=redirect&bpo=37805): Tests covering `json.dump(..., skipkeys=True)` were added by Donghee Na.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

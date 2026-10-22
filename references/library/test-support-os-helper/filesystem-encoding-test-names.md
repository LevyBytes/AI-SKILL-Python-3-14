# test.support.os_helper: Filesystem encoding and filename test constants

### `test.support.os_helper` — Utilities for os tests

The `test.support.os_helper` module offers support for os tests.

Added in version 3.10.

 test.support.os_helper.FS_NONASCII

A non-ASCII character that [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) can encode.

 test.support.os_helper.SAVEDCWD

Holds [`os.getcwd()`](https://docs.python.org/3.14/library/os.html#os.getcwd).

 test.support.os_helper.TESTFN

Holds a name that is safe to use as a temporary file's name. Whatever temporary file gets created should afterward be closed and unlinked (removed).

 test.support.os_helper.TESTFN_NONASCII

Holds a filename containing the `FS_NONASCII` character, when one exists. This ensures that, where the filename exists, it can be encoded and decoded under the default filesystem encoding. That lets tests needing a non-ASCII filename be skipped easily on platforms where they cannot function.

 test.support.os_helper.TESTFN_UNENCODABLE

Holds a filename (str type) that ought not to be encodable by the file system encoding in strict mode. It may be `None` where producing such a filename is not feasible.

 test.support.os_helper.TESTFN_UNDECODABLE

Holds a filename (bytes type) that ought not to be decodable by the file system encoding in strict mode. It may be `None` where producing such a filename is not feasible.

 test.support.os_helper.TESTFN_UNICODE

Holds a non-ASCII name for a temporary file.

[Subject index](INDEX.md) · [Previous](../test-support-threading-helper/thread-test-joining-and-concurrent-execution.md) · [Continue](test-support-os-helper-environmentvarguard-class.md)

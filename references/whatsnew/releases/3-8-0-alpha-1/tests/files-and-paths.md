# Python 3.8.0 alpha 1 / tests / files and paths

[bpo-33901](https://bugs.python.org/issue?@action=redirect&bpo=33901): Repair test_dbm_gnu under macOS together with gdbm 1.15: write a bigger value so the file size genuinely changes.

[bpo-35772](https://bugs.python.org/issue?@action=redirect&bpo=35772): Repair the sparse-file tests in test_tarfile running on ppc64 atop the tmpfs filesystem. Mend the routine that checks for sparse-file support on the filesystem: build a file holding data plus "holes" rather than one holding no data. The effective block size of tmpfs equals a page size (tmpfs resides in the page cache). On aarch64, ppc64, ppc64le, RHEL uses 64 KiB pages; only s390x and x86_64 stick with 4 KiB pages, while the test punches holes of 4 KiB.

[bpo-34279](https://bugs.python.org/issue?@action=redirect&bpo=34279): regrtest raises a warning whenever no tests ran inside a given test file. On top of that, a new final result state appears if no test ran across every test file. Patch by Pablo Galindo.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

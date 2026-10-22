# Python 3.8.0 alpha 1 / library / ctypes

[bpo-16865](https://bugs.python.org/issue?@action=redirect&bpo=16865): Allow arrays of 2GiB or larger in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes). Patch by Segev Finer.

[bpo-32647](https://bugs.python.org/issue?@action=redirect&bpo=32647): For dlopen, the ctypes module formerly relied on indirect linking. On platforms providing dl, the shared extension is now linked explicitly with libdl.

[bpo-35847](https://bugs.python.org/issue?@action=redirect&bpo=35847): RISC-V required the CTYPES_PASS_BY_REF_HACK. This fixes the ctypes Structure test_pass_by_value.

[bpo-34558](https://bugs.python.org/issue?@action=redirect&bpo=34558): Fixed a typo in Lib/ctypes/_aix.py

[bpo-35523](https://bugs.python.org/issue?@action=redirect&bpo=35523): Eliminate the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) callback workaround: stop building a callback during startup. This prevents the SELinux alert on `import ctypes` and `import uuid`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

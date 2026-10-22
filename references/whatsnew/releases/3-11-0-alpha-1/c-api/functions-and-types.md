# Python 3.11.0 alpha 1 / c api / functions and types

[bpo-43795](https://bugs.python.org/issue?@action=redirect&bpo=43795): The undocumented `Py_FrozenMain()` function has been taken out of the Limited API.

[bpo-41710](https://bugs.python.org/issue?@action=redirect&bpo=41710): When the timeout is excessively large, the PyThread_acquire_lock_timed() function now clamps it instead of aborting the process. Victor Stinner provided the patch.

[bpo-42747](https://bugs.python.org/issue?@action=redirect&bpo=42747): The `Py_TPFLAGS_HAVE_VERSION_TAG` type flag is now a no-op. The `Py_TPFLAGS_HAVE_AM_SEND` flag (introduced back in 3.10) has been dropped. Neither was ever required, since type objects cannot exist with the pertinent fields absent.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

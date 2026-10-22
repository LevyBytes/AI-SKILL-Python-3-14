# Python 3.8.0 alpha 1 / build / make profile opt will no longer swap cflags nodist cflags

[bpo-35499](https://bugs.python.org/issue?@action=redirect&bpo=35499): `make profile-opt` will no longer swap `CFLAGS_NODIST` for `CFLAGS`. Instead it appends profile-guided optimization (PGO) flags onto `CFLAGS_NODIST`, retaining whatever `CFLAGS_NODIST` flags already exist.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

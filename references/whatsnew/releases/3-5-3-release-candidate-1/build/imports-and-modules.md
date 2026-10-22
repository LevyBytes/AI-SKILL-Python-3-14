# Python 3.5.3 release candidate 1 / build / imports and modules

[bpo-26307](https://bugs.python.org/issue?@action=redirect&bpo=26307): The profile-opt build now extends PGO to cover the built-in modules.

[bpo-25825](https://bugs.python.org/issue?@action=redirect&bpo=25825): Set right the references pointing at Modules/python.exp and ld_so_aix, both needed on AIX. This refreshes a reference to an install path altered back in 3.2a4, and reverts the build-tree reference changes introduced in 3.5.0a1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.7.0 alpha 1 / build / files and paths

[bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404): No longer regenerate generated files using file modification timestamps: that step is now triggered explicitly. Swap `make touch` for `make regen-all`.

[bpo-15819](https://bugs.python.org/issue?@action=redirect&bpo=15819): Drop the duplicate include search directory option used when building away from the source tree.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

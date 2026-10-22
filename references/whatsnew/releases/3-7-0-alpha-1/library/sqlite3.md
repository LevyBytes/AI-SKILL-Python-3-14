# Python 3.7.0 alpha 1 / library / sqlite3

[bpo-9303](https://bugs.python.org/issue?@action=redirect&bpo=9303): The sqlite3 module was migrated onto the _v2 API. Aviv Palivoda wrote the patch.

[bpo-26187](https://bugs.python.org/issue?@action=redirect&bpo=26187): A test verifies the sqlite3 trace callback does not fire repeatedly while a schema changes. The underlying issue was indirectly resolved by adopting sqlite3_prepare_v2() under [bpo-9303](https://bugs.python.org/issue?@action=redirect&bpo=9303). Aviv Palivoda wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

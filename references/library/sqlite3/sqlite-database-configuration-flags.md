# sqlite3: Database-configuration capability and safety flags

sqlite3.SQLITE_DBCONFIG_DEFENSIVE

 sqlite3.SQLITE_DBCONFIG_DQS_DDL

 sqlite3.SQLITE_DBCONFIG_DQS_DML

 sqlite3.SQLITE_DBCONFIG_ENABLE_FKEY

 sqlite3.SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER

 sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION

 sqlite3.SQLITE_DBCONFIG_ENABLE_QPSG

 sqlite3.SQLITE_DBCONFIG_ENABLE_TRIGGER

 sqlite3.SQLITE_DBCONFIG_ENABLE_VIEW

 sqlite3.SQLITE_DBCONFIG_LEGACY_ALTER_TABLE

 sqlite3.SQLITE_DBCONFIG_LEGACY_FILE_FORMAT

 sqlite3.SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE

 sqlite3.SQLITE_DBCONFIG_RESET_DATABASE

 sqlite3.SQLITE_DBCONFIG_TRIGGER_EQP

 sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA

 sqlite3.SQLITE_DBCONFIG_WRITABLE_SCHEMA

The `Connection.setconfig()` and `getconfig()` methods make use of these constants.

Which of these constants you have on hand depends on the SQLite version Python was built against.

Added in version 3.12.

See also

[https://www.sqlite.org/c3ref/c_dbconfig_defensive.html](https://www.sqlite.org/c3ref/c_dbconfig_defensive.html)

SQLite docs: Database Connection Configuration Options

Deprecated since version 3.12, removed in version 3.14: both the `version` constant along with `version_info`.

[Subject index](INDEX.md) · [Previous](sqlite3-threadsafety.md) · [Continue](sqlite3-connection-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: Module constants](sqlite-transaction-and-version-constants.md)

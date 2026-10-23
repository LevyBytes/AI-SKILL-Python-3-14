# sqlite3 - How to adapt custom Python types to SQLite values

### How to adapt custom Python types to SQLite values

Natively, SQLite handles only a narrow range of data types. So that custom Python types can live in SQLite databases, *adapt* each one into a Python type that SQLite already grasps natively.

Two routes exist for adapting Python objects into SQLite types: having the object adapt itself, or relying on an *adapter callable*. The callable wins out over the self-adapting approach. When a library publishes a custom type, allowing that type to adapt itself can be reasonable. From an application developer's standpoint, registering custom adapter functions to keep direct control may suit better.

[Subject index](INDEX.md) · [Previous](how-to-use-placeholders-to-bind-values-in-sql-queries.md) · [Continue](how-to-write-adaptable-objects.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)

# Python 3.11.0 alpha 1 / security / marshal

[bpo-41180](https://bugs.python.org/issue?@action=redirect&bpo=41180): Bring auditing events to the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) module, and quit raising `code.__init__` events for each unmarshalled code object. A code object that is built directly will still raise an event, and an audit event handler should examine or gather the raw marshal data. This trims a sizeable performance cost when loading out of `.pyc` files.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

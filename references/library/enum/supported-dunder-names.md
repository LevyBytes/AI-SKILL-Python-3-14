# enum - Supported `__dunder__` names

### Supported `__dunder__` names

An ordered, read-only mapping of `member_name`:`member` entries is what `__members__` holds, and you can reach it on the class alone.

When you provide `__new__()`, it has to construct and hand back the enum members; setting each member’s `_value_` correctly is strongly advised as well. After every member exists, the method stops being invoked.

[Subject index](INDEX.md) · [Previous](enum-enumdict-class.md) · [Continue](supported-sunder-names.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)

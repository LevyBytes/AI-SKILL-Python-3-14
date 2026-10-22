# Python 3.10.0 alpha 5 / library / enum shift member creation away enummeta new into proto member set name lets

[bpo-42901](https://bugs.python.org/issue?@action=redirect&bpo=42901): [Enum] shift member creation away from `EnumMeta.__new__` and into `_proto_member.__set_name__`, which lets members come into being and be visible inside `__init_subclass__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

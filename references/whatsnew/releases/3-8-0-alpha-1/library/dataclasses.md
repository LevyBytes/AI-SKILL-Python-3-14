# Python 3.8.0 alpha 1 / library / dataclasses

[bpo-33453](https://bugs.python.org/issue?@action=redirect&bpo=33453): Make dataclasses operate correctly with literal string type annotations or with PEP 563 "Postponed Evaluation of Annotations". Only certain string prefixes get recognized for ClassVar ("ClassVar" and "typing.ClassVar") along with InitVar ("InitVar" and "dataclasses.InitVar").

[bpo-33947](https://bugs.python.org/issue?@action=redirect&bpo=33947): Recursive reprs are now handled by dataclasses without a RecursionError being raised.

[bpo-32960](https://bugs.python.org/issue?@action=redirect&bpo=32960): For dataclasses, forbid inheriting frozen from non-frozen classes, and likewise forbid inheriting non-frozen from frozen classes. This limitation is set to ease at some later date.

[bpo-34213](https://bugs.python.org/issue?@action=redirect&bpo=34213): Frozen dataclasses may now declare a field called "object". This formerly clashed with an internal use of "object".

[bpo-33175](https://bugs.python.org/issue?@action=redirect&bpo=33175): Within dataclasses, Field.__set_name__ now resolves the __set_name__ special method against the class, not the instance, of the default value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

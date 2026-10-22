# Python 3.9.0 alpha 1 / library / collections and iteration

[bpo-37555](https://bugs.python.org/issue?@action=redirect&bpo=37555): Fixed `NonCallableMock._call_matcher`, which used to give back a tuple in place of a `_Call` object whenever `self._spec_signature` was present. Elizabeth Uselton contributed the patch.

[bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766): Reshaped feature_version into a (major, minor) tuple.

[bpo-37158](https://bugs.python.org/issue?@action=redirect&bpo=37158): Made statistics.fmean() quicker by trading a function for a generator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

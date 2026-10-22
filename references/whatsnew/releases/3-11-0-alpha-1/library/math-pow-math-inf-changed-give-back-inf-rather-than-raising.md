# Python 3.11.0 alpha 1 / library / math pow math inf changed give back inf rather than raising

[bpo-44339](https://bugs.python.org/issue?@action=redirect&bpo=44339): `math.pow(±0.0, -math.inf)` was changed to give back `inf` rather than raising `ValueError`. That aligns the special-case treatment within `math.pow` with the IEEE 754 standard.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

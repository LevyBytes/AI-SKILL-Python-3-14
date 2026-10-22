# Python 3.10.0 alpha 1 / library / zoneinfo

[bpo-41025](https://bugs.python.org/issue?@action=redirect&bpo=41025): Resolved a problem that blocked subclassing of the C implementation of [`zoneinfo.ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo).

[bpo-41056](https://bugs.python.org/issue?@action=redirect&bpo=41056): Fixed a situation where a MemoryError arising within the zoneinfo module could go unreported or be reported away from its source. (found by Coverity)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

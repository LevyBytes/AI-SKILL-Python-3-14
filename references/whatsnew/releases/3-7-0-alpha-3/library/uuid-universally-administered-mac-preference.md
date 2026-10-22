# Python 3.7.0 alpha 3 / library / can uuid getnode favours returning universally administered mac addresses ahead

[bpo-32107](https://bugs.python.org/issue?@action=redirect&bpo=32107): When it can, `uuid.getnode()` now favours returning universally administered MAC addresses ahead of locally administered ones. That offers a stronger promise of worldwide uniqueness for the UUIDs that `uuid.uuid1()` produces. Should only locally administered MAC addresses be on hand, the first one discovered is what gets returned.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.3 release candidate 1 / library / itertools

[bpo-28322](https://bugs.python.org/issue?@action=redirect&bpo=28322): Repair possible crashes when itertools objects are unpickled from malformed pickle data. The work builds on a patch from John Leitch.

- Repair possible integer overflows and crashes within the mmap module under unusual usage patterns.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

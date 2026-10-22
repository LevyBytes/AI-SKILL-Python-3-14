# Python 3.5.2 release candidate 1 / library / fileinput

[bpo-25447](https://bugs.python.org/issue?@action=redirect&bpo=25447): fileinput now takes sys.stdin as-is when it lacks a buffer attribute, which restores the earlier backward compatibility.

[bpo-15068](https://bugs.python.org/issue?@action=redirect&bpo=15068): Removed the excessive buffering that the fileinput module performed. The bufsize parameter no longer has any effect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

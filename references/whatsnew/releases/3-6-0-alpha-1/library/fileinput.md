# Python 3.6.0 alpha 1 / library / fileinput

[bpo-23883](https://bugs.python.org/issue?@action=redirect&bpo=23883): The following modules gained the missing APIs in __all__ so it lines up with their documented APIs: calendar, csv, enum, fileinput, ftplib, logging, optparse, tarfile, threading and wave. A test.support.check__all__() helper was introduced as well. Jacek Kołodziej, Mauro S. M. Rodrigues and Joel Taddei provided the patches.

[bpo-15068](https://bugs.python.org/issue?@action=redirect&bpo=15068): Removed the excessive buffering that fileinput performed. Its bufsize parameter is now deprecated and disregarded.

[bpo-25447](https://bugs.python.org/issue?@action=redirect&bpo=25447): When sys.stdin lacks a buffer attribute, fileinput now uses it as-is, restoring backward compatibility.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

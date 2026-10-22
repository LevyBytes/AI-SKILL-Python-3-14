# Python 3.6.4 release candidate 1 / library / files and paths

[bpo-32110](https://bugs.python.org/issue?@action=redirect&bpo=32110): For a non-negative *n*, `codecs.StreamReader.read(n)` now hands back no more than *n* characters/bytes. That brings it in line with the `read()` methods on other file-like objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.1 release candidate 1 / library / text and unicode

[bpo-25034](https://bugs.python.org/issue?@action=redirect&bpo=25034): Corrected a string.Formatter issue involving automatic numbering combined with nested format_specs. Anthon van der Neut supplied the patch.

[bpo-25047](https://bugs.python.org/issue?@action=redirect&bpo=25047): Element Tree's emitted XML encoding declaration now keeps whatever letter case the user supplied. That brings back the option to spell encoding names with capitals such as "UTF-8", which had worked under Python 2.

[bpo-24684](https://bugs.python.org/issue?@action=redirect&bpo=24684): Rather than invoking the host's encode() method, socket.socket.getaddrinfo() now uses PyUnicode_AsEncodedString(), so a custom string whose encode() method doesn't hand back a byte string is dealt with properly. The IDNA codec's encoder is likewise now invoked directly instead of through the string's encode() method.

[bpo-25019](https://bugs.python.org/issue?@action=redirect&bpo=25019): Repaired a crash triggered by assigning a non-string key on an expat parser. The work builds on a patch from John Leitch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

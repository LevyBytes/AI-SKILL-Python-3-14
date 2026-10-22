# Python 3.6.5 release candidate 1 / security / difflib

[bpo-32981](https://bugs.python.org/issue?@action=redirect&bpo=32981): The difflib and poplib regexes were open to catastrophic backtracking, and these regexes became likely DOS vectors (REDOS). They have since been reworked. This closes out [**CVE 2018-1060**](https://www.cve.org/CVERecord?id=CVE-2018-1060) along with [**CVE 2018-1061**](https://www.cve.org/CVERecord?id=CVE-2018-1061). Jamie Davis sent the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

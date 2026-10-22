# Python 3.7.0 beta 3 / security / difflib

[bpo-32981](https://bugs.python.org/issue?@action=redirect&bpo=32981): Regexes within difflib and poplib were open to catastrophic backtracking. Those regexes were possible DOS vectors (REDOS) and have since been refactored. This addresses [**CVE 2018-1060**](https://www.cve.org/CVERecord?id=CVE-2018-1060) and [**CVE 2018-1061**](https://www.cve.org/CVERecord?id=CVE-2018-1061). Patch by Jamie Davis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

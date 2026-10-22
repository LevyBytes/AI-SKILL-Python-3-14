# Python 3.7.0 alpha 2 / library / text

[bpo-31648](https://bugs.python.org/issue?@action=redirect&bpo=31648): Path predicate enhancements in ElementTree: Permit whitespace surrounding predicate parts, so ?[a = ?text?]? works rather than forcing the harder-to-read ?[a=?text?]?. Also add text comparison against the current node, as in ?[.=?text?]?. Stefan Behnel wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.3 release candidate 1 / library / email

[bpo-22233](https://bugs.python.org/issue?@action=redirect&bpo=22233): Split email header lines *only* at the CR and LF characters named by the RFC, rather than at any arbitrary unicode line break. A bug in HTTP header parsing is repaired by the same change.

[bpo-27988](https://bugs.python.org/issue?@action=redirect&bpo=27988): Repaired email iter_attachments, which had been wrongly mutating the payload list.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

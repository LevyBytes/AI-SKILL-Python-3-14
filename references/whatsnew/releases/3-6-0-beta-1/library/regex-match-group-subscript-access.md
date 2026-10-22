# Python 3.6.0 beta 1 / library / groups regular expression match object can reached via getitem

[bpo-24454](https://bugs.python.org/issue?@action=redirect&bpo=24454): The groups of a regular expression match object can now be reached via __getitem__. Writing “mo[x]” is the same as “mo.group(x)”.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.7.0 alpha 1 / library / plistlib

[bpo-29196](https://bugs.python.org/issue?@action=redirect&bpo=29196): The plistlib module lost the classes Plist, Dict and _InternalDict, all previously deprecated back in Python 2.4. Within the output of readPlist() and readPlistFromBytes(), Dict values are now ordinary dicts. Attribute access can no longer reach the items held in these dictionaries.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

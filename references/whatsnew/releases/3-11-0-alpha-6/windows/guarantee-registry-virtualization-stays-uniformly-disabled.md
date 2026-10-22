# Python 3.11.0 alpha 6 / windows / guarantee registry virtualization stays uniformly disabled

[bpo-46638](https://bugs.python.org/issue?@action=redirect&bpo=46638): Guarantee registry virtualization stays uniformly disabled. On 3.10 and earlier it remains turned on (a handful of registry writes are shielded), whereas on 3.11 and onward it is turned off (registry edits reach every application).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

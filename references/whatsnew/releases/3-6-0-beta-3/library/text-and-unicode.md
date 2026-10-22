# Python 3.6.0 beta 3 / library / text and unicode

[bpo-25953](https://bugs.python.org/issue?@action=redirect&bpo=25953): re.sub() now signals an error on an invalid numerical group reference within the replacement template even when the pattern goes unmatched in the string. The error message for an invalid group reference now carries the group index along with the reference's position. SilentGhost's patch was the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

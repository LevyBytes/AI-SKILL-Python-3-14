# Python 3.7.0 alpha 1 / library / text

[bpo-30228](https://bugs.python.org/issue?@action=redirect&bpo=30228): io.FileIO's seek() and tell() methods now set the internal seekable attribute, sparing one syscall during open() (whether in buffered or text mode).

[bpo-25953](https://bugs.python.org/issue?@action=redirect&bpo=25953): re.sub() now raises an error on an invalid numerical group reference within a replacement template, even where the pattern never matched the string. The error text for an invalid group reference now reports both the group index and the reference's position. This builds on a patch from SilentGhost.

[bpo-22493](https://bugs.python.org/issue?@action=redirect&bpo=22493): The warning text raised by placing inline flags partway through a regular expression now carries a (truncated) regex pattern. Tim Graham authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

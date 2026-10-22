# Python 3.7.0 release candidate 1 / idle / windows

[bpo-33664](https://bugs.python.org/issue?@action=redirect&bpo=33664): Make IDLE's editor text scroll a line at a time. Formerly both the wheel and the scrollbar handle shifted text by a set pixel count, which left partial lines along the top of the editor box. This adjustment reaches the shell plus grep output windows too, though read-only text views are excluded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

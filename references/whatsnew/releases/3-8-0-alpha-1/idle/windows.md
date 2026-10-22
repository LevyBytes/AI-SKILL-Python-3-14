# Python 3.8.0 alpha 1 / idle / windows

[bpo-34120](https://bugs.python.org/issue?@action=redirect&bpo=34120): Repair the unresponsiveness following the close of particular windows and dialogs.

[bpo-33924](https://bugs.python.org/issue?@action=redirect&bpo=33924): Switch the mainmenu.menudefs key ‘windows’ over to ‘window’. Every remaining menudef key is the lowercase form of its main menu entry.

[bpo-33664](https://bugs.python.org/issue?@action=redirect&bpo=33664): Make IDLE's editor text scroll a line at a time. Formerly both the wheel and the scrollbar handle shifted text by a set pixel count, which left partial lines along the top of the editor box. This adjustment reaches the shell plus grep output windows too, though read-only text views are excluded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

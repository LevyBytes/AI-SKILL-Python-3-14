# Python 3.5.1 release candidate 1 / idle / tkinter

[bpo-25173](https://bugs.python.org/issue?@action=redirect&bpo=25173): Tie tkinter messageboxes to a particular widget. Under Mac OSX, render them as a "sheet". Mark Roseman authored the patch.

[bpo-16893](https://bugs.python.org/issue?@action=redirect&bpo=16893): For Idle doc display, swap help.txt out for help.html. The new idlelib/help.html is an rstripped Doc/build/html/library/idle.html. It reads better than help.txt and will document Idle as shipped more thoroughly. Mark Roseman wrote the tkinter html viewer that handles this file. The EditorWindow.HelpDialog class plus the helt.txt file, both now unused, are deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.0 alpha 1 / idle / tkinter

[bpo-25173](https://bugs.python.org/issue?@action=redirect&bpo=25173): Tie tkinter messageboxes to a particular widget. Under Mac OSX, render them as a "sheet". Mark Roseman contributed this patch.

[bpo-16893](https://bugs.python.org/issue?@action=redirect&bpo=16893): Swapped help.txt out for help.html in the Idle doc display. This new idlelib/help.html is an rstripped Doc/build/html/library/idle.html. It presents better than help.txt and will document Idle as shipped more accurately. The tkinter html viewer capable of handling this file was authored by Rose Roseman. Now that they go unused, the EditorWindow.HelpDialog class along with the helt.txt file are deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# What's New In Python 3.6 / idlelib and IDLE

### idlelib and IDLE

Refactoring and modernization of the idlelib package is ongoing, with goals of giving IDLE a better look and feel while keeping its code simpler to read, test, and extend. One part of the visual cleanup, most noticeable on Linux and Mac, is adopting ttk widgets, chiefly within the dialogs. Because of that shift, IDLE will no longer launch under tcl/tk 8.4; either 8.5 or 8.6 of tcl/tk is now mandatory. Running whichever of those you have at its most recent release is advised.

The act of "Modernizing" also covers renaming idlelib modules and merging some of them. Stripping the partial uppercase from file names parallels how, back in 3.0, Tkinter and TkFont were turned into tkinter and tkinter.font. Consequently, idlelib imports that functioned under 3.5 mostly will fail under 3.6. Expect to need a module name change at minimum (consult idlelib/README.txt), and occasionally additional edits. (For the renaming, Al Swiegart along with Terry Reedy contributed [bpo-24225](https://bugs.python.org/issue?@action=redirect&bpo=24225). The bulk of later idlelib patches have formed, and will keep forming, a piece of this effort.)

To make up for that, the payoff over time should be that several idlelib classes become friendlier to work with, carrying improved APIs along with clarifying docstrings. Further handy details will land in idlelib as they become ready.

New in 3.6.2:

Multiple fixes for autocompletion. (Contributed by Louie Lu in [bpo-15786](https://bugs.python.org/issue?@action=redirect&bpo=15786).)

New in 3.6.3:

Sitting on the File menu and once known as Class Browser, the Module Browser now surfaces functions and classes that are nested, not merely the ones at top level. (Contributed by Guilherme Polo, Cheryl Sabella, and Terry Jan Reedy in [bpo-1612262](https://bugs.python.org/issue?@action=redirect&bpo=1612262).)

What were once extension-based IDLE capabilities have now been rebuilt as ordinary built-in features. The Extensions tab no longer holds their settings, which now live across other tabs of the dialog. (Contributed by Charles Wohlganger and Terry Jan Reedy in [bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099).)

To enhance how it looks as well as how it behaves, the Settings dialog (Options, Configure IDLE) received a partial rewrite. (Contributed by Cheryl Sabella and Terry Jan Reedy in multiple issues.)

New in 3.6.4:

So that the impact of picking a given font is clearer, the font sample now carries an assortment of non-Latin glyphs. (Contributed by Terry Jan Reedy in [bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802).) You may edit that sample to add other characters. (Contributed by Serhiy Storchaka in [bpo-31860](https://bugs.python.org/issue?@action=redirect&bpo=31860).)

New in 3.6.6:

The editor's code context option has been overhauled. Every context line, out to maxlines, appears in the box. The editor scrolls to a line when its context entry is clicked. The Settings dialog's Highlights tab gained context colors usable by custom themes. (Contributed by Cheryl Sabella and Terry Jan Reedy in [bpo-33642](https://bugs.python.org/issue?@action=redirect&bpo=33642), [bpo-33768](https://bugs.python.org/issue?@action=redirect&bpo=33768), and [bpo-33679](https://bugs.python.org/issue?@action=redirect&bpo=33679).)

A fresh API call on Windows informs the OS that tk handles DPI scaling. Under Windows 8.1+ or 10, provided the Python binary's DPI compatibility properties are left as-is and the display exceeds 96 DPI, lines and text ought to look crisper. Otherwise nothing visibly changes. (Contributed by Terry Jan Reedy in [bpo-33656](https://bugs.python.org/issue?@action=redirect&bpo=33656).)

New in 3.6.7:

Whenever output exceeds N lines (the default being 50), it collapses into a button. You set N within the PyShell section under the General page of the Settings dialog. By right clicking the output, you can also squeeze a smaller count of potentially very long lines. To expand collapsed output again, double-click the button to restore it in place, or right-click the button to drop it onto the clipboard or open it in its own window. (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

[Subject index](INDEX.md) · [Previous source section](http-client.md) · [Next source section](importlib.md) · [Release/subject declaration](summary-release-highlights.md)

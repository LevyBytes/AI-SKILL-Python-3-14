# What's New In Python 3.9 / IDLE and idlelib - sys

A setting was added that lets you switch the cursor blink off. (Contributed by Zackery Spytz in [bpo-4603](https://bugs.python.org/issue?@action=redirect&bpo=4603).)

Pressing Escape will now dismiss IDLE completion windows. (Contributed by Johnny Najera in [bpo-38944](https://bugs.python.org/issue?@action=redirect&bpo=38944).)

Keywords were added to the list used for module name completion. (Contributed by Terry J. Reedy in [bpo-37765](https://bugs.python.org/issue?@action=redirect&bpo=37765).)

New in 3.9 maintenance releases

IDLE now calls [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) when launched without the ?-n? flag; before this, user-supplied hooks were skipped. (Contributed by Ken Hilton in [bpo-43008](https://bugs.python.org/issue?@action=redirect&bpo=43008).)

Those preceding changes were also backported into the 3.8 maintenance releases.

The settings dialog has been reorganized. The General tab is divided into separate Windows and Shell/Ed tabs. Help sources, which add entries to the Help menu, were relocated to the Extensions tab. This frees room for additional options while trimming the dialog down, which helps it fit on smaller displays. (Contributed by Terry Jan Reedy in [bpo-40468](https://bugs.python.org/issue?@action=redirect&bpo=40468).) The indent space control was relocated out of the Font tab and into the newly created Windows tab. (Contributed by Mark Roseman and Terry Jan Reedy in [bpo-33962](https://bugs.python.org/issue?@action=redirect&bpo=33962).)

Syntax highlighting is now applied to `.pyi` files. (Contributed by Alex Waygood and Terry Jan Reedy in [bpo-45447](https://bugs.python.org/issue?@action=redirect&bpo=45447).)

[Subject index](INDEX.md) · [Next source section](imaplib.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](http.md) · [Preceding release/subject continuation](http.md)

# Python 3.6.0 alpha 3 / idle / dialog

[bpo-27380](https://bugs.python.org/issue?@action=redirect&bpo=27380): IDLE: introduced query.py holding a base Query dialog plus ttk widgets. That module carried the subclasses SectionName, ModuleName, and HelpSource, which configdialog and file =>Load Module rely on to gather information from users. Every subclass brings its own validity checks. ModuleName lets users correct a bad module name instead of restarting from scratch. Tests were added and the two files folded into the new one were deleted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

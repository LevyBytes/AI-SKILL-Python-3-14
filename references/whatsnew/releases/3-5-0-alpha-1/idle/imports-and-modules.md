# Python 3.5.0 alpha 1 / idle / imports and modules

[bpo-16233](https://bugs.python.org/issue?@action=redirect&bpo=16233): To use a module browser (File : Class Browser, Alt+C) you need an editor window that has a filename. If Class Browser is asked for in another way, whether from a shell, an output window, or an ‘Untitled’ editor, Idle stops showing an error box. Instead it now raises an Open Module box (Alt+M). Enter a valid name, and once a module opens, the matching browser opens alongside it.

[bpo-21986](https://bugs.python.org/issue?@action=redirect&bpo=21986): The pickle module ordinarily leaves code objects unpickled. To stay consistent, running under Idle no longer pickles them either.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

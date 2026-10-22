# Python 3.6.0 alpha 1 / idle / text

[bpo-25313](https://bugs.python.org/issue?@action=redirect&bpo=25313): Reworked the handling of the new built-in text color themes so it more cleanly addresses the compatibility problem that the addition of IDLE Dark introduced. The revised idleConf.CurrentTheme is now used consistently throughout idlelib.

[bpo-24820](https://bugs.python.org/issue?@action=redirect&bpo=24820): IDLE now ships with an "IDLE Dark" built-in text color theme. It is roughly IDLE Classic turned inside out, set against a cobalt blue background. Strings, comments, keywords, — remain green, red, orange, — . On IDLEs that shipped before November 2015, to use it press the "Save as New Custom Theme" button and supply a fresh name like "Custom Dark". Such a custom theme runs on any IDLE release and stays editable.

[bpo-25225](https://bugs.python.org/issue?@action=redirect&bpo=25225): Tightened up and reworked the Idle doc section covering text colors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

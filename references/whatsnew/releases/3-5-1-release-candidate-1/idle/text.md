# Python 3.5.1 release candidate 1 / idle / text

[bpo-25313](https://bugs.python.org/issue?@action=redirect&bpo=25313): Reworked how the new built-in text color themes are handled to better tackle the compatibility issue that arrived alongside IDLE Dark. Throughout idlelib, the revised idleConf.CurrentTheme is now used consistently.

[bpo-24820](https://bugs.python.org/issue?@action=redirect&bpo=24820): IDLE ships with a built-in "IDLE Dark" text color theme. Roughly an inverted IDLE Classic atop a cobalt blue background, it keeps strings, comments, keywords, — colored green, red, orange, — . On IDLE builds shipped before November 2015, click the "Save as New Custom Theme" button and supply a fresh name like "Custom Dark". Any IDLE release will accept that custom theme, and it remains editable.

[bpo-25225](https://bugs.python.org/issue?@action=redirect&bpo=25225): Tighten and rewrite the Idle doc section dealing with text colors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

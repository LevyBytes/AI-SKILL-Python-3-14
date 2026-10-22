# Python 3.6.4 release candidate 1 / idle / dialog

[bpo-31860](https://bugs.python.org/issue?@action=redirect&bpo=31860): Within the IDLE configuration dialog the font sample is now editable. The changes hold while IDLE stays open

[bpo-31459](https://bugs.python.org/issue?@action=redirect&bpo=31459): Change the name of IDLE’s module browser from Class Browser over to Module Browser. What began as a module-level class and method browser turned into a module browser years back once module-level functions were added. Nested classes plus functions arrived yesterday. To preserve backward compatibility the virtual event <&lt;open-class-browser&gt;>, which shows up on the Settings dialog's Keys tab, stays unchanged. Cheryl Sabella wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.0 beta 1 / library / numeric behavior

[bpo-21931](https://bugs.python.org/issue?@action=redirect&bpo=21931): When a bad argument is given, msilib.FCICreate() now raises TypeError rather than a ValueError carrying a bogus FCI error number. Jeffrey Armstrong supplied the patch.

[bpo-23880](https://bugs.python.org/issue?@action=redirect&bpo=23880): Tcl_Obj is now accepted by Tkinter's getint() and getdouble(). Tkinter's getdouble() now takes any number (int included).

[bpo-23728](https://bugs.python.org/issue?@action=redirect&bpo=23728): For empty data, binascii.crc_hqx() could hand back an integer beyond the 0-0xffff range.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

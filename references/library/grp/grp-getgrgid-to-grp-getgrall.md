# grp — `grp` — The group database

## grp — The group database

### `grp` — The group database

---

This module grants access to the Unix group database. Every Unix version offers it.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

A group database entry is delivered as a tuple-like object whose attributes line up with the members of the `group` structure (the Attribute column below; refer to `<grp.h>`):

| Index | Attribute | Meaning |
| --- | --- | --- |
| 0 | gr_name | the group’s name |
| 1 | gr_passwd | the group password in encrypted form; frequently blank |
| 2 | gr_gid | the group ID as a number |
| 3 | gr_mem | the user names of every group member |

In this object the gid arrives as an integer, both name and password arrive as strings, while the roster of members arrives as a list of strings. (Bear in mind that, according to the password database, most users are not spelled out as members of the group they belong to. Consult both databases to assemble full membership information. Bear in mind too that a `gr_name` opening with a `+` or `-` is probably a YP/NIS reference and might be unreachable through `getgrnam()` or `getgrgid()`.)

It defines these items:

 grp.getgrgid(*id*)

Hand back the group database entry matching the supplied numeric group ID. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the requested entry cannot be located.

Changed in version 3.10: when the argument is something other than an integer, such as a float or a string, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is now raised.

 grp.getgrnam(*name*)

Hand back the group database entry matching the supplied group name. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the requested entry cannot be located.

 grp.getgrall()

Hand back a list of every group entry that is available, in no particular order.

See also

Module [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd)

A user-database interface that parallels this one.

[Subject index](INDEX.md)

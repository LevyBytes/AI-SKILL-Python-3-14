# pwd`pwd` - The password database

## pwd - The password database??

### `pwd` - The password database

---

This module opens up access to the Unix user account and password database. It ships on every Unix version.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not iOS.

Entries in the password database come back as a tuple-like object whose attributes line up with the members of the `passwd` structure (Attribute field below, see `<pwd.h>`):

| Index | Attribute | Meaning |
| --- | --- | --- |
| 0 | `pw_name` | Login name |
| 1 | `pw_passwd` | Optional encrypted password |
| 2 | `pw_uid` | Numerical user ID |
| 3 | `pw_gid` | Numerical group ID |
| 4 | `pw_gecos` | User name or comment field |
| 5 | `pw_dir` | User home directory |
| 6 | `pw_shell` | User command interpreter |

The uid and gid items come back as integers, every other one as a string. [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) gets raised whenever the requested entry can't be located.

Note

On traditional Unix the field `pw_passwd` typically holds a password encrypted via a DES-derived algorithm. Most modern unices, though, run a so-called *shadow password* system. On those unices the *pw_passwd* field merely holds an asterisk (`'*'`) or the letter `'x'`, while the encrypted password lives inside a file `/etc/shadow` that isn't world readable. Whether the *pw_passwd* field carries anything useful comes down to the system.

It defines the following items:

 pwd.getpwuid(*uid*)

Hand back the password database entry for the supplied numeric user ID.

 pwd.getpwnam(*name*)

Hand back the password database entry for the supplied user name.

 pwd.getpwall()

Hand back a list of every available password database entry, in arbitrary order.

See also

Module [`grp`](https://docs.python.org/3.14/library/grp.html#module-grp)

An interface onto the group database, much like this one.

[Subject index](INDEX.md) · [Continue](../py-compile/py-compile-pycompileerror-to-py-compile-compile.md)

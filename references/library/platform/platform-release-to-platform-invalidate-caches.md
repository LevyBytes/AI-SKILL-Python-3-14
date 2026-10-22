# platform: `platform.release()`, `platform.system()`, `platform.system_alias()`, `platform.version()`, `platform.uname()`, `platform.invalidate_caches()`

platform.release()

Hands back the system's release, such as `'2.2.0'` or `'NT'`. Where the value cannot be worked out, an empty string comes back.

 platform.system()

Hands back the system/OS name — for example `'Linux'`, `'Darwin'`, `'Java'`, `'Windows'`. Where the value cannot be worked out, an empty string comes back.

Under iOS and Android, what comes back is the user-facing OS name (that is, `'iOS`, `'iPadOS'` or `'Android'`). Should you instead want the kernel name (`'Darwin'` or `'Linux'`), turn to [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname).

 platform.system_alias(*system*, *release*, *version*)

Hands back `(system, release, version)` mapped onto the familiar marketing names that certain systems go by. In a few situations it likewise shuffles the information around to head off confusion that would otherwise arise.

 platform.version()

Hands back the system's release version, for instance `'#3 on degas'`. Where the value cannot be worked out, an empty string comes back.

Under iOS and Android, this stands for the user-facing OS version. Should you want the Darwin or Linux kernel version instead, turn to [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname).

 platform.uname()

A reasonably portable uname interface. Hands back a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) that holds six attributes: `system`, `node`, `release`, `version`, `machine`, and `processor`.

The `processor` value is computed lazily, only when asked for.

Note: the leading two attribute names are not the same as those [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname) shows, where they go by `sysname` and `nodename`.

Any entry that cannot be worked out is set to `''`.

Changed in version 3.3: Result changed from a tuple to a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple).

Changed in version 3.9: `processor` is now computed lazily rather than right away.

 platform.invalidate_caches()

Empties the internal cache holding information like the `uname()`. You will mostly want this when some outside process alters the platform's `node()` and you have to pick up the refreshed value.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](platform-architecture-to-platform-python-version-tuple.md) · [Continue](platform-java-ver.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md) · [Owning module, declaration or section: Cross platform](platform-architecture-to-platform-python-version-tuple.md)
